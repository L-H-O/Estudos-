# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 11:36:00 2023

@author: lider
"""

import sys; sys.path.append(r"C:\Users\lider\Programming\Scrapings")
import pandas as pd
#import os
import statsmodels.api as sm
import dateparser

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

ndates = dates.apply(lambda x : dateparser.parse(x, languages = ['pt'], date_formats = ("%b")))

dates_new = pd.to_datetime(dates, format = "%b/%y")


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

# Composição da DPF, DPMFi e DPFe

def compDPF(df):
    
    df = df[3:]
    df.columns = df.iloc[0,:]
    df = df.iloc[2:]
    df.index.name = 'Date'
    
    return df

# Detentores da DPMFi

def ownersDPMFi(df):
    
    df = df[3:]
    df.columns = df.iloc[0,:]
    df = df.iloc[1:]
    df.index.name = "Date"
    
    return df

# Participação da DPMFi

def partDPMFi(df):
    
    lft = df.loc["LFT":"LTN",:]
    lft = lft[2:]
    lft.columns = lft.iloc[0,:]
    lft = lft[1:].dropna()
    lft.index = pd.to_datetime(lft.index.where(~lft.index.isin(['mar/18*','abr/18*']), ['2018-04-01','2018-03-01']))
    lft.index.name = 'Date'
    
    ltn = df.loc["LTN":"NTN-B",:]
    ltn = ltn[2:]
    ltn.columns = ltn.iloc[0,:]
    ltn = ltn[1:].dropna()
    ltn.index = pd.to_datetime(ltn.index.where(~ltn.index.isin(['mar/18*','abr/18*']), ['2018-04-01','2018-03-01']))
    ltn.index.name = 'Date'
  
    ntnb = df.loc["NTN-B":"NTN-F",:]
    ntnb = ntnb[2:]
    ntnb.columns = ntnb.iloc[0,:]
    ntnb = ntnb[1:].dropna()
    ntnb.index = pd.to_datetime(ntnb.index.where(~ntnb.index.isin(['mar/18*','abr/18*']), ['2018-04-01','2018-03-01']))
    ntnb.index.name = 'Date'
    
    ntnf = df.loc["NTN-F":"OUTROS",:]
    ntnf = ntnf[2:]
    ntnf.columns = ntnf.iloc[0,:]
    ntnf = ntnf[1:].dropna()
    ntnf.index = pd.to_datetime(ntnf.index.where(~ntnf.index.isin(['mar/18*','abr/18*']), ['2018-04-01','2018-03-01']))
    ntnf.index.name = 'Date'
    
    others = df.loc["OUTROS":,:]    
    others = others[2:]
    others.columns = others.iloc[0,:]
    others = others[1:].dropna()
    others.index = pd.to_datetime(others.index.where(~others.index.isin(['mar/18*','abr/18*']), ['2018-04-01','2018-03-01']))
    others.index.name = 'Date'
       
    return lft, ltn, ntnb, ntnf, others

#%% Análise

sheet = 6.1
data = Reserves(RMD(sheet))

dpf, dpmfi, dpfe = Vencimentos(RMD(sheet))

dfpm = PMDPMFi(RMD(sheet))

compdpf, compdpmfi, compdpfe = compDPF(RMD(2.4)), compDPF(RMD(2.5)), compDPF(RMD(2.6))

lft, ltn, ntnb, ntnf, others = partDPMFi(RMD(2.8))


