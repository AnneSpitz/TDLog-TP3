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

# Ensemble des valeurs accessible pour les points de la grille.

import customExceptions

point = [5, 10, 20, 50, 100, 200]

class Grid:
    def __init__(self, taille, tableauValeurs=0):
        """
        Constructeur de la classe Grid.
        :param taille: (int) Taille de la grille crée. Si la taille est paire ou négative, on raise
        une exception.
        :param tableauValeurs: (list) Défini à 0 par défaut, si on rentre une list dedans,
        le type ne sera plus int et la grille sera défini par tableauValeurs.
        """

        # Lorsqu'on importe le tableau de valeurs, la position centrale est mise à 0
        # Elle sera remise à None lors de la construction du jeu
        if not (isinstance(tableauValeurs, int)):
            matriceValeurs = tableauValeurs.as_matrix()
            matriceValeurs[taille // 2, taille // 2] = 0
            self._tableau = [[int(matriceValeurs[abscisse][ordonnee]) for abscisse in range(taille)]
                             for ordonnee in range(taille)]

        # Dans le cas où on ne rentre pas de tableau et où la taille est conforme, on initialise
        # à None les élèments de la grille.
        elif taille < 0:
            raise customExceptions.TailleNegativeError()
        elif taille % 2 == 0:
            raise customExceptions.TaillePaireError()
        else:
            self._tableau = [[None for abscisse in range(int(taille))] for ordonnee in
                             range(taille)]

    def getTaille(self):
        """
        Assesseur en lecture de la taille de la grille.
        :return: Un int correspondant à la taille de la Grid.
        """

        return len(self._tableau)

    def __getitem__(self, coordonnee):
        """
        Assesseur en lecture de la cellule de coordonnées coordonnee.
        :param coordonnee: (list / tuple) Coordonnées de la cellule à lire.
        :return: La valeur de la cellule.
        """

        assert coordonnee in self
        return self._tableau[coordonnee[0]][coordonnee[1]]

    def __setitem__(self, coordonnee, valeur):
        """
        Assesseur en écriture de la cellule de coordonnées coordonnee.
        :param coordonnee: (list / tuple) Coordonnées de la cellule à écrire.
        :param valeur: (int) Valeur à mettre dans la cellule.
        :return: Rien.
        """

        self._tableau[coordonnee[0]][coordonnee[1]] = valeur

    def __contains__(self, coordonnee):
        """
        Surcharge de l'opérateur in.
        :param coordonnee: (list / tuple) Coordonnées de la cellule à tester.
        :return: True si les coordonnées sont valides. False sinon.
        """

        taille = self.getTaille()
        return coordonnee[0] >= 0 and coordonnee[1] >= 0 and coordonnee[0] < taille and \
               coordonnee[1] < taille

    def affichageGrille(self, position):
        """
        Affiche la grille dans la console, avec des 0 sur les cases visitées et ### à la place du
        pion.
        :param position: (tuple / list) Position actuelle du joueur
        :return: Rien
        """

        # On cherche le nombre de digit maximal des points, pour les aligner à gauche.
        maxLength = max(len(str(nombre)) for nombre in point)

        # On parcours la grille, en l'affichant par ligne.
        for ordonnee in range(self.getTaille()):

            ligneAAfficher = ""

            for abscisse in range(self.getTaille()):

                # Si on est à la place du pion :
                if [abscisse, ordonnee] == position:
                    ligneAAfficher += " {0}".format("#" * maxLength)  # On affiche le pion.

                # Sinon on affiche la valeur, aligné à droite.
                else:
                    valeur = self[(abscisse, ordonnee)]

                    # Si la case est non visitée on met la valeur.
                    if isinstance(valeur, int):
                        valeur_a_afficher = str(valeur)
                        largeur_case = maxLength - len(valeur_a_afficher)

                    # Sinon on met un 0.
                    else:
                        valeur_a_afficher = "0"
                        largeur_case = maxLength - 1

                    ligneAAfficher += " {0: <{width}}{1}".format("", valeur_a_afficher,
                                                                 width=largeur_case)

            print(ligneAAfficher)

        print("\n")

        return None

    def writeGridIntoCSV(self, nomFichier):
        """
        Permet d'enregistrer la grille dans un fichier csv.
        :param nomFichier: (str) Nom du fichier où écrire.
        :return: Rien.
        """

        with open(nomFichier, 'w+') as csvfile:
            for ligne in self._tableau:
                csvfile.write(",".join(str(elem) for elem in ligne) + "\n")
