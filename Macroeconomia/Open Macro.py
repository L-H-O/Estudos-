# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 11:44:04 2022

Estudos Macro Aberta

@author: lider
"""

import numpy as np
import pandas as pd
from pandas_datareader import data
from datetime import datetime as date

#%%

def exchange():

    ''' Extrai a taxa de câmbio com a precisão de duas casas decimais '''
    
    exchange_rate =  round(data.DataReader('BRL=X', 'yahoo')['Adj Close']\
                    [pd.to_datetime(date.today()).strftime("%Y/%m/%d")], 2 )

    return exchange_rate

exchange_rate = exchange()
    

