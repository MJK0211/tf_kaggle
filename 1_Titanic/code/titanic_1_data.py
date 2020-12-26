

import numpy as np
import pandas as pd

#1. 데이터
gender = pd.read_csv('./1_Titanic/data/csv/gender_submission.csv',
                     index_col=0,
                     header=0,
                     encoding='UTF-8'
)

train = pd.read_csv('./1_Titanic/data/csv/train.csv',
                     index_col=0,
                     header=0,
                     encoding='UTF-8'                 
)

test = pd.read_csv('./1_Titanic/data/csv/test.csv',
                     index_col=0,
                     header=0,
                     encoding='UTF-8'
)

print(gender.shape) #(418, 1)
print(train.shape) #(891, 11)
print(test.shape) #(418, 10)

print(train.isnull().sum())
# Survived      0
# Pclass        0
# Name          0
# Sex           0
# Age         177
# SibSp         0
# Parch         0
# Ticket        0
# Fare          0
# Cabin       687
# Embarked      2
# dtype: int64

print(test.isnull().sum())
# Survived      0
# Pclass        0
# Name          0
# Sex           0
# Age         177
# SibSp         0
# Parch         0
# Ticket        0
# Fare          0
# Cabin       687
# Embarked      2
# dtype: int64
# Pclass        0
# Name          0
# Sex           0
# Age          86
# SibSp         0
# Parch         0
# Ticket        0
# Fare          1
# Cabin       327
# Embarked      0
# dtype: int64