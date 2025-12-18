'''
# step 1: train the model
import subprocess

subprocess.run("""
chemprop train \
    --data-path dataset_202.csv \
    --task-type regression \
    --epochs 1000 \
    --ensemble-size 5 \
    --batch-size 64 \
    --depth 3 \
    --message-hidden-dim 50 \
    --ffn-num-layers 1 \
    --ffn-hidden-dim 50 \
    --dropout 0.4 \
    --data-seed 0 \
    --save-smiles-splits
""", shell=True, check=True)

'''
# test the model
import os

def scan_files_in_folders(folders):
    models = []
    for folder in folders:
        print(f"Scanning folder: {folder}")
        for root, _, files in os.walk(folder):
            for file in files:
                if 'last' in file:
                    print(os.path.join(root, file))
                    models.append(os.path.join(root, file))
    return models

# List of folders to scan
dir_name = 'chemprop_training/dataset_202/2025-12-17T23-04-04'  # change the folder
folders_to_scan = [dir_name]

models = scan_files_in_folders(folders_to_scan)


# prediction (automated)
xlsx = 'estimated_data.xlsx'
test_path = 'estimated_smiles.csv'
import subprocess
import pandas as pd
import numpy as np
for idx, model in enumerate(models):
    ########################## chemprop predict ###################################
    print(f'predict: {model}')
    command = f"chemprop predict --test-path {test_path} --model-path {model} --preds-path preds{idx}.csv" #--atom-features-path MDFeatureGen/070124_partialcharge_sigma_epsilon.npz --descriptors-path MDFeatureGen/070224_surface_area_head_tail.npz"
    print(command)
    subprocess.run(command, shell=True)
    ########################## end ###################################
    
    df_pred = pd.read_csv(f'preds{idx}.csv')
    df_pred = df_pred.rename(columns={'0':'smiles'})
    
    # add to xlsx file
    df_xlsx =  pd.read_excel(xlsx)
    df_xlsx['pred_0_m'+str(idx)]=df_pred['pred_0']
    df_xlsx.to_excel(xlsx,index=False)

# Create a list of column names to calculate the mean
columns_to_average0 = ['pred_0_m' + str(idx) for idx in range(5)]

# Add the new column by calculating the mean across the specified columns
df_xlsx['pred_0'] = df_xlsx[columns_to_average0].mean(axis=1)
df_xlsx.to_excel(xlsx,index=False)

# calculate the performance of model
# metrics
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

# Load data
df = pd.read_excel("data.xlsx")
test_df = pd.read_csv(dir_name + '/model_0/test_predictions.csv')

# Define parity plot function
def parityplot(y_true, y_pred, color, label):
    # Calculate metrics
    r2 = r2_score(y_true, y_pred)
    print(f'R-squared: {r2}')

    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    print(f'RMSE: {rmse}')

    mae = mean_absolute_error(y_true, y_pred)
    print(f'MAE: {mae}')

    # Scatter plot
    plt.scatter(y_true, y_pred, color=color, label=label)

    # Axis labels
    plt.xlabel('y_true')
    plt.ylabel('y_pred')

# Split DataFrame into train and test
df_train = df[~df['smiles'].isin(test_df['smiles'])]
df_test = df[df['smiles'].isin(test_df['smiles'])]

# Create figure
plt.figure(figsize=(6, 5))
df_train_CMC = df_train.dropna(subset=['logCMC'])
df_test_CMC = df_test.dropna(subset=['logCMC'])
print('train')
y_true = df_train_CMC['logCMC'].to_numpy()
y_true = np.log10((10 ** y_true) * 1e-6)
y_pred = df_train_CMC['pred_0'].to_numpy()
y_pred = np.log10((10 ** y_pred) * 1e-6)
parityplot(y_true, y_pred, 'k', 'train')

print('test')
y_true = df_test_CMC['logCMC'].to_numpy()
y_pred = df_test_CMC['pred_0'].to_numpy()
y_true = np.log10((10 ** y_true) * 1e-6)
y_pred = np.log10((10 ** y_pred) * 1e-6)
parityplot(y_true, y_pred, 'r', 'test')

# Reference line
plt.plot([-5, -1], [-5, -1], '--k')

# Axis labels
plt.xlabel('Experimental logCMC (M)', fontsize=16)
plt.ylabel('Predicted logCMC (M)', fontsize=16)

# Add legend
plt.legend()

# Show plot
plt.show()
