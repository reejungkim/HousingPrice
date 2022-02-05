# HousingPrice
<br></br>
[![Gmail Badge](https://img.shields.io/badge/Gmail-d14836?style=flat-square&logo=Gmail&logoColor=white&link=mailto:reejugn.kim@gmail.com)](mailto:reejung.kim@gmail.com) 
[![Linkedin Badge](https://img.shields.io/badge/-LinkedIn-blue?style=flat-square&logo=Linkedin&logoColor=white&link=www.linkedin.com/in/reejungkim/)](https://www.linkedin.com/in/reejungkim/) 
[![Git page](http://img.shields.io/badge/-Portfolio-black?style=flat-square&logo=github&link=https://reejungkim.github.io/)](https://reejungkim.github.io/)
<br></br>

This repository is divided into two parts

[Kaggle - predict housing prices](https://www.kaggle.com/c/house-prices-advanced-regression-techniques/overview)


<img src="img/kaggle.png" height="100" width="500">


### 1. House pricing prediction using standard ML models installed in scikit-learn
```
conda install -c conda-forge lightgbm 
conda install -c conda-forge xgboost
```

    - model candiates: random forest regression, support vector regression, gradient boosting regression
    - preprocessor: label encoder, robust scaler, normalizer
    - Evaluation method: Root-Mean-Squared-Error (RMSE)
    - Optimizer: GridSearchCV
    - model interpretation: feature importance, local interpretable model-agnostic explanations (LIME)
  <img src='img/lime_local_exp.png' height='200' width='350'>
   
    
  [See jupyter notebook](Kaggle%20-%20House%20Prices%20ML.ipynb)
   
   - Final submission:  [Submission.csv](https://raw.githubusercontent.com/reejungkim/HousingPrice/master/submission.csv)
   - RMSE score: 0.13615


### 2. Housing pricing prediction using Tensorflow


```
pip install tensorflow
```

  [See jupyter notebook](Boston%20housing%20price%20using%20tensorflow.ipynb)
  
<img src="img/learning_rate.png" height="200" width="400">
