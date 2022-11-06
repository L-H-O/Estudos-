# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 11:07:56 2022

Estudos OOP

@author: lider
"""
#%% Classe de consumidor --> QuantEcon

class Consumer():
    
    ''' Creates a consumer object as outlined by QuantEcon '''    
    
    def __init__(self, w, name = 'Bob'):
        
        self.w = w
        self.name = name
        
    def earn(self, e):
        
        self.w += e
        
    def spend(self, s):
        
        self.w -= s
        
        return self.w

    
#%% Testes --> consumidor
    
c1 = Consumer(10, 'Erika')

print(f'Initial wealth is {c1.w}')

c1.spend(7)

print(f"After paying off her debts, {c1.name}'s wealth is {c1.w}")

c1.earn(5)

print(f"Ater receiving a government benefit, {c1.name}'s final wealth stands at {c1.w}")

#%%


