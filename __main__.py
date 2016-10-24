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


def demandeJoueurs():
    """
    Demande le nombre de joueur et leur noms.
    :return: une list contenant le nombre de joueur, et leur noms.
    """

    nombreJoueur = 0

    # On demande un nombre de joueur entre 1 et 2.
    while nombreJoueur not in {"1", "2"}:
        nombreJoueur = input("Partie à combien de joueurs ? 1/2")

    if nombreJoueur == "1":
        nomJoueur1 = input("Comment vous appellez-vous ?")
        nomJoueur2 = "GLaDOS"  # Nom par défaut de l'IA.

    else:
        nomJoueur1 = input("Nom du joueur 1 :")
        nomJoueur2 = input("Nom du joueur 2 :")

    return [nombreJoueur, nomJoueur1, nomJoueur2]


def creationOuImportationPartie(nomJoueur1, nomJoueur2):
    """
    Cette fonction crée la partie. Soit de manière aléatoire, soit en lisant un fichier,
    à la demande des joueurs. De plus, elle affiche l'état initiale de la partie et si la partie
    est aléatoire, demande au joueur s'il veut l'enregistrer.
    :param nomJoueur1: (str) Nom du joueur 1.
    :param nomJoueur2: (str) Nom du joueur 2.
    :return: Renvoie la partie (Game).
    """

    # On demande si on charge une partie depuis un fichier.
    reponse = input("Souhaitez-vous importer une grille à partir d'un fichier csv ? y/N")

    if reponse.lower() == "y":
        print("Pas encore complétement implémenté")
        nomFichier = input("Quel fichier ? (nom sans extension)")
        nomFichier += ".csv"
        with open(nomFichier) as csvfile:

            fichier = pandas.read_csv(csvfile, delimiter=",", header=None)
            partie = Game.Game(nomJoueur1, nomJoueur2, tableauValeurs=fichier)

        partie.affichage()

    # Génération d'une partie avec grille aléatoire si on ne lit pas de fichier.
    else:
        print("Choisissez la taille de la grille.")

        # On s'assure que les paramètres donnés sont corrects :
        while True:
            try:
                tailleDemandee = int(input())
                partie = Game.Game(nomJoueur1, nomJoueur2, taille=tailleDemandee)

            except ValueError:
                print("Veuillez entrer un chiffre positif et impair.")

            else:
                break

        partie.affichage()

        # Possibilité d'exporter la grille générée aléatoirement :
        reponse = input(
            "Souhaitez-vous exporter la grille générée sous forme d'un fichier csv ? y/N")

        if reponse.lower() == "y":
            nomFichier = input(
                "Quel nom souhaitez-vous donner au fichier ? (nom sans extension)")
            nomFichier += ".csv"
            partie.writeIntoCSV(nomFichier)

    print("Que la partie commence !\n")

    return partie


def gestionTour(partie, isIAPresente):
    """
    Va cherche la direction auprès du joueur (en demandant aux humains et en appelant
    choixDirectionIA pour l'IA). Puis modifie l'état de la partie.
    :param partie: (Game) Partie sur laquelle on travaille.
    :param isIAPresente: (bool) True s'il y a une IA dans la partie.
    :return: Rien.
    """

    # S'il y a une IA, et que c'est à elle de jouer, on appelle la choixDirectionIA.
    if isIAPresente and partie.joueurCourant == 1:
        print(" refléchit...".format(partie.listeJoueurs[1].getNom()))
        direction = IA.choixDirectionIA(partie)

    else:
        direction = partie.demandeDirection()
        # On demande la direction tant que celle-ci n'est pas valide.
        while partie.isDirectionNonValide(direction):
            direction = partie.demandeDirection()

    # Une fois qu'on a la direction on modifie l'état.
    partie.modifieEtat(direction)

    return None


def gestionJeu(partie, isIAPresente):
    """
    Va appeller gestionTour tant que la partie n'est pas finie, puis afficher le résultat via
    resultatPartie.
    :param partie: (Game) Partie sur laquelle on travaille.
    :param isIAPresente: (bool) True s'il y a une IA dans la partie.
    :return: Renvoie le return de resultatPartie.
    """

    while not partie.finPartie():
        gestionTour(partie, isIAPresente)
        partie.affichage()

    return partie.resultatPartie()


# /////////////////////////////////////////////////////////////////////////////////////////////////
# Corps du programme :


informationJoueurs = demandeJoueurs()

partie = creationOuImportationPartie(informationJoueurs[1], informationJoueurs[2])

if informationJoueurs[0] == "1":
    isIAPresente = True
else:
    isIAPresente = False

gestionJeu(partie, isIAPresente)
