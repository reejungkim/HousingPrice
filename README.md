# HousingPrice
<br></br>
[![Gmail Badge](https://img.shields.io/badge/Gmail-d14836?style=flat-square&logo=Gmail&logoColor=white&link=mailto:reejugn.kim@gmail.com)](mailto:reejung.kim@gmail.com) 
[![Linkedin Badge](https://img.shields.io/badge/-LinkedIn-blue?style=flat-square&logo=Linkedin&logoColor=white&link=www.linkedin.com/in/reejungkim/)](https://www.linkedin.com/in/reejungkim/) 
[![Git page](http://img.shields.io/badge/-Portfolio-black?style=flat-square&logo=github&link=https://reejungkim.github.io/)](https://reejungkim.github.io/)
<br></br>

[Kaggle - predict housing prices](https://www.kaggle.com/c/house-prices-advanced-regression-techniques/overview)

Evaluation method: Root-Mean-Squared-Error (RMSE)


<img src="img/kaggle.png" height="100" width="500">


```
conda install -c conda-forge lightgbm 
conda install -c conda-forge xgboost
```

This repository is divided into two parts

### 1. House pricing prediction using standard ML models installed in scikit-learn

  [See jupyter notebook](Kaggle%20-%20House%20Prices%20ML.ipynb)
   - random forest regression
   - support vector regression
   - gradient boosting regression
   - Optimizer: GridSearchCV
   - model interpretation: LIME, SHAP, feature importance
  <img src='img/lime_img.png' height='300' width='350'>
   
   - Final submission:  [Submission.csv](https://raw.githubusercontent.com/reejungkim/HousingPrice/master/submission.csv)
   - RMSE score: 0.13615


### 2. Housing pricing prediction using Tensorflow


```
pip install tensorflow
```

  [See jupyter notebook](Boston%20housing%20price%20using%20tensorflow.ipynb)
  
<img src="img/learning_rate.png" height="200" width="400">
