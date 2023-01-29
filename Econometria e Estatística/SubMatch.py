# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 15:58:47 2023

@author: lider
"""

import pandas as pd

import os

os.chdir(r"C:\Users\lider\Programming")

#%% Loading data 

data = pd.read_csv('adult.csv')

# Checking data hygiene

data.describe()

unknowns = (data[data == '?'].count()) # <- ? is equivalent to nan 
unknowns.name = 'Count'

tunknowns = unknowns.sum()

data['income_s'] = 0
data.loc[data['income'] == '>50K', 'income_s'] = 1

data['sex_s'] = 0
data.loc[data['sex'] == 'Female', 'sex_s'] = 1

data['race_s'] = 0
data.loc[data['race'] == 'White', 'race_s'] = 1
data.loc[data['race'] == 'Black', 'race_s'] = 2
data.loc[data['race'] == 'Amer-Indian-Eskimo', 'race_s'] = 3
data.loc[data['race'] == 'Asian-Pac-Islander', 'race_s'] = 4


ey0 = data.loc[data['income_s'] == 0, 'sex_s'].mean()
ey1 = data.loc[data['income_s'] == 1, 'sex_s'].mean()

sdo = ey1 - ey0
#%%

data['age_s'] = 0
data.loc[data['age'] > data.age.mean(), 'age_s'] = 1

data['control'] = 0

data.loc[(data.sex_s == 0) & (data.age_s==1), 'control'] = 1
data.loc[(data.sex_s == 0) & (data.age_s==0), 'control'] = 2
data.loc[(data.sex_s == 1) & (data.age_s==1), 'control'] = 3
data.loc[(data.sex_s == 1) & (data.age_s==0), 'control'] = 4

obs = data.loc[data.income_s == 0].shape[0]

def weighted_avg_effect(df):
    
    diff = df[df.age_s==1].income_s.mean() - df[df.age_s==0].income_s.mean()
    weight = df[df.age_s==0].shape[0]/obs
    return diff*weight

wae = data.groupby(['control']).apply(weighted_avg_effect).sum()
