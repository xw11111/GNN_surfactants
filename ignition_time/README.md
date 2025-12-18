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

## Usage

To train the model and generate predictions:
```bash
python train.py
```

Ensure `chemprop` and its dependencies are installed in your environment.

