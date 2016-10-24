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


import random
import pandas

from Grid import *
from Player import *

# Différentes combinaisons de touches possibles pour les contrôles, permet de choisir ses
# touches de contrôle
tabDirectionAcceptable = [{"8": [0, -1], "4": [-1, 0], "2": [0, 1], "6": [1, 0],
                             "7": [-1, -1], "9": [1, -1], "1": [-1, 1], "3": [1, 1]},
                            {"z": [0, -1], "q": [-1, 0], "x": [0, 1], "d": [1, 0],
                             "a": [-1, -1], "e": [1, -1], "w": [-1, 1], "c": [1, 1]}]

commandesChoisies = 1

directionAcceptable = tabDirectionAcceptable[commandesChoisies]


def add(x, y):
    """
    Permet d'additionner terme à terme deux couples ou deux tableaux
    :param x, y: couples ou tableaux à additionner terme à terme
    :return: tableau des résultats
    """

    assert (len(x) == len(y))
    return [x[i] + y[i] for i in range(len(x))]


class Game:
    def __init__(self, joueur1, joueur2, taille=0,
                 tableauValeurs=0):
        """
        Constructeur.
        :param taille: Taille de la grille
        :param joueur1: Nom du premier joueur
        :param joueur2: Nom du deuxième joueur
        """

        self.joueurCourant = 0

        self.listeJoueurs = [Player(joueur1), Player(joueur2)]

        if not isinstance(tableauValeurs, int):
            taille = len(tableauValeurs)

        if not isinstance(tableauValeurs, int):
            print("bonjour")
            self.grilleJeu = Grid(taille, tableauValeurs)
        else:
            self.grilleJeu = Grid(taille)

            for x in range(taille):
                for y in range(taille):
                    self.grilleJeu[(x, y)] = random.choice(point)

        # La position initiale est mise à 0 : elle est déjà explorée.

        self.grilleJeu[
            (taille // 2,
             taille // 2)] = None

        self.positions = [taille // 2, taille // 2]

    def demandeDirection(self):
        """
        Demande à l'utilisateur de rentrer une touche du clavier.
        :return: une string correspondant à la touche demandée.
        """

        return input(
            "À {0} de jouer. \n "
            "Appuyez sur une touche parmi : "
            "{1}; {2}; {3}; {4}; {5}; {6}; {7}; {8}. Choisissez une case non vide.".format(
                self.listeJoueurs[self.joueurCourant].getNom(),
                *directionAcceptable.keys()))

    def isDirectionNonValide(self, direction):
        """
        teste si la direction demandée est incompatible ou si on peut continuer
        :return: False si la direction est correcte et qu'on peut continuer
                 True si la direction n'est pas correcte et qu'il faut redemander
        """
        print(self.positions)
        print(direction)


        if direction not in directionAcceptable.keys():
            print("pas valide")
            return True
        else:
            positionVoulue = add(self.positions, directionAcceptable[direction])
            print(positionVoulue)
            if positionVoulue not in self.grilleJeu:
                print("TEST TA GUEULE")
                return True
            elif not isinstance(self.grilleJeu[positionVoulue], int):
                return True
            else:
                return False

    def gestionTour(self):
        """
        Permet de jouer pour le joueur courant, puis passe la main.
        :param direction: direction dans laquel le joueur veut se déplacer.
        :return: Rien
        """

        direction = self.demandeDirection()

        # On demande la direction tant que celle-ci n'est pas valide.
        while self.isDirectionNonValide(direction):
            direction = self.demandeDirection()

        # Une fois la position valide, on bouge le pion, ajoute les points, modifie la grille et change de joueur.
        self.positions = add(self.positions, directionAcceptable[direction])
        self.listeJoueurs[self.joueurCourant].augmenteScore(
            self.grilleJeu[self.positions])
        self.grilleJeu[self.positions] = None
        self.joueurCourant = (self.joueurCourant + 1) % 2

        return None

    def finPartie(self):
        """
        Permet de déterminer si la partie est finie ou non,
        c'est à dire s'il reste des directions acceptable avec des points à récupérer.
        :return: True si la partie est finie,
                 False sinon.
        """

        for direction in directionAcceptable.values():
            positionTestee = add(self.positions, direction)
            if positionTestee in self.grilleJeu and isinstance(
                    self.grilleJeu[positionTestee], int):
                return False
        return True

    def resultatPartie(self):
        """
        Affiche le résultat de la partie et renvoie le numéro du joueur vainqueur.
        :return: 1 ou 2 selon le joueur qui a gagné, None sinon.
        """

        scoreJoueur1 = self.listeJoueurs[0].getScore()
        scoreJoueur2 = self.listeJoueurs[1].getScore()
        if scoreJoueur1 > scoreJoueur2:
            print("Le joueur 1 a gagné ! Son score est de {} points contre {}".format(
                str(scoreJoueur1),
                str(scoreJoueur2)))
            return 1
        elif scoreJoueur1 == scoreJoueur2:
            print("Il y a une égalité ! Les deux joueurs ont {} points".format(
                str(scoreJoueur2)))
            return None
        else:
            print("Le joueur 2 a gagné ! Son score est de {} points contre {}".format(
                str(scoreJoueur2),
                str(scoreJoueur1)))
            return 2

    def affichage(self):
        """
        Affiche l'état actuel de la partie.
        :return: Rien
        """

        print("\n\n==============================================\n"
              "==============================================\n \n \n")

        self.grilleJeu.affichageGrille(self.positions)
        maxLength = max(len(self.listeJoueurs[i].getNom()) for i in {0, 1})
        self.listeJoueurs[0].afficheJoueur(maxLength)
        self.listeJoueurs[1].afficheJoueur(maxLength)

    def writeIntoCSV(self, nomFichier):
        self.grilleJeu.writeGridIntoCSV(nomFichier)


def gestionJeu():
    """
    Fonction principale du jeu.
    :return: Le numéro du vainqueur, ou rien en cas d'égalité.
             Affichage du score via la fonction resultatPartie() de Game
    """

    # Création de la partie
    nomJoueur1 = input("Joueur 1 : quel est votre nom ? \n")
    nomJoueur2 = input("Joueur 2 : quel est votre nom ? \n")

    # Importation d'une grille
    reponse = input("Souhaitez-vous importer une grille à partir d'un fichier csv ? y/N")

    if reponse.lower() == "y":
        print("Pas encore complétement implémenté")
        nomFichier = input("Quel fichier ? (nom sans extension)")
        nomFichier += ".csv"
        with open(nomFichier) as csvfile:
            fichier = pandas.read_csv(csvfile, delimiter=",", header=None)
            partie = Game(nomJoueur1, nomJoueur2, tableauValeurs=fichier)

        partie.affichage()


    # génération d'une partie avec grille aléatoire
    else:
        print("Choisissez la taille de la grille.")

        # On s'assure que les paramètres donnés sont corrects.
        while True:
            try:
                tailleDemandee = int(input())
                partie = Game(nomJoueur1, nomJoueur2, taille=tailleDemandee)
            except ValueError:
                print("Veuillez entrer un chiffre positif et impair.")
            else:
                break

        partie.affichage()

        # Possibilité d'exporter la grille générée aléatoirement
        reponse = input(
            "Souhaitez-vous exporter la grille générée sous forme d'un fichier csv ? y/N")

        if reponse.lower() == "y":
            nomFichier = input(
                "Quel nom souhaitez-vous donner au fichier ? (nom sans extension)")
            nomFichier += ".csv"
            partie.writeIntoCSV(nomFichier)

    # Boucle principale du jeu.
    while not partie.finPartie():
        partie.gestionTour()
        partie.affichage()

    return partie.resultatPartie()


gestionJeu()
