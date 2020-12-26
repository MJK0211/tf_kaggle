import numpy as np
import pandas as pd

#1. 데이터
gender = pd.read_csv('./data/csv/gender_submission.csv',
                     index_col=0,
                     header=0,
                     encoding='UTF-8'
)

train = pd.read_csv('./data/csv/train.csv',
                     index_col=0,
                     header=0,
                     encoding='UTF-8'                 
)

test = pd.read_csv('./data/csv/train.csv',
                     index_col=0,
                     header=0,
                     encoding='UTF-8'
)

import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style='darkgrid')

def bar_chart(feature):
    survived = train[train['Survived']==1][feature].value_counts()
    dead = train[train['Survived']==0][feature].value_counts()
    df = pd.DataFrame([survived,dead])
    df.index = ['Survived', 'Dead']
    df.plot(kind='bar', stacked=True, figsize=(10,5))
    plt.show()

bar_chart('Sex')


