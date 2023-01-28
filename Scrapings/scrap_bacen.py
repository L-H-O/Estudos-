# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 21:45:33 2022

@author: lider
"""
# Imports

import pandas as pd

#%% Extração dos dados

def bacen(codigo):

    url = f'https://api.bcb.gov.br/dados/serie/bcdata.sgs.{str(codigo)}/dados?formato=json'

    df = pd.read_json(url)
    
    df.index = pd.to_datetime(df['data'])
    
    df = df['valor']
    
    df.index.name = 'Date'
    
    df.name = 'Value'
    
    return df

code = 10844

selic = bacen(code)

