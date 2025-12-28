# 表面活性剂性质预测工具箱使用指南

📍 **GitHub项目地址**: https://github.com/your-username/surfactant-gnn-prediction

---

## 🎯 这个工具箱能做什么？

这个工具箱可以通过分子的SMILES结构式，自动预测表面活性剂的三个关键性质：

- **(a) Γmax (表面吸附量)**: 最大表面浓度 (mol/m²)
- **(b) γcmc (CMC时表面张力)**: 临界胶束浓度时的表面张力 (mN/m) 
- **(c) logCMC (临界胶束浓度)**: CMC的对数值 (M)

**简单来说**: 输入分子结构 → 输出三个重要的表面活性剂性质数值

---

## 📦 工具箱里面有什么？

下载这个GitHub项目后，你会得到：

### 🔧 **核心工具**
- `GNN.ipynb` - 主要的操作界面（Jupyter笔记本）
- 已训练好的AI模型（5个ensemble模型）

### 📊 **数据文件** 
- `data.csv` - 训练数据集样例
- `smiles.csv` - 需要预测的分子SMILES列表
- `data_prediction.xlsx` - 预测结果存储文件

### 📁 **模型文件夹**
- `chemprop_training/` - 包含所有训练好的模型权重和配置

---

## 🚀 两种使用方式

### 方式一：直接使用现有模型进行预测 ⚡（推荐新手）

**适用场景**: 你有一些表面活性剂分子，想快速知道它们的性质

**操作步骤**:
1. **准备你的分子数据**
   - 把你的表面活性剂分子转换成SMILES格式
   - 替换 `smiles.csv` 文件，格式如下：
   ```
   smiles,
   CCCCCCCCOCCOCCOCCOCCOCCOCCO,
   CCCCCCCCCOCCOCCOCCOCCOCCOCCOCCOCCO,
   你的其他SMILES...
   ```

2. **运行预测**
   - 打开 `GNN.ipynb`
   - 执行 Cell 2 和 Cell 3
   - 程序会自动用5个模型分别预测，然后整合结果

3. **查看结果**
   - 预测结果会自动保存在 `data_prediction.xlsx` 中
   - 包含每个分子的三种性质预测值

**预期时间**: 几分钟内完成

---

### 方式二：用你自己的数据重新训练模型 🔬（适用于研究者）

**适用场景**: 你有自己的实验数据，想训练专门针对你数据的模型

**操作步骤**:

1. **准备训练数据**
   - 替换 `data.csv`，格式必须包含：
   ```
   smiles,SurfaceExcess (mol/m2),Gamma_cmc (mN/m),LogCMC (M)
   CCCCCCCCOCCOCCOCCOCCOCCOCCO,3.59E-06,32.77966102,-1.996644295
   你的数据...
   ```
   - 同时准备 `data_prediction.xlsx`，包含你想预测的新分子

2. **开始训练**
   - 打开 `GNN.ipynb`
   - 执行 Cell 1 开始训练
   - 程序会自动训练5个模型（ensemble learning）
   
3. **模型预测**
   - 训练完成后，执行 Cell 2 和 Cell 3
   - 用你的新模型预测新分子

4. **性能评估**
   - Cell 3 会自动生成性能图表
   - 显示R²、RMSE、MAE等指标

**预期时间**: 根据数据量，几分钟到几小时不等

---

## 🛠️ 环境配置

### 第一次使用需要安装：
```bash
pip install chemprop pandas numpy scikit-learn matplotlib openpyxl
```

### 运行环境：
- Python 3.7+
- Jupyter Notebook
- 建议有GPU加速（可选）

---

## 📈 模型性能参考

使用提供的训练数据，模型在测试集上的表现：

| 性质 | R² 分数 | 说明 |
|------|---------|------|
| 表面吸附量 (Γmax) | 0.816 | 较好 |
| CMC表面张力 (γcmc) | 0.904 | 优秀 |
| logCMC | 0.903 | 优秀 |

**解读**: R²越接近1.0，预测越准确

---

## 🔍 常见使用场景

### 📋 **场景1: 新分子筛选**
你合成了10个新的表面活性剂，想快速评估哪些有潜力
→ 使用方式一，直接预测

### 📋 **场景2: 数据库扩充** 
你有100个分子的实验数据，想预测另外1000个分子
→ 使用方式二，用你的数据重新训练

### 📋 **场景3: 性质优化**
你想设计具有特定CMC值的表面活性剂
→ 使用方式一，大批量预测候选分子

---

## ⚠️ 重要提醒

1. **SMILES格式**: 确保分子结构转换正确
2. **数据质量**: 训练数据的质量直接影响预测准确性
3. **适用范围**: 模型主要针对表面活性剂分子，其他分子类型可能不准确
4. **结果验证**: 重要应用建议实验验证预测结果

---

## 🆘 遇到问题？

### 常见错误解决：
- **文件格式错误**: 检查CSV/Excel文件格式是否正确
- **依赖包问题**: 重新安装chemprop和相关包
- **内存不足**: 减少batch size或分批处理

### 获取帮助：
- 查看项目GitHub页面的Issues
- 联系项目作者
- 参考ChemProp官方文档

---

## 📄 引用说明

如果你在研究中使用了这个工具箱，请引用原始论文：

```
Ham, S., Wang, X., Zhang, H., Lattimer, B., & Qiao, R. (2024). 
A GNN-Based QSPR Model for Surfactant Properties. 
Colloids and Interfaces, 8(6), 63.
```

---

**🎉 开始使用吧！从下载项目到得到预测结果，通常只需要几分钟时间。**
