# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 17:08:46 2022

@author: lider
"""

import pandas as pd
import requests as re
import dateparser

from bs4 import BeautifulSoup
from pandas.tseries.offsets import DateOffset

#%%
def Wages():
    
    # Scrapping

    aux = "http://pdet.mte.gov.br"

    url = "http://pdet.mte.gov.br/novo-caged"

    link = re.get(url, verify = False)

    soup = BeautifulSoup(link.content, 'html.parser')

    link1 = soup.find_all('li', class_ ="item-6107")[0].find_all('a')[0]['href']

    finallink = aux + link1

# Cleaning

    df = pd.read_excel(finallink, sheet_name = 'Tabela 9',   header = 4, parse_dates = ['Mês'])

    df = df.iloc[:,1:]

    df.dropna(inplace = True)

    df.Mês = pd.to_datetime(df.Mês.apply(lambda x: dateparser.parse(x)))

    df.set_index(df.Mês, inplace = True)

    df.drop(columns = "Mês", inplace = True)

    df.index = df.index.where(~df.index.duplicated(), df[df.index.duplicated()].index[0] + DateOffset(months = 1))

    df.index.name = 'Date'

    final = df.resample('M').last()
    
    return final

wages = Wages()

wages.plot()

table = pd.DataFrame(index = wages.columns)
table['Acumulado'] = table.sum().values
