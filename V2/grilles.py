import random
from fltk import *

def creation_grille_B():
    """
    Retourne un tableau en 2 dimensions pour les billes

    Returns:
        list
    """
    lst = []
    for _ in range(7):
        lst2 = []
        for _ in range(7):
            chance = random.randint(1, 8)
            if chance == 1:
                lst2.append(1)
            else:
                lst2.append(0)
        lst.append(lst2)
    return lst

def creation_grille_H():
    """
    Retourne un tableau en 2 dimensions pour les tirettes horizontaux

    Returns:
        list
    """
    lst = []
    for _ in range(7):
        lst2 = []
        for _ in range(7):
            chance = random.randint(1, 2)
            if chance == 1:
                lst2.append(0)
            else:
                lst2.append(1)
        lst.append(lst2)
    return lst

def creation_grille_V():
    """
    Retourne un tableau en 2 dimensions pour les tirettes verticaux

    Returns:
        list
    """
    lst = []
    for _ in range(7):
        lst2 = []
        for _ in range(7):
            chance = random.randint(1, 2)
            if chance == 1:
                lst2.append(0)
            else:
                lst2.append(2)
        lst.append(lst2)
    return lst

def affichage_grille(grille):
    """
    Affiche un tableau en 2 dimensions ligne par ligne

    Args:
        grille (list): tableaux en 2 dimensions représentant la grille de la couche de jeu
    """
    for x in grille:
        print(x)
    print("")

def deplacer_droite(grille, ligne):
    """
    Décale toutes les valeurs de la liste vers la droite de facon circulaire

    Args:
        grille (lst): La grille contenant la tirette qui va avoir ses valeurs décalé
        ligne (int): La tirette qui va avoir ses valeurs décalé
    """
    last_val = grille[ligne].pop()
    grille[ligne].insert(0, last_val)

def deplacer_gauche(grille, ligne):
    """
    Décale toutes les valeurs de la liste vers la gauche de facon circulaire

    Args:
        grille (lst): La grille contenant la tirette qui va avoir ses valeurs décalé
        ligne (int): La tirette qui va avoir ses valeurs décalé
    """
    first_val = grille[ligne].pop(0)
    grille[ligne].insert(len(grille[ligne]), first_val)

def deplacer_bas(grille, colonne):
    """
    Décale toutes les valeurs de la grille vers le bas de facon circulaire

    Args:
        grille (lst): La grille contenant la tirette qui va avoir ses valeurs décalé
        ligne (int): La tirette qui va avoir ses valeurs décalé
    """
    last_val = grille[len(grille) - 1][colonne]
    for x in range(len(grille) - 1, 0, -1):
        grille[x][colonne] = grille[x - 1][colonne]
    grille[0][colonne] = last_val

def deplacer_haut(grille, colonne):
    """
    Décale toutes les valeurs de la grille vers le haut de facon circulaire

    Args:
        grille (lst): La grille contenant la tirette qui va avoir ses valeurs décalé
        ligne (int): La tirette qui va avoir ses valeurs décalé
    """
    first_val = grille[0][colonne]
    for x in range(len(grille) - 1):
        grille[x][colonne] = grille[x + 1][colonne]
    grille[len(grille)- 1][colonne] = first_val


def affichage_grille(grille):
    """
    Affiche un tableau en 2 dimensions ligne par ligne

    Args:
        grille (list): tableaux en 2 dimensions représentant la grille de la couche de jeu
    """
    for x in grille:
        print(x)
    print("")

def comparaison(PL,TV,TH):
    """
    Fonction inutilisé ?
    """
    for y in range(len(PL)):
        for x in range(len(PL)):
            if TV[y][x] == True and TH[y][x] == True:
                PL[y][x] = True

def fusion(TV, TH):
    """
    Fusionne la couche des tirettes verticales et horizontales pour ne former qu'un tableau en 2 dimensions qui sera affiché au joueur

    Args:
        TV (list): tableaux en 2 dimensions représentant les tirettes verticaux
        TH (list): tableaux en 2 dimensions représentant les tirettes horizontaux

    Returns:
        list: Tableau en 2 dimensions représentant les 2 couches de jeu
    """
    LstVide = []
    for y in range(len(TV)):
        LstVide2 = []
        for x in range(len(TV)):
            LstVide2.append(TV[y][x] + TH[y][x])
        LstVide.append(LstVide2)
    return LstVide

def poser_bille(PB,x,y):
    PB[y][x] = True

def gerer_evenement(B,V,H,x,y, coord_min_x, coord_min_y, coord_max_x, coord_max_y, taille_case, taille_bouton, hitbox_b):
    if x > coord_min_x + taille_case  and x < coord_max_x and y > coord_min_y + taille_case and y < coord_max_y:
        X = int((x - coord_min_x) // taille_case) - 1
        Y = int((y - coord_min_y) // taille_case) - 1
        poser_bille(B, X, Y)
    elif x > coord_min_x and x < coord_min_x + taille_case and y > coord_min_y and y < coord_max_y:
        Y = int((y - coord_min_y) // taille_case) - 1
        if Y in range(len((B)[0])):
            deplacer_droite(H, Y)
    elif x > coord_max_x and x < coord_max_x + taille_bouton * hitbox_b  and y > coord_min_y and y < coord_max_y:
        Y = int((y - coord_min_y) // taille_case) - 1
        if Y in range(len((B)[0])):
            deplacer_gauche(H, Y)
    elif x > coord_min_x + taille_case and x < coord_max_x  and y < coord_min_y + taille_case and y > coord_min_y - taille_bouton * hitbox_b :
        X = int((x - coord_min_x) // taille_case) - 1
        if X in range(len(B)):
            deplacer_bas(V, X)
    elif x > coord_min_x + taille_case and x < coord_max_x and y > coord_max_y and y < coord_max_y + taille_bouton * hitbox_b :
        X = int((x - coord_min_x) // taille_case) - 1
        if X in range(len(B)):
            deplacer_haut(V, X)

def calcul_coord(taille_case, taille_plateau):
    coord_min_x = largeur_fenetre() / 2 - (taille_plateau /2 * taille_case) - taille_case
    coord_max_x = (coord_min_x + taille_case) + (taille_case * taille_plateau)
    coord_min_y = hauteur_fenetre() / 2 - (taille_plateau/2 * taille_case) - taille_case
    coord_max_y = (coord_min_y + taille_case) + (taille_case * taille_plateau)
    return coord_min_x, coord_max_x, coord_min_y, coord_max_y