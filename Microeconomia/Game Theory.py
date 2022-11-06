# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 11:43:35 2022

Estudos Teoria dos Jogos

@author: lider
"""

import numpy as np

#%% Batalha dos Sexos

def game(stratman, startwom):
    
    ''' Tomamos de início que o homem faz a primeira decisão,
        seguido pela mulher '''
    
    utils = np.array([[0,1], [1,0],
         [1,2], [0,0]]).reshape(2,4)
    
    if stratman == 0:
        
        

