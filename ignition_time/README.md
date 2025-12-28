# Ignition Time Prediction

This project focuses on predicting the ignition time of chemical compounds using Graph Neural Networks (GNNs), specifically through the `chemprop` library.

## Project Structure

- `data.csv`: The primary dataset containing SMILES strings and their corresponding ignition `time`.
- `data.xlsx`: The original dataset in Excel format.
- `train.py`: The main script for data preprocessing, model training, and evaluation.
- `all_smiles_for_prediction.csv`: A list of SMILES strings used for model evaluation and making predictions.
- `smiles.csv`: A supplementary list of SMILES strings.
- `chemprop_training/`: Directory containing trained models, configurations, and logs.

## Methodology

### Data Preprocessing
The model treats ignition time prediction as a **multi-class classification** task. The continuous `time` values are binned into three classes:
- **Class 0**: `time < 200`
- **Class 1**: `200 <= time <= 800`
- **Class 2**: `time > 800`

This conversion is handled within `train.py`, which generates a `data_class.csv` for training.

### Model Training
The project uses `chemprop` to train a GNN ensemble. Key training parameters (configurable in `train.py`):
- **Task Type**: Classification
- **Epochs**: 100
- **Ensemble Size**: 5
- **Architecture**: Depth 1, Hidden Dimension 20

### Evaluation
The script evaluates the models using classification metrics such as:
- Accuracy
- Confusion Matrix
- F1-Score

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Option 1: Using the Pretrained Model for Predictions

If you want to predict ignition times for your own surfactants using the pretrained model, follow these steps:

1. **Prepare your SMILES data**: Replace the content of `smiles.csv` with your surfactant SMILES strings. The file should have a header row with the column name `smiles`:

```csv
smiles
CCCCCCCCCCCC[N+](C)(C)C.[Br-]
CCCCCCCC[N+](C)(C)C.[Br-]
YOUR_SMILES_STRING_HERE
```

2. **Use the trained model**: The pretrained model is located in `chemprop_training/hyperparam_run_11/model_0/checkpoints/`. You can make predictions using:

```bash
chemprop predict \
    --test-path smiles.csv \
    --model-path chemprop_training/hyperparam_run_11/model_0/checkpoints/best-epoch=2-val_loss=0.56.ckpt \
```

3. **Interpret the results**: The output `predictions.csv` will contain probability scores for each class:
   - **Class 0**: `time < 200` (fast ignition)
   - **Class 1**: `200 <= time <= 800` (medium ignition)
   - **Class 2**: `time > 800` (slow ignition)

### Option 2: Retraining the Model with Your Own Dataset

If you want to train a new model with your own surfactant data:

1. **Prepare your dataset**: Replace both `data.csv` and `data.xlsx` with your own dataset. The CSV file must contain at least two columns:
   - `smiles`: SMILES representation of your surfactants
   - `time`: Ignition time values (continuous numerical values)

Example format for `data.csv`:

```csv
smiles,time
CCCCCCCCCCCC[N+](C)(C)C.[Br-],678.3
CCCCCCCC[N+](C)(C)C.[Br-],0
YOUR_SMILES_STRING,YOUR_TIME_VALUE
```

2. **Run the training script**:

```bash
python train.py
```

This script will:
   - Convert the continuous ignition times into three classes automatically
   - Train an ensemble of 5 GNN models
   - Generate predictions on your dataset
   - Display evaluation metrics (accuracy, confusion matrix, F1-score)
   - Save the trained models in the `chemprop_training/` directory

3. **Review the results**: The script outputs:
   - Train and test set evaluation metrics
   - Confusion matrices visualized with matplotlib
   - Trained model checkpoints for future predictions

### Customizing Training Parameters

You can modify the training hyperparameters in `train.py`:
- `--epochs`: Number of training epochs (default: 100)
- `--ensemble-size`: Number of models in the ensemble (default: 5)
- `--batch-size`: Training batch size (default: 16)
- `--depth`: Number of message passing steps (default: 1)
- `--message-hidden-dim`: Hidden dimension for message passing (default: 20)
- `--ffn-hidden-dim`: Hidden dimension for feed-forward network (default: 20)
- `--dropout`: Dropout rate (default: 0.2)

## Requirements

Ensure `chemprop` and its dependencies are installed in your environment (see `requirements.txt`).

