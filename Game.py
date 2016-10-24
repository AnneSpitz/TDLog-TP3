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


from Grid import *
from Player import *
from random import choice

# Différentes combinaisons de touches possibles pour les contrôles, permet de choisir ses
# touches de contrôle
tab_direction_acceptable = [{"8": [0, -1], "4": [-1, 0], "2": [0, 1], "6": [1, 0],
                             "7": [-1, -1], "9": [1, -1], "1": [-1, 1], "3": [1, 1]},
                            {"z": [0, -1], "q": [-1, 0], "x": [0, 1], "d": [1, 0],
                             "a": [-1, -1], "e": [1, -1], "w": [-1, 1], "c": [1, 1]}]

commandes_choisies = 1

direction_acceptable = tab_direction_acceptable[commandes_choisies]


def add(x, y):
    """
    Permet d'additionner terme à terme deux couples ou deux tableaux
    :param x, y: couples ou tableaux à additionner terme à terme
    :return: tableau des résultats
    """

    assert (len(x) == len(y))
    return [x[i] + y[i] for i in range(len(x))]


class Game:
    def __init__(self, taille, joueur_1, joueur_2):
        """
        Constructeur.
        :param taille: Taille de la grille
        :param joueur_1: Nom du premier joueur
        :param joueur_2: Nom du deuxième joueur
        """

        self.joueur_courant = 0

        assert (isinstance(taille, int))
        self.grille_jeu = Grid(taille)
        for x in range(taille):
            for y in range(taille):
                self.grille_jeu[(x, y)] = choice(point)
        self.grille_jeu[
            (taille // 2, taille // 2)] = None  # La position initiale est mise à 0 : elle est déjà explorée.
        self.liste_joueurs = [Player(joueur_1), Player(joueur_2)]

        self.positions = [taille // 2, taille // 2]

    def demande_direction(self):
        """
        Demande à l'utilisateur de rentrer une touche du clavier.
        :return: une string correspondant à la touche demandée.
        """

        return input(
            "À {0} de jouer. \n "
            "Appuyez sur une touche parmi : "
            "{1}; {2}; {3}; {4}; {5}; {6}; {7}; {8}. Choisissez une case non vide.".format(
                self.liste_joueurs[self.joueur_courant].get_nom(),
                *direction_acceptable.keys()))

    def is_direction_non_valide(self, direction):
        """
        teste si la direction demandée est incompatible ou si on peut continuer
        :return: False si la direction est correcte et qu'on peut continuer
                 True si la direction n'est pas correcte et qu'il faut redemander
        """
        print(self.positions)
        print(direction)


        if direction not in direction_acceptable.keys():
            print("pas valide")
            return True
        else:
            position_voulue = add(self.positions, direction_acceptable[direction])
            print(position_voulue)
            if position_voulue not in self.grille_jeu:
                print("TEST TA GUEULE")
                return True
            elif not isinstance(self.grille_jeu[position_voulue], int):
                return True
            else:
                return False

    def gestion_tour(self):
        """
        Permet de jouer pour le joueur courant, puis passe la main.
        :param direction: direction dans laquel le joueur veut se déplacer.
        :return: Rien
        """

        direction = self.demande_direction()

        # On demande la direction tant que celle-ci n'est pas valide.
        while self.is_direction_non_valide(direction):
            direction = self.demande_direction()

        # Une fois la position valide, on bouge le pion, ajoute les points, modifie la grille et change de joueur.
        self.positions = add(self.positions, direction_acceptable[direction])
        self.liste_joueurs[self.joueur_courant].augmente_score(
            self.grille_jeu[self.positions])
        self.grille_jeu[self.positions] = None
        self.joueur_courant = (self.joueur_courant + 1) % 2

        return None

    def fin_partie(self):
        """
        Permet de déterminer si la partie est finie ou non,
        c'est à dire s'il reste des directions acceptable avec des points à récupérer.
        :return: True si la partie est finie,
                 False sinon.
        """

        for direction in direction_acceptable.values():
            position_testee = add(self.positions, direction)
            if position_testee in self.grille_jeu and isinstance(
                    self.grille_jeu[position_testee], int):
                return False
        return True

    def resultat_partie(self):
        """
        Affiche le résultat de la partie et renvoie le numéro du joueur vainqueur.
        :return: 1 ou 2 selon le joueur qui a gagné, None sinon.
        """

        score_joueur_1 = self.liste_joueurs[0].get_score()
        score_joueur_2 = self.liste_joueurs[1].get_score()
        if score_joueur_1 > score_joueur_2:
            print("Le joueur 1 a gagné ! Son score est de {} points contre {}".format(
                str(score_joueur_1),
                str(score_joueur_2)))
            return 1
        elif score_joueur_1 == score_joueur_2:
            print("Il y a une égalité ! Les deux joueurs ont {} points".format(
                str(score_joueur_2)))
            return None
        else:
            print("Le joueur 2 a gagné ! Son score est de {} points contre {}".format(
                str(score_joueur_2),
                str(score_joueur_1)))
            return 2

    def affichage(self):
        """
        Affiche l'état actuel de la partie.
        :return: Rien
        """

        print("\n\n==============================================\n"
              "==============================================\n \n \n")

        self.grille_jeu.affichage_grille(self.positions)
        max_length = max(len(self.liste_joueurs[i].get_nom()) for i in {0, 1})
        self.liste_joueurs[0].affiche_joueur(max_length)
        self.liste_joueurs[1].affiche_joueur(max_length)


def gestion_jeu():
    """
    Fonction principale du jeu.
    :return: Le numéro du vainqueur, ou rien en cas d'égalité.
             Affichage du score via la fonction resultat_partie() de Game
    """

    # Création de la partie
    nom_joueur_1 = input("Joueur 1 : quel est votre nom ? \n")
    nom_joueur_2 = input("Joueur 2 : quel est votre nom ? \n")

    print("Choisissez la taille de la grille.")

    # On s'assure que les paramètres donnés sont corrects.
    while True:
        try:
            taille = int(input())
            partie = Game(taille, nom_joueur_1, nom_joueur_2)
        except ValueError:
            print("Veuillez entrer un chiffre positif et impair.")
        else:
            break

    partie.affichage()

    # Boucle principale du jeu.
    while not partie.fin_partie():
        partie.gestion_tour()
        partie.affichage()

    return partie.resultat_partie()


gestion_jeu()
