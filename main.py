from tkinter import Tk, Button, PhotoImage, Canvas, Label,N, W, E, ALL
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

# D�finition du canevas ( Ecran de jeu )

canvas=Canvas(fenetre,width=640,height=480,bg='black')

# Définition des touches qui vont permettre
# de diriger le canon mobile



# On affiche l'écran de présentation du jeu

EcranDePresentation(afficherScore, canvas, fenetre)

# On met le gestionnaire d'évènements en route

fenetre.mainloop()

