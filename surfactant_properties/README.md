# Surfactant Properties Prediction (CMC)

This project aims to predict the Critical Micelle Concentration (CMC) of surfactants based on their chemical structure (SMILES) using Graph Neural Networks (GNNs).

## Project Structure

- `dataset_202.csv`: The core dataset containing 202 surfactant entries with `smiles` and `logCMC` values.
- `data.xlsx`: The original dataset in Excel format.
- `retrain_qin.py`: The script used for retraining the model, performing predictions on new data, and calculating performance metrics.
- `estimated_data.xlsx` / `estimated_smiles.csv`: Data files used for generating CMC predictions for new surfactant candidates.
- `preds0.csv` to `preds4.csv`: Individual prediction outputs from each model in the ensemble.
- `chemprop_training/`: Contains the trained models, split into subdirectories by dataset and timestamp.

## Methodology

### Task Type
The model performs a **regression** task to predict the `logCMC` value.

### Model Training
The project utilizes `chemprop` for training a Message Passing Neural Network (MPNN) ensemble:
- **Task Type**: Regression
- **Epochs**: 1000
- **Ensemble Size**: 5
- **Architecture**: Depth 3, Hidden Dimension 50, Dropout 0.4
- **Splits**: The data is automatically split into training, validation, and test sets.

### Prediction & Ensembling
Predictions are made using an ensemble of 5 models. The final `logCMC` prediction is the average of the outputs from all 5 models, which helps improve robustness and provide a measure of uncertainty.

### Evaluation
Model performance is evaluated using standard regression metrics:
- **R-squared (R²)**
- **Root Mean Squared Error (RMSE)**
- **Mean Absolute Error (MAE)**
Parity plots are generated to visualize the relationship between true and predicted values.

## Usage

To retrain the model or generate predictions on new data:
1. Ensure your target SMILES are in `estimated_smiles.csv`.
2. Update the `dir_name` in `retrain_qin.py` to point to your desired training output directory.
3. Run the script:
   ```bash
   python retrain_qin.py
   ```

## Dependencies
- `chemprop`
- `pandas`
- `numpy`
- `scikit-learn`
- `matplotlib`
- `seaborn`

