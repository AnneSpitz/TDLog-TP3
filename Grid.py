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
point = [5, 10, 20, 50, 100, 200]


class Grid:
    def __init__(self, taille):
        """
        Constructeur de la classe Grid.
        :param taille de la grille souhaitée.
        Si la taille est paire ou négative, on raise une exception.
        """

        if taille % 2 == 0 or taille < 0:
            raise ValueError()
        else:
            self._tableau = [[None for i in range(int(taille))] for i in range(taille)]

    def get_taille(self):
        """
        Assesseur en lecture de la taille de la grille.
        :return: Un int correspondant à la taille de la Grid.
        """

        return len(self._tableau)

    def __getitem__(self, xy):
        """
        Assesseur en lecture de la cellule de coordonnées xy
        :param xy: coordonnées de la cellule à lire
        :return: la valeur de la cellule
        """

        assert xy in self
        return self._tableau[xy[0]][xy[1]]

    def __setitem__(self, xy, valeur):
        """
        Assesseur en écriture de la cellule de coordonnées xy
        :param xy: coordonnées de la cellule à écrire
        :param valeur: valeur à mettre dans la cellule.
        :return:
        """
        self._tableau[xy[0]][xy[1]] = valeur

    def __contains__(self, x):
        """
        :param x: Coordonnée en abscisse.
        :param y: Coordonnée en ordonnée.
        :return: True si les coordonnées x et y sont valides. False sinon.
        """

        taille = self.get_taille()
        return x[0] >= 0 and x[1] >= 0 and x[0] < taille and x[1] < taille

    def affichage_grille(self, position):
        """
        Affiche la grille dans la console.
        :param position: actuelle du joueur
        :return: Rien
        """

        max_length = max(len(str(nombre)) for nombre in point)
        for i in range(self.get_taille()):
            ligne_a_afficher = ""
            for j in range(self.get_taille()):
                if [j, i] == position:
                    ligne_a_afficher += " {0}".format("#" * max_length)
                else:
                    valeur = self[(j, i)]
                    ligne_a_afficher += " {0: <{width}}{1}".format("",
                                                                   ["0", str(valeur)][isinstance(valeur, int)],
                                                                   width=max_length - [1, len(str(valeur))][
                                                                       isinstance(valeur, int)])
            print(ligne_a_afficher)
        print("\n")
        return None
