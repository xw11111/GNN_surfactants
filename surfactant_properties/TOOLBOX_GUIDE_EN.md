# Surfactant Property Prediction Toolbox User Guide

📍 **GitHub Repository**: https://github.com/your-username/surfactant-gnn-prediction

---

## 🎯 What Can This Toolbox Do?

This toolbox can automatically predict three key surfactant properties from molecular SMILES structures:

- **(a) Γmax (Surface Excess)**: Maximum surface concentration (mol/m²)
- **(b) γcmc (Surface Tension at CMC)**: Surface tension at critical micelle concentration (mN/m) 
- **(c) logCMC (Critical Micelle Concentration)**: Logarithm of CMC (M)

**In simple terms**: Input molecular structure → Output three important surfactant property values

---

## 📦 What's Inside the Toolbox?

After downloading this GitHub project, you'll get:

### 🔧 **Core Tools**
- `GNN.ipynb` - Main operation interface (Jupyter notebook)
- Pre-trained AI models (5 ensemble models)

### 📊 **Data Files** 
- `data.csv` - Training dataset example
- `smiles.csv` - List of molecular SMILES for prediction
- `data_prediction.xlsx` - Prediction results storage file

### 📁 **Model Directory**
- `chemprop_training/` - Contains all trained model weights and configurations

---

## 🚀 Two Usage Methods

### Method 1: Direct Prediction with Existing Models ⚡ (Recommended for Beginners)

**Use Case**: You have some surfactant molecules and want to quickly know their properties

**Steps**:
1. **Prepare Your Molecular Data**
   - Convert your surfactant molecules to SMILES format
   - Replace `smiles.csv` file with the following format:
   ```
   smiles,
   CCCCCCCCOCCOCCOCCOCCOCCOCCO,
   CCCCCCCCCOCCOCCOCCOCCOCCOCCOCCOCCO,
   Your other SMILES...
   ```

2. **Run Prediction**
   - Open `GNN.ipynb`
   - Execute Cell 2 and Cell 3
   - The program will automatically predict using 5 models and integrate results

3. **View Results**
   - Prediction results are automatically saved in `data_prediction.xlsx`
   - Contains predicted values for three properties of each molecule

**Expected Time**: Complete within minutes

---

### Method 2: Retrain Models with Your Own Data 🔬 (For Researchers)

**Use Case**: You have your own experimental data and want to train models specifically for your dataset

**Steps**:

1. **Prepare Training Data**
   - Replace `data.csv` with format that must include:
   ```
   smiles,SurfaceExcess (mol/m2),Gamma_cmc (mN/m),LogCMC (M)
   CCCCCCCCOCCOCCOCCOCCOCCOCCO,3.59E-06,32.77966102,-1.996644295
   Your data...
   ```
   - Also prepare `data_prediction.xlsx` containing molecules you want to predict

2. **Start Training**
   - Open `GNN.ipynb`
   - Execute Cell 1 to begin training
   - Program will automatically train 5 models (ensemble learning)
   
3. **Model Prediction**
   - After training completion, execute Cell 2 and Cell 3
   - Use your new models to predict new molecules

4. **Performance Evaluation**
   - Cell 3 will automatically generate performance charts
   - Display metrics like R², RMSE, MAE

**Expected Time**: Minutes to hours depending on data size

---

## 🛠️ Environment Setup

### First-time Installation:
```bash
pip install chemprop pandas numpy scikit-learn matplotlib openpyxl
```

### Runtime Environment:
- Python 3.7+
- Jupyter Notebook
- GPU acceleration recommended (optional)

---

## 📈 Model Performance Reference

Using the provided training data, model performance on test set:

| Property | R² Score | Performance |
|----------|----------|-------------|
| Surface Excess (Γmax) | 0.816 | Good |
| CMC Surface Tension (γcmc) | 0.904 | Excellent |
| logCMC | 0.903 | Excellent |

**Interpretation**: R² closer to 1.0 means more accurate prediction

---

## 🔍 Common Use Cases

### 📋 **Scenario 1: New Molecule Screening**
You synthesized 10 new surfactants and want to quickly assess which ones show promise
→ Use Method 1, direct prediction

### 📋 **Scenario 2: Database Extension** 
You have experimental data for 100 molecules and want to predict 1000 more
→ Use Method 2, retrain with your data

### 📋 **Scenario 3: Property Optimization**
You want to design surfactants with specific CMC values
→ Use Method 1, batch predict candidate molecules

---

## ⚠️ Important Notes

1. **SMILES Format**: Ensure correct molecular structure conversion
2. **Data Quality**: Training data quality directly affects prediction accuracy
3. **Applicability**: Model primarily targets surfactant molecules, other molecule types may be inaccurate
4. **Result Validation**: Important applications should experimentally validate predictions

---

## 🆘 Troubleshooting

### Common Error Solutions:
- **File Format Error**: Check if CSV/Excel file format is correct
- **Package Dependencies**: Reinstall chemprop and related packages
- **Memory Issues**: Reduce batch size or process in batches

### Get Help:
- Check Issues on project GitHub page
- Contact project authors
- Refer to ChemProp official documentation

---

## 📄 Citation

If you use this toolbox in your research, please cite the original paper:

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

---

**🎉 Start Using Now! From downloading the project to getting prediction results usually takes just a few minutes.**
