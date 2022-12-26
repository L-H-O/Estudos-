# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 15:55:47 2022

@author: lider


Created on Thu Dec 8 15:15:00 2022

Versão 2

"""
import pandas as pd
import requests as re

from requests.packages.urllib3.exceptions import InsecureRequestWarning
from datetime import datetime

re.packages.urllib3.disable_warnings(InsecureRequestWarning)

#%%

 

class Expectativas():

  

   ''' Classe que gerencia as expectativas do Focus '''

   

   def splitter(self, data):

      

       ''' Função auxiliar que divide a data por ano de referência '''

   

       data22 = data[data.DataReferencia == '2022']

       data23 = data[data.DataReferencia == '2023']

       data24 = data[data.DataReferencia == '2024']

       data25 = data[data.DataReferencia == '2025']

       data26 = data[data.DataReferencia == '2026']

   

       consol = [i.drop(columns = 'DataReferencia') for i in [data22, data23, data24, data25, data26]]

   

       final = [i.groupby('Data', dropna = False).first() for i in consol]

 

       return final

   

    

   def get_IPCA(self):

      

       ''' Extrai o IPCA '''

 

       link = "https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/ExpectativasMercadoAnuais?$filter=Indicador%20eq%20'IPCA'%20and%20Data%20ge%20'2022-01-07'&$format=json&$select=Indicador,Data,DataReferencia,Mediana"

 

       r = re.get(link, verify = False).json()['value']

      

       data = pd.DataFrame.from_dict(r)

       data.set_index(pd.to_datetime(data.Data), inplace = True)

       data.drop(columns = ['Data', 'Indicador'], inplace = True )

       data.columns = ['DataReferencia', 'IPCA']

 

       data = data[data.index.weekday == 4]

       

       split_data = self.splitter(data)

       

       return split_data

   

   def get_GDP(self):

      

       ''' Extrai o PIB '''

       

       link = "https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/ExpectativasMercadoAnuais?$filter=Indicador%20eq%20'PIB%20Total'%20and%20Data%20ge%20'2022-01-07'&$format=json&$select=Indicador,Data,DataReferencia,Mediana"

   

       r = re.get(link, verify = False, timeout = 5).json()['value']

         

       data = pd.DataFrame.from_dict(r)

       data.set_index(pd.to_datetime(data.Data), inplace = True)

       data.drop(columns = ['Data', 'Indicador'], inplace = True )

       data.columns = ['DataReferencia', 'PIB']

 

       data = data[data.index.weekday == 4]

       

       split_data = self.splitter(data)

       

       return split_data

   

   def get_Selic(self):

       

       ''' Extrai a Selic '''

       

       link = "https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/ExpectativasMercadoAnuais?$filter=Indicador%20eq%20'Selic'%20and%20Data%20ge%20'2022-01-07'&$format=json&$select=Indicador,Data,DataReferencia,Mediana"

   

       r = re.get(link, verify = False, timeout = 5).json()['value']

             

       data = pd.DataFrame.from_dict(r)

       data.set_index(pd.to_datetime(data.Data), inplace = True)

       data.drop(columns = ['Data', 'Indicador'], inplace = True )

       data.columns = ['DataReferencia', 'Selic']

 

       data = data[data.index.weekday == 4]

       

       split_data = self.splitter(data)

       

       return split_data

   

   def get_FX(self):

      

       ''' Extrai o cambio '''

       

       link = "https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/ExpectativasMercadoAnuais?$filter=Indicador%20eq%20'C%C3%A2mbio'%20and%20Data%20ge%20'2022-01-07'&$format=json&$select=Indicador,Data,DataReferencia,Mediana"

   

       r = re.get(link, verify = False, timeout = 5).json()['value']

       

       data = pd.DataFrame.from_dict(r)

       data.set_index(pd.to_datetime(data.Data), inplace = True)

       data.drop(columns = ['Data', 'Indicador'], inplace = True )

       data.columns = ['DataReferencia', 'Selic']

 

       data = data[data.index.weekday == 4]

       

       split_data = self.splitter(data)

       

       return split_data

  

   def get_AR(self):

       

        ''' Extrai a taxa de desocupação '''

       

        link ="https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/ExpectativasMercadoAnuais?$filter=Indicador%20eq%20'Taxa%20de%20desocupa%C3%A7%C3%A3o'%20and%20Data%20ge%20'2022-01-07'&$format=json&$select=Indicador,Data,DataReferencia,Mediana"
       

        r = re.get(link, verify = False, timeout = 5).json()['value']

        

        data = pd.DataFrame.from_dict(r)

        data.set_index(pd.to_datetime(data.Data), inplace = True)

        data.drop(columns = ['Data', 'Indicador'], inplace = True )

        data.columns = ['DataReferencia', 'Taxa de desocupação']

 

        data = data[data.index.weekday == 4]

        

        split_data = self.splitter(data)

        

        return split_data

   

   def Readout(self):

      

       ''' Usado no dia que o relatório sai à criação da base '''

       

       aux = ['2022', '2023', '2024', '2025', '2026']

       

       ipca = pd.concat(self.get_IPCA(), axis = 1)

       ipca.columns = aux

             

       while ipca.index[-1].day != datetime.now().day - 3:

              

           ipca = pd.concat(self.get_IPCA(), axis = 1)

           ipca.columns = aux

                    

       gdp = pd.concat(self.get_GDP(), axis = 1)

       gdp.columns = aux

      

       while gdp.index[-1].day != datetime.now().day - 3:

              

           gdp = pd.concat(self.get_GDP(), axis = 1)

           gdp.columns = aux

           

       selic = pd.concat(self.get_Selic(), axis = 1)

       selic.columns = aux

      

       while selic.index[-1].day != datetime.now().day - 3:

                 

           selic = pd.concat(self.get_Selic(), axis = 1)

           selic.columns = aux

       

       fx = pd.concat(self.get_FX(), axis = 1)

       fx.columns = aux

      

       while fx.index[-1].day != datetime.now().day - 3:

           

           fx = pd.concat(self.get_FX(), axis = 1)

           fx.columns = aux

              

       return ipca, gdp, selic, fx

  

   def Focus(self):

      

       ''' Criação da base em outros dias '''

       

       aux = ['2022', '2023', '2024', '2025', '2026']

        

       ipca = pd.concat(self.get_IPCA(), axis = 1)

       ipca.columns = aux

                                      

       gdp = pd.concat(self.get_GDP(), axis = 1)

       gdp.columns = aux

                         

       selic = pd.concat(self.get_Selic(), axis = 1)

       selic.columns = aux              

         

       fx = pd.concat(self.get_FX(), axis = 1)

       fx.columns = aux

                            

       return ipca, gdp, selic, fx

        

#%% Extração

 

#expec = Expectativas().Focus

   

#ipca, gdp, selic, fx = expec()

 

readout = Expectativas().Readout

 

ipca,gdp,selic,fx = readout()