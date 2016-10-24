#!/usr/bin/python
# -*- coding: utf-8 -*-

# /////////////////////////////////////////////////////
#
# TP3 du module de Techniques de Développement LOGiciel
#
# Groupe 3
# TP réalisé par RIU Clément et SPITZ Anne
#
# Rendu le
#
# /////////////////////////////////////////////////////

import Game
import math
import copy

profondeurMax = 4


def minMax(partie, profondeur, isMax, indiceJoueurIA):
    """

    :param partie:
    :param profondeur:
    :param isMax:
    :return:
    """
    if partie.finPartie() or profondeur <= 0:
        return int(partie.listeJoueurs[indiceJoueurIA].getScore())
    else:
        if isMax:
            valeur = - math.inf
            for direction in Game.directionAcceptable:
                if not partie.isDirectionNonValide(direction):
                    partieLocal = copy.deepcopy(partie)
                    partieLocal.modifiePostion(direction)
                    valeur = max(valeur, minMax(partieLocal, profondeur - 1, False, indiceJoueurIA))
            return int(valeur)
        else:
            valeur = math.inf
            for direction in Game.directionAcceptable:
                if not partie.isDirectionNonValide(direction):
                    partieLocal = copy.deepcopy(partie)
                    partieLocal.modifiePostion(direction)
                    valeur = min(valeur, minMax(partieLocal, profondeur - 1, True, indiceJoueurIA))
            return int(valeur)


def choixDirectionIA(partie):
    """

    :param partie:
    :return:
    """
    score = {}
    indiceJoueurIA = partie.joueurCourant
    print(indiceJoueurIA)
    for direction in Game.directionAcceptable:
        partieLocal = copy.deepcopy(partie)
        if not partieLocal.isDirectionNonValide(direction):
            partieLocal.modifiePostion(direction)
            score[minMax(partieLocal, profondeurMax, False, indiceJoueurIA)] = direction
    print(score)
    maxScore = max (score.keys())
    print(maxScore)
    return score[maxScore]
