# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 09:21:13 2020

@author: taz
"""


#Nombre de chances qu'à le joueur :
nb_chances = 8

#Meilleur score de la partie :
with open('meilleur_score.txt','r') as ms :
    m_s = ms.readline()
    meilleur_score=int(m_s)
    ms.close()

#Création de la liste de jeu avec laquelle on joue :
with open('liste_mots.txt','r') as f:
    lines = [line.strip('\n') for line in f.readlines()]
    f.close()
    