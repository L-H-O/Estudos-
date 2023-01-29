# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 11:36:00 2023

@author: lider
"""

import sys; sys.path.append(r"C:\Users\lider\Programming\Scrapings")
import pandas as pd
#import os
import statsmodels.api as sm
import re

from statsmodels.tsa.x13 import x13_arima_analysis as arima
from RMD import RMD

x13as = r"C:\Users\lider\Programming\WinX13\x13as"

#%% Funções de Limpeza 

# Reserva de Liquidez

def Reserves(df):

    df = df.iloc[3:]
    df.columns = df.iloc[0]
    df = df.iloc[2:]
    df.index.name = 'Date'
    df.index = pd.to_datetime(df.index)
    
    return df

# Emissões e Resgates da DPF

df = RMD(1.2)

dates = df.iloc[3,:]


aux = {'Jan':'Jan', 'Fev':'Feb', 'Mar':'Mar', 'Abr':'Apr',
       'Mai':'May', 'Jun':'Jun', 'Jul':'Jul', 'Ago':'Aug',
       'Set':'Sep', 'Out':'Oct', 'Nov':'Nov', 'Dez':'Dec'}

dates.replace([d[0:3] for d in dates], aux)

date = []

aux2 = [i for i in range(0,len(dates))]

new_dates = []

for k,v in aux.items():
   
    for d in dates:
        
        if k in d[0:3]:
            
           dates[[i for i in range(0,len(dates))]] = d.replace(d[0:3],v)
           
test = pd.Series(new_dates)
test1 = pd.to_datetime(test, format = "%b/%y")

# Vencimentos da DPF

def Vencimentos(df):
    
    dpf = df.loc['DPF':'DPMFi',:][2:]
    dpf.columns = dpf.iloc[0,:]
    dpf = dpf.iloc[2:].dropna()

    dpmfi = df.loc['DPMFi':'DPFe',:][2:]
    dpmfi.columns = dpmfi.iloc[0,:]
    dpmfi = dpmfi.iloc[2:].dropna()

    dpfe = df.loc['DPFe':,:][2:]
    dpfe.columns = dpfe.iloc[0,:]
    dpfe = dpfe.iloc[2:].dropna()
    
    dpf.name = 'Date'
    dpmfi.name = 'Date'
    dpfe.name = 'Date'
    
    return dpf, dpmfi, dpfe

# Prazo médio das emissões da DPMFi

def PMDPMFi(df):
    
    df = df.iloc[3:,:]
    df.columns = df.iloc[0,:]
    df = df.iloc[2:]
    df.name = 'Date'
    
    return df   

# Composição da DPF

def compDPF(df):
    
    df = df[3:]
    df.columns = df.iloc[0,:]
    df = df.iloc[2:]
    df.index.name = 'Date'
    
    return df

# Composição da DPMFi

def compDPMFi(df):
    
    df = df[3:]
    df.columns = df.iloc[0,:]
    df = df.iloc[2:]
    df.index.name = 'Date'
    
    return df

# Composição da DPFe

def compDPFe(df):
    
    df = df[3:]
    df.columns = df.iloc[0,:]
    df = df.iloc[2:]
    df.index.name = 'Date'
    
    return df

#%% Análise

sheet = 3.9
data = Reserves(RMD(sheet))

dpf, dpmfi, dpfe = Vencimentos(RMD(sheet))

dfpm = PMDPMFi(RMD(sheet))

compdpf, compdpmfi, compdpfe = compDPF(RMD(2.4)), compDPMFi(RMD(2.5)), compDPFe(RMD(2.6))

