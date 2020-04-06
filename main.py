from tkinter import Tk, Button, PhotoImage, Canvas, Label, N, W, E, ALL
from random import *
import time
import pickle
from function import *

#######################
#                     #
# Programme principal #
#                     #
#######################

# Création de la fenêtre principale

fenetre=Tk()

# Titre de la fenêtre

fenetre.title('Space invaders')

InitVarEnv()

# D�finition du canevas ( Ecran de jeu )

gameC=Canvas(fenetre,width=640,height=480,bg='black')

# On affiche l'écran de présentation du jeu
afficherGlobal()

EcranDePresentation(score, gameC, fenetre, debutJeu)

# On met le gestionnaire d'évènements en route

fenetre.mainloop()

