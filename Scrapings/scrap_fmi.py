# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 20:33:34 2022

@author: lider
"""

import pandas as pd
import requests as req
import matplotlib.pyplot as plt

#%%

code = 'CompactData/IFS/M.GB.PMP_IX' 
url ='http://dataservices.imf.org/REST/SDMX_JSON.svc/{}'.format(code)

data = req.get(url).json()['CompactData']['DataSet']['Series']

#base_year = data['@BASE-YEAR']

data_list = [[obs.get('@TIME_PERIOD'), obs.get('@OBS_VALUE')] for obs in data['Obs']]

df = pd.DataFrame(data_list, columns = ['Date', 'Values'])

series = df.set_index(pd.to_datetime(df['Date'])).drop('Date', axis = 1)['Values'].astype('float')

print(series)

#%%

acm = series.resample('Y').sum()

series_rolling = series.rolling(12).mean()

plt.plot(series_rolling.index,series_rolling.values)

plt.plot(acm.index,acm.values)

series_var = series.pct_change()
series_var = series_var[1:]

for i in range(series_var.shape[0]):
     
    aux = [100]
    
    index = (aux[0]*(series_var[i]+1/100))
    
    aux.append(index)



#%%

with pd.ExcelWriter('caminho', engine = 'xlrd') as writer:
    
    series.to_excel(Writer, sheet_name = 'Dados')