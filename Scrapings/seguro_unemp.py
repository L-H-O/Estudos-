# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 20:18:33 2023

@author: lider
"""

import pandas as pd
import numpy as np
import requests as req

from bs4 import BeautifulSoup
#%%
def Scraper() -> bytes:
    
    url = "http://pdet.mte.gov.br/component/content/article?id=1778"
    
    r = req.get(url,
                verify = False)
    
    soup = BeautifulSoup(r.content, 'html.parser')
    
    link = "http://pdet.mte.gov.br" + soup.find_all('div', class_ = 'item-page')[0].find_all('a')[-1]['href']
    
    return req.get(link, verify = False).content

db = Scraper()

sheets = pd.ExcelFile(db).sheet_names[5:]

def Cleaner(db : pd.DataFrame, sheet : str) -> pd.DataFrame:
    
    df = pd.read_excel(io = db,
                       header = 5, 
                       sheet_name = sheet).T.dropna(how = 'all')
    
    df.columns = df.iloc[0,:]
    df = df.iloc[1:].dropna(axis = 1).astype(np.int64)
    
    df.index = pd.to_datetime(df.index)
    df.index.name = 'Date'
    
    return df

def YTD(df):
    
    return (df
              .groupby(df.index.year)
              .expanding()
              .sum())

dfs = [Cleaner(db, sheet) for sheet in sheets]