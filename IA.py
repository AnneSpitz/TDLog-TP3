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

import game
import math
import copy

profondeurMax = 4  # Définie la profondeur maximle de l'algorithme de minMax.


def minMax(partie, profondeur, isMax, indiceJoueurIA):
    """
    Applique l'algorithme de min-max à partie, sur profondeur itération.
    :param partie: (Game) Doit être une copie de la vraie partie sur laquelle doit s'appliquer le
    calcul du min-max.
    :param profondeur: (int) Nombre d'itération maximale. Si profondeur = 0 on passe dans le cas de
    base.
    :param isMax: (bool) Si isMax est vrai on cherche le plus grand résultat, sinon le plus faible.
    :return: Renvoie le score calculer sur le moment, sous forme de int.
    """

    # Cas de base :
    if partie.finPartie() or profondeur <= 0:

        return int(partie.listeJoueurs[indiceJoueurIA].getScore())

    # Récursion :
    else:

        # isMax == True correspond à un coup de l'IA, qui doit prendre le meilleur résultat
        # possible.
        if isMax:

            valeur = - math.inf

            # On teste toute les direction qui sont valides :
            for direction in game.directionAcceptable:
                if partie.isDirectionValide(direction):

                    partieLocal = copy.deepcopy(partie)
                    partieLocal.modifieEtat(direction)
                    # On remplace valeur si le nouveau score calculé par minMax est meilleur (
                    # plus grand), sinon on garde valeur.
                    valeur = max(valeur, minMax(partieLocal, profondeur - 1, False, indiceJoueurIA))

            return int(valeur)

        # isMax == False correspond à un coup du joueur, il faut donc minimiser son score possible.
        else:

            valeur = math.inf

            # On teste toute les direction qui sont valides :
            for direction in game.directionAcceptable:
                if partie.isDirectionValide(direction):

                    partieLocal = copy.deepcopy(partie)
                    partieLocal.modifieEtat(direction)
                    # On remplace valeur si le nouveau score calculé par minMax est meilleur (
                    # plus petit), sinon on garde valeur.
                    valeur = min(valeur, minMax(partieLocal, profondeur - 1, True, indiceJoueurIA))
            return int(valeur)


def choixDirectionIA(partie):
    """
    Permet à l'IA de choisir la direction optimale, en utilisant la fonction minMax.
    :param partie: (Game) Partie en cours, qui va être copiée lors du calcul.
    :return: Renvoie la direction correspondant au score maximale sous forme de str.
    """

    # Initialisaton d'un dictionnaire de score.
    score = {}
    # On sauvegarde l'indice du joueur IA.
    indiceJoueurIA = partie.joueurCourant

    # L'IA tente toutes les directions et va choisir celle dont le minMax renvoie le plus grand
    # score.
    valeurOptimale = 0
    directionChoisie = ""

    for direction in game.directionAcceptable:

        # On effectue une copie profonde de la partie pour pouvoir travailler dessus.
        partieLocal = copy.deepcopy(partie)

        if not partieLocal.isDirectionNonValide(direction):

            # On modifie la position puis on calcule la valeur du minMax.
            partieLocal.modifieEtat(direction)
            valeur = minMax(partieLocal, profondeurMax, False, indiceJoueurIA)

            # On modifie la valeurOptimale et la direction si on a une meilleure valeur.
            if valeur > valeurOptimale:
                valeurOptimale = valeur
                directionChoisie = direction

    return directionChoisie
