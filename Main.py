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

import IA
import Game
import pandas


def creationPartie(nombreJoueur):
    """

    :return:
    """

    # Création de la partie


    # Demande des noms, pour 1 ou 2 joueurs.
    if nombreJoueur == "1":
        nomJoueur1 = input("Comment vous appellez-vous ? \n")
        nomJoueur2 = "GLaDOS"
    else:
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
            partie = Game.Game(nomJoueur1, nomJoueur2, tableauValeurs=fichier)

        partie.affichage()


    # génération d'une partie avec grille aléatoire
    else:
        print("Choisissez la taille de la grille.")

        # On s'assure que les paramètres donnés sont corrects.
        while True:
            try:
                tailleDemandee = int(input())
                partie = Game.Game(nomJoueur1, nomJoueur2, taille=tailleDemandee)
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

    return (partie)


def gestionJeu2Humains(partie):
    """
    Fonction principale du jeu.
    :return: Le numéro du vainqueur, ou rien en cas d'égalité.
             Affichage du score via la fonction resultatPartie() de Game
    """

    # Boucle principale du jeu.
    while not partie.finPartie():
        partie.gestionTourHumain()
        partie.affichage()

    return partie.resultatPartie()


def gestionJeu1Humain(partie):
    """

    :param partie:
    :return:
    """
    while not partie.finPartie():
        if partie.joueurCourant == 0:
            partie.gestionTourHumain()
        else:
            print("GLaDOS réflechie... \n")
            IA.gestionTourIA(partie)
        partie.affichage()

    return partie.resultatPartie()


nombreJoueur = 0
while nombreJoueur not in {"1", "2"}:
    nombreJoueur = input("Combien de joueur ? 1/2")

partie = creationPartie(nombreJoueur)

if nombreJoueur == "2":
    gestionJeu2Humains(partie)

else:
    gestionJeu1Humain(partie)
