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


class Player:
    def __init__(self, nom):
        """
        Constructeur.
        _score commence à zéro quoi qu'il arrive.
        :param nom: (str) Nom du joueur.
        """

        self._score = 0
        self._nom = nom

    def getNom(self):
        """
        Assesseur en lecture du nom du joueur.
        :return: Le nom du joueur (str).
        """

        return self._nom

    def getScore(self):
        """
        Assesseur en lecture du score du joueur.
        :return: Le score du joueur (int).
        """

        return self._score

    def augmenteScore(self, valeur):
        """
        Permet d'incrémenter (uniquement) le score du joueur
        :param valeur: (int) Valeur dont on veut augmenter le score du joueur.
        :return: Rien.
        """

        self._score += valeur

    def afficheJoueur(self, maxTailleNom):
        """
        Affiche les noms des joueurs et leurs scores.
        :return: Rien.
        """

        print("{0: <{width}} : {1}".format(self.getNom(), self.getScore(),
                                           width=maxTailleNom - len(self.getNom())))