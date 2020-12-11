# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 08:23:45 2020

@author: taz
"""
import random
from fonctions import*

with open('mots.txt','r') as f:
    lines=[line.strip() for line in f.readlines()]


def jeu_pendu():
    mot_choisi = choix_mot()
    lettre = entrer_lettre
    test_lettre(lettre, mot_choisi)
    


    
    
from mots import*
from fonctions import*

 

def jouer_pendu():
    mot_choisi=choix_mot()
    liste_lettres=[]
    liste_lettres_fausses=[]
    mot=renvoyer_mot(mot_choisi,liste_lettres)
    print(mot)
    while mot!=mot_choisi :
        lettre = entrer_lettre()
        test_lettre(lettre,mot_choisi)
        mot = renvoyer_mot(mot_choisi,liste_lettres)
        print(mot)