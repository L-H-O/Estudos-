# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 20:57:04 2023

Estudo de processamento e leitura de dados

@author: lider
"""
import pandas as pd
import pickle
import requests as re
import os
home = os.getcwd()

from bs4 import BeautifulSoup
from io import BytesIO
#%%
def Wages():
    
    # Scrapping

    aux = "http://pdet.mte.gov.br"

    url = "http://pdet.mte.gov.br/novo-caged"

    link = re.get(url, verify = False)

    soup = BeautifulSoup(link.content, 'html.parser')

    link1 = soup.find_all('li', class_ ="item-6107")[0].find_all('a')[0]['href']

    finallink = aux + link1
    
    return finallink

content = re.get(Wages()).content

#%% Funções dumpers

def pickle_dump(pklname, content):
    
    ''' Processa os dados inputados em um pickle '''
    
    with open(str(pklname)+'.pickle','wb') as handle:
        
        pickle.dump(str(pklname),handle)
    
def excel_dump(fname, content):
    
    ''' Processa os dados inputados em um excel'''
    
    with open(str(fname)+'.xlsx','wb') as handle:
        
        handle.write(content)
           
def dumper(fname, content, file_type):
    
    ''' Processa os dados inputados de acordo com o tipo do arquivo '''
    
    if file_type != '.pickle':
        
        with open(str(fname)+str(file_type),'wb') as handle:
            
            return handle.write(content)    
    else:
        
        with open(str(fname)+str(file_type),'wb') as handle:
            
            return pickle.dump(content,handle)
#%% dumping

pickle_dump('caged',content)
excel_dump('caged',content)

pkldump = dumper('caged', content, '.pickle')
xldump = dumper('caged', content, '.xlsx')

#%% Funções loaders

def read_pickle(pklname):
    
    ''' Lê um arquivo pickle '''
    
    with open(pklname, 'rb') as handle:
        
        pkl_obj = pickle.load(handle)
        
    return pkl_obj

def read_excel(xlname):
    
    ''' Lê um arquivo excel '''
    
    with open(xlname, 'rb') as handle:
        
        xl = handle.read()
        
    return xl

def reader(fname, file_type):
    
    ''' Lê o arquivo de acordo com o tipo '''
    
    if file_type != '.pickle':
    
        with open(str(fname)+str(file_type), 'rb') as handle:
        
            return handle.read()   
    else:
        
        with open(str(fname)+str(file_type), 'rb') as handle:
            
            return pickle.load(handle)
        
rpkl = reader('caged','.pickle')

with open('caged.pickle','rb') as handle:
    
    pkl = pickle.load(handle)
    
#%% reading com loaders

pkl = pd.read_excel(read_pickle('caged.pickle'), sheet_name = 'Tabela 9')

xl = pd.read_excel(read_excel('caged.xlsx'), sheet_name = 'Tabela 9')

#%% reading nativos

dfxl = pd.read_excel('caged.xlsx', sheet_name = 'Tabela 9')
dfpickle = pd.read_excel(pd.read_pickle('caged.pickle'), sheet_name = 'Tabela 9')

#%% removing

os.remove('caged.xlsx')
os.remove('caged.pickle')


