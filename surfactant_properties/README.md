# Surfactant Property Prediction using Graph Neural Networks

A machine learning project that predicts key surfactant properties including (a) Γmax, (b) γcmc, (c) logCMC from chemical structure of surfactants.

This project implements an ensemble of Graph Neural Networks to predict three critical surfactant properties:

- **Surface Excess (Γmax)**: Maximum surface concentration (mol/m²) 
- **Surface Tension at CMC (γCMC)**: Surface tension at critical micelle concentration (mN/m)
- **Critical Micelle Concentration (LogCMC)**: Logarithm of CMC (M)

The model takes SMILES (Simplified Molecular Input Line Entry System) strings as input and outputs quantitative predictions for these important surfactant characteristics.

## 🎯 Key Features

- **Multi-target Regression**: Simultaneous prediction of three surfactant properties
- **Ensemble Learning**: Uses 5 independent models for robust predictions
- **High Accuracy**: Achieves R² scores of 0.80-0.90 on test data
- **Automated Pipeline**: Complete workflow from training to prediction
- **Comprehensive Evaluation**: Includes parity plots and statistical metrics

## 📊 Model Performance

### Test Set Results (R² scores):
- **Surface Excess**: 0.816
- **Surface Tension at CMC**: 0.904  
- **LogCMC**: 0.903

### Training Set Results (R² scores):
- **Surface Excess**: 0.937
- **Surface Tension at CMC**: 0.946
- **LogCMC**: 0.952

## 🏗️ Model Architecture

- **Framework**: ChemProp (Chemical Property Prediction)
- **Base Model**: Graph Neural Network (GNN)
- **Ensemble Size**: 5 models
- **Training Epochs**: 10 (configurable up to 1000)
- **Molecular Featurization**: SMILES-based graph representation

### Hyperparameters:
- **Message Hidden Dimension**: 300
- **Depth**: 3 layers
- **FFN Hidden Dimension**: 300
- **FFN Layers**: 1
- **Batch Size**: 64

## 📁 Project Structure

```
sg_model/
├── GNN.ipynb                          # Main notebook with training & prediction pipeline
├── data.csv                           # Training dataset with SMILES and properties
├── smiles.csv                         # SMILES for prediction
├── data_prediction.xlsx               # Prediction results
├── output.xlsx                        # Additional results
├── smiles_preds_0.csv                # Model predictions
└── chemprop_training/                 # Training outputs
    └── 071524_chemprop/
        └── 2024-11-14T14-20-06/
            ├── config.toml            # Training configuration
            ├── model_0/ to model_4/   # Ensemble model checkpoints
            │   ├── best.pt           # Best model weights
            │   ├── checkpoints/      # Training checkpoints
            │   └── test_predictions.csv
            ├── train_smiles.csv      # Training split
            ├── val_smiles.csv        # Validation split
            └── test_smiles.csv       # Test split
```

## 🚀 Usage

### Training a New Model Using Your Own Data

Replace `data.csv` and `data_prediction.xlsx` with your own dataset. This file should include SMILES strings and the corresponding experimental values for SurfaceExcess (mol/m²), Gamma_cmc (mN/m), and LogCMC (M).

```bash
chemprop train \
    --data-path your_dataset.csv \

```

### Making Predictions Using the Current Pretrained Model

If using the current pretrained model to make predictions on your surfactants, replace `smiles.csv` with the SMILES of your surfactants.

```bash
chemprop predict \
    --test-path your_smiles.csv \
    --model-path chemprop_training/071524_chemprop/2024-11-14T14-20-06/model_0/checkpoints/best.pt
```

### Running the Complete Pipeline

1. Open `GNN.ipynb` in Jupyter Notebook
2. Execute cells sequentially:
   - **Cell 1**: Train ensemble models
   - **Cell 2**: Scan trained models
   - **Cell 3**: Make predictions on new SMILES
   - **Cell 4**: Generate performance metrics and parity plots

## 📋 Requirements

```python
# Core dependencies
chemprop              # Chemical property prediction framework
pandas               # Data manipulation
numpy                # Numerical computing  
scikit-learn         # Machine learning metrics
matplotlib           # Plotting and visualization
openpyxl            # Excel file handling

# Additional requirements
torch               # Deep learning framework (ChemProp dependency)
rdkit               # Chemical informatics (ChemProp dependency)
```

## 📈 Data Format

### Training Data (`data.csv`)
```csv
smiles,SurfaceExcess (mol/m2),Gamma_cmc (mN/m),LogCMC (M)
CCCCCCCCOCCOCCOCCOCCOCCOCCO,3.59E-06,32.77966102,-1.996644295
CCCCCCCCCOCCOCCOCCOCCOCCOCCOCCOCCO,2.00E-06,,
...
```

### Prediction Input (`smiles.csv`)
```csv
smiles,
CCCCCCCCOCCOCCOCCOCCOCCOCCO,
CCCCCCCCCOCCOCCOCCOCCOCCOCCOCCOCCO,
...
```

## 🔍 Results Analysis

The project includes comprehensive model evaluation with:

- **Parity Plots**: Visual comparison of predicted vs experimental values
- **Statistical Metrics**: R², RMSE, and MAE for each property
- **Error Analysis**: Performance breakdown by train/test splits
- **Automated Reporting**: Results exported to Excel for further analysis

### Performance Visualization

The notebook generates three parity plots showing:
1. Surface Excess predictions (×10⁶ mol/m²)
2. Surface Tension at CMC (mN/m)  
3. LogCMC (M)

Each plot displays both training (black) and test (red) data points with perfect prediction reference lines.

## 🛠️ Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd sg_model
```

2. Install ChemProp:
```bash
pip install chemprop
```

3. Install additional dependencies:
```bash
pip install pandas numpy scikit-learn matplotlib openpyxl
```

4. Run the Jupyter notebook:
```bash
jupyter notebook GNN.ipynb
```

## 📄 Citation

If you use this code or model in your research, please cite our paper:

```bibtex
@article{ham2024gnn,
  title={A GNN-Based QSPR Model for Surfactant Properties},
  author={Ham, Seokgyun and Wang, Xin and Zhang, Hongwei and Lattimer, Brian and Qiao, Rui},
  journal={Colloids and Interfaces},
  volume={8},
  number={6},
  pages={63},
  year={2024},
  publisher={MDPI}
}
```
