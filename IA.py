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


def mouvement(partie, direction):
    """

    :param partie:
    :param direction:
    :return:
    """
    # Une fois la position valide, on bouge le pion, ajoute les points, modifie la grille et change de joueur.
    partie.positions = Game.add(partie.positions, Game.directionAcceptable[direction])
    partie.listeJoueurs[partie.joueurCourant].augmenteScore(partie.grilleJeu[partie.positions])
    partie.grilleJeu[partie.positions] = None
    partie.joueurCourant = (partie.joueurCourant + 1) % 2


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
                    mouvement(partieLocal, direction)
                    valeur = max(valeur, minMax(partieLocal, profondeur - 1, False, indiceJoueurIA))
            return int(valeur)
        else:
            valeur = math.inf
            for direction in Game.directionAcceptable:
                if not partie.isDirectionNonValide(direction):
                    partieLocal = copy.deepcopy(partie)
                    mouvement(partieLocal, direction)
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
            mouvement(partieLocal, direction)
            score[minMax(partieLocal, profondeurMax, False, indiceJoueurIA)] = direction
    print(score)
    maxScore = max (score.keys())
    print(maxScore)
    return score[maxScore]


def gestionTourIA(partie):
    """
    :param partie:
    :return:
    """
    direction = choixDirectionIA(partie)
    print("DIRECTION DE GLaDOS : ", direction)
    # Une fois la position valide, on bouge le pion, ajoute les points, modifie la grille et change de joueur.
    partie.positions = Game.add(partie.positions, Game.directionAcceptable[direction])
    partie.listeJoueurs[partie.joueurCourant].augmenteScore(partie.grilleJeu[partie.positions])
    partie.grilleJeu[partie.positions] = None
    partie.joueurCourant = (partie.joueurCourant + 1) % 2
