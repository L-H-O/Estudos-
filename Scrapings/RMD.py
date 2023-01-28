# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 10:02:24 2023

@author: lider
"""
# Setup -> importação das bibliotecas necessárias 

import requests as req
import zipfile as zf
import os
import pandas as pd

from io import BytesIO
from bs4 import BeautifulSoup
from requests.packages.urllib3.exceptions import InsecureRequestWarning

req.packages.urllib3.disable_warnings(InsecureRequestWarning)

home = os.getcwd()

#%%

def RMD(sheet_name = None):

    # Scraping    

    url = "https://www.tesourotransparente.gov.br/publicacoes/relatorio-mensal-da-divida-rmd"

    link0 = req.get(url, verify = False)

    soup0 = BeautifulSoup(link0.content, 'html.parser')

    url1 = soup0.find_all('ul', class_ = "anexos")[0].find_all('a')[0]['href']

    link1 = req.get(url1, verify = False)

    soup1 = BeautifulSoup(link1.content, 'html.parser')

    url2 = soup1.find_all('frame')[0]['src']

    r = req.get(url2, verify = False).content
    
    # Processamento e extração

    anexo = zf.ZipFile(BytesIO(r))
    
    fname = [fname.filename for fname in anexo.infolist()][0]
    
    anexo.extractall(path = home)
    
    # Criação do DF
    
    df = pd.read_excel(fname, sheet_name = str(sheet_name), index_col = 0)
    
    # Remoção do arquivo excel bruto
    
    os.remove(fname)
    
    return df
        
df = RMD(4.2)
