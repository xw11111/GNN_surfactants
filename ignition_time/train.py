
import pandas as pd
import subprocess

# Load your data
df = pd.read_csv('data.csv')

# --- Convert regression target to multi-class classification target ---
def assign_label(time_value):
    if time_value < 200:
        return 0
    elif 200 <= time_value <= 800:
        return 1
    else:  # time_value > 800
        return 2

# Assuming your target column is 'time'. If not, change 'time' to your column name.
target_column = 'time'
classification_column = f'{target_column}_class'

if target_column in df.columns:
    df[classification_column] = df[target_column].apply(assign_label)
else:
    raise ValueError(f"Target column '{target_column}' not found in data.csv")

# Save the modified data to a new file for classification training
classification_data_path = 'data_class.csv'
# We are only saving smiles and the new classification column for chemprop
# to avoid confusion with the original regression target.
df[['smiles', classification_column]].to_csv(classification_data_path, index=False)


# step 1: train the model
# The command is updated for a classification task
subprocess.run(f"""
chemprop train \
    --data-path {classification_data_path} \
    --task-type classification \
    --epochs 100 \
    --ensemble-size 5 \
    --batch-size 16 \
    --depth 1 \
    --message-hidden-dim 20 \
    --ffn-num-layers 1 \
    --ffn-hidden-dim 20 \
    --dropout 0.2 \
    --data-seed 0 \
    --save-smiles-splits
""", shell=True, check=True)


# NOTE: The rest of this script is for the original regression task.
# You will need to update it to use multi-class classification metrics
# (like accuracy, confusion matrix, F1-score) instead of regression metrics (R-squared, RMSE, MAE).

# --- Part 2: Automated Prediction and Classification Evaluation ---

# test the model
import os
import glob
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Automatically find the latest training directory
try:
    list_of_dirs = glob.glob('chemprop_training/data/*/')
    latest_dir = max(list_of_dirs, key=os.path.getctime)
    print(f"Automatically selected latest training directory: {latest_dir}")
    dir_name = latest_dir
except (ValueError, FileNotFoundError):
    print("Could not automatically find training directory. Please set 'dir_name' manually.")
    dir_name = 'chemprop_training/data/' # Fallback, please change if needed

def scan_files_in_folders(folders):
    """Scans for model files ('best.pt' or 'last.pt') in the specified folders."""
    models = []
    for folder in folders:
        print(f"Scanning folder: {folder}")
        # Prefer 'best.pt' saved based on validation performance
        model_paths = glob.glob(os.path.join(folder, 'model_*/best.pt'))
        if not model_paths:
             # Fallback to 'last.pt' if 'best.pt' is not found
            model_paths = glob.glob(os.path.join(folder, 'model_*/last.pt'))
        models.extend(model_paths)
    print(f"Found {len(models)} models.")
    return models

folders_to_scan = [dir_name]
models = scan_files_in_folders(folders_to_scan)


# prediction (automated)
# We need to predict on all the smiles from the original dataset to evaluate train/test sets
df_full_smiles = pd.read_csv('data.csv')[['smiles']]
test_path = 'all_smiles_for_prediction.csv'
df_full_smiles.to_csv(test_path, index=False)

all_preds_probs = []
if models:
    for idx, model in enumerate(models):
        ########################## chemprop predict ###################################
        print(f'predicting with model: {model}')
        preds_path = f"preds{idx}.csv"
        command = f"chemprop predict --test-path {test_path} --model-path {model} --preds-path {preds_path}"
        subprocess.run(command, shell=True, check=True)
        ########################## end ###################################
        
        df_pred = pd.read_csv(preds_path)
        # For classification, predictions are probabilities per class.
        # Find probability columns dynamically (e.g., 'time_class_0', 'time_class_1', ...)
        prob_columns = [c for c in df_pred.columns if c.startswith(classification_column)]
        all_preds_probs.append(df_pred[prob_columns].values)

# Average the probabilities across all models in the ensemble
avg_probs = np.mean(all_preds_probs, axis=0)

# Get the predicted class by finding the index of the max probability
predicted_classes = np.argmax(avg_probs, axis=1)

# Load data with true labels and add predictions
df_with_labels = pd.read_csv(classification_data_path)
df_with_labels['predicted_class'] = predicted_classes


# --- Calculate and display the performance of the model ---

def print_classification_metrics(y_true, y_pred, title=""):
    """Calculates and prints classification metrics and plots a confusion matrix."""
    print(f"--- {title} ---")
    accuracy = accuracy_score(y_true, y_pred)
    print(f'Accuracy: {accuracy:.4f}')
    print('Classification Report:')
    # classification_report can fail if a class in the test set is never predicted,
    # which can happen with small, imbalanced datasets.
    try:
        print(classification_report(y_true, y_pred, zero_division=0))
    except ValueError as e:
        print(f"Could not generate classification report: {e}")

    # Plot confusion matrix
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(6, 5))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.xlabel('Predicted Label')
    plt.ylabel('True Label')
    plt.title(f'Confusion Matrix - {title}')
    plt.show()


# Split DataFrame into train and test to evaluate separately using the splits from chemprop
test_smiles_path = os.path.join(dir_name, 'model_0/test_smiles.csv')

try:
    test_df_smiles = pd.read_csv(test_smiles_path)
    
    df_eval = df_with_labels.copy()

    df_train = df_eval[~df_eval['smiles'].isin(test_df_smiles['smiles'])]
    df_test = df_eval[df_eval['smiles'].isin(test_df_smiles['smiles'])]

    # Evaluate train set
    y_true_train = df_train[classification_column]
    y_pred_train = df_train['predicted_class']
    print_classification_metrics(y_true_train, y_pred_train, title="Train Set Evaluation")

    # Evaluate test set
    y_true_test = df_test[classification_column]
    y_pred_test = df_test['predicted_class']
    print_classification_metrics(y_true_test, y_pred_test, title="Test Set Evaluation")

except FileNotFoundError:
    print(f"Warning: Could not find '{test_smiles_path}'. Cannot split into train/test for evaluation.")
    print("Evaluating on the full dataset instead.")
    y_true_full = df_with_labels[classification_column]
    y_pred_full = df_with_labels['predicted_class']
    print_classification_metrics(y_true_full, y_pred_full, title="Full Dataset Evaluation")
