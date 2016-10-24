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
import customExceptions


def demandeJoueurs():
    """

    :return:
    """
    nombreJoueur = 0

    while nombreJoueur not in {"1", "2"}:
        nombreJoueur = input("Partie à combien de joueurs ? 1/2 \n")

    if nombreJoueur == "1":
        nomJoueur1 = input("Comment vous appellez-vous ? \n")
        nomJoueur2 = "GLaDOS"
    else:
        nomJoueur1 = input("Nom du joueur 1 : \n")
        nomJoueur2 = input("Nom du joueur 2 : \n")

    return [nombreJoueur, nomJoueur1, nomJoueur2]


def creationOuImportationPartie(nomJoueur1, nomJoueur2):
    """

    :param nomJoueur1:
    :param nomJoueur2:
    :return:
    """
    #
    reponse = input("Souhaitez-vous importer une grille à partir d'un fichier csv ? y/N \n")

    if reponse.lower() == "y":
        nomFichier = input("Quel fichier ? (nom sans extension) \n")
        nomFichier += ".csv"
        with open(nomFichier) as csvfile:
            fichier = pandas.read_csv(csvfile, delimiter=",", header=None)
            partie = Game.Game(nomJoueur1, nomJoueur2, tableauValeurs=fichier)


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
            except customExceptions.TailleNegativeError:
                print("Vous avez entré une taille négative. Veuillez entrer un chiffre positif et impair.")
            except customExceptions.TaillePaireError:
                print("Vous avez entré une taille paire. Veuillez entrer un chiffre positif et impair.")
            else:
                break

        partie.affichage()

        # Possibilité d'exporter la grille générée aléatoirement
        print("==============================================\n"
              "==============================================\n")
        reponse = input(
            "Souhaitez-vous exporter la grille générée sous forme d'un fichier csv ? y/N \n")

        if reponse.lower() == "y":
            nomFichier = input(
                "Quel nom souhaitez-vous donner au fichier ? (nom sans extension) \n")
            nomFichier += ".csv"
            partie.writeIntoCSV(nomFichier)

        print("==============================================\n"
              "==============================================")

    print("Que la partie commence !\n")

    partie.affichage()

    return partie


def gestionTour(partie, isIAPresente):
    """
    Permet de jouer pour le joueur courant, puis passe la main.
    :param direction: direction dans laquel le joueur veut se déplacer.
    :return: Rien
    """
    if isIAPresente and partie.joueurCourant == 1:
        direction = IA.choixDirectionIA(partie)
        print(" refléchit...".format(partie.listeJoueurs[1].getNom()))
    else:
        direction = partie.demandeDirection()
        # On demande la direction tant que celle-ci n'est pas valide.
        while partie.isDirectionNonValide(direction):
            direction = partie.demandeDirection()

    # Une fois la position valide, on bouge le pion, ajoute les points, modifie la grille et change de joueur.
    partie.modifiePostion(direction)

    return None


def gestionJeu(partie, isIAPresente):
    """

    :param isIAPresente:
    :return:
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
