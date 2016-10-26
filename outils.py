#!/usr/bin/python
# -*- coding: utf-8 -*-

# /////////////////////////////////////////////////////
#
# TP3 du module de Techniques de Développement LOGiciel
#
# Groupe 3
# TP réalisé par RIU Clément et SPITZ Anne
#
# Rendu le 26 octobre 2016
#
# /////////////////////////////////////////////////////



def add(x, y):
    """
    Permet d'additionner terme à terme deux couples ou deux tableaux.
    :param x, y: (tuple / list) Vecteurs à additionner terme à terme.
    :return: Renvoie le tableau des résultats sous forme de list.
    """
    assert (len(x) == len(y))
    return [x[i] + y[i] for i in range(len(x))]


def maxEtIndice(liste):
    """
    Fonction qui calcule le max d'une liste et cherche les indices des maximums.
    :param liste: (list) La liste dont on souhaite connaître le maximum.
    :return: une list de la forme [max, nombreMax, [listeIndice]]
    """

    maximum = max(liste)
    nombreMax = 0
    listeIndice = []
    for indice in range(len(liste)):
        if liste[indice] == maximum:
            nombreMax += 1
            listeIndice.append(indice)

    return [maximum, nombreMax, listeIndice]
