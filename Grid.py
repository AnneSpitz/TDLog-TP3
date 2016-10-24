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
point = [5, 10, 20, 50, 100, 200]


class Grid:
    def __init__(self, taille, tableauValeurs=0):
        """
        Constructeur de la classe Grid.
        :param taille de la grille souhaitée.
        Si la taille est paire ou négative, on raise une exception.
        """

        # Lorsqu'on importe le tableau de valeurs, la position centrale est mise à 0
        # Elle sera remise à None lors de la construction du jeu
        if not (isinstance(tableauValeurs, int)):
            matriceValeurs = tableauValeurs.as_matrix()
            matriceValeurs[taille // 2, taille // 2] = 0
            self._tableau = [[int(matriceValeurs[i][j]) for
                              i in range(taille)] for j in range(taille)]
        elif taille % 2 == 0 or taille < 0:
            raise ValueError()
        else:
            self._tableau = [[None for i in range(int(taille))] for i in range(taille)]

    def getTaille(self):
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

        taille = self.getTaille()
        return x[0] >= 0 and x[1] >= 0 and x[0] < taille and x[1] < taille

    def affichageGrille(self, position):
        """
        Affiche la grille dans la console.
        :param position: actuelle du joueur
        :return: Rien
        """

        maxLength = max(len(str(nombre)) for nombre in point)
        for i in range(self.getTaille()):
            ligneAAfficher = ""
            for j in range(self.getTaille()):
                if [j, i] == position:
                    ligneAAfficher += " {0}".format("#" * maxLength)
                else:
                    valeur = self[(j, i)]
                    ligneAAfficher += " {0: <{width}}{1}".format("",
                                                                   ["0", str(valeur)][isinstance(valeur, int)],
                                                                   width=maxLength - [1, len(str(valeur))][
                                                                       isinstance(valeur, int)])
            print(ligneAAfficher)
        print("\n")
        return None

    def writeGridIntoCSV(self, nomFichier):
        with open(nomFichier, 'w+') as csvfile:
            for ligne in self._tableau:
                csvfile.write(",".join(str(elem) for elem in ligne) + "\n")
