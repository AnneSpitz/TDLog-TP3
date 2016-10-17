#!/usr/bin/python
# -*- coding: utf-8 -*-

# /////////////////////////////////////////////////////
#
# TP2 du module de Techniques de Développement LOGiciel
#
# Groupe 3
# TP réalisé par RIU Clément et SPITZ Anne
#
# Rendu le 14 octobre 2016
#
# /////////////////////////////////////////////////////


class Player:
    def __init__(self, nom):
        """
        Constructeur. _score commence à zéro quoi qu'il arrive.
        :param nom:
        """

        self._score = 0
        self._nom = nom

    def get_nom(self):
        """
        Assesseur en lecture du nom du joueur
        """
        return self._nom

    def get_score(self):
        """
        Assesseur en lecture du score du joueur.
        """

        return self._score

    def augmente_score(self, valeur):
        """
        Permet d'incrémenter (uniquement) le score du joueur
        :param valeur: nombre dont on veut augmenter le score
        :return: Rien
        """

        self._score += valeur

    def affiche_joueur(self, max_taille_nom):
        """
        Affiche les noms des joueurs et leurs scores.
        :return: Rien
        """

        print("{0: <{width}} : {1}".format(self.get_nom(), self.get_score(),
                                           width=max_taille_nom - len(self.get_nom())))