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

(debutJeu, score) = InitVarEnv()

# D�finition du canevas ( Ecran de jeu )

gameC=Canvas(fenetre,width=640,height=480,bg='black')

# On affiche l'écran de présentation du jeu
affichageScore=Label(fenetre,font=('Fixedsys',16))

affichageScore.grid(row=0,column=0,sticky=W)


debutJeu = EcranDePresentation(affichageScore, gameC, fenetre, debutJeu)

# On met le gestionnaire d'évènements en route

afficherGlobal(debutJeu, score)

fenetre.mainloop()

