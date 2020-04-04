from tkinter import *
from random import *
from function import *
import time
import pickle


fenetre=Tk()


# Titre de la fenetre
fenetre.title('The Big Brick Shooter')
can=Canvas(fenetre,width=640,height=480,bg='black')
can.pack()

# fond d'ecran
fond=PhotoImage(file='fond.gif')
#bloc_joueur
bloc = PhotoImage(file="fusee.png")
# fond d'ecran
can.create_image(320,240,image=fond)
#bloc_joueur
bloc_tk= can.create_image(320, 430, image=bloc)


#fontion pour aller à gauche
def left(event):
    print('hey')
    can.move(bloc_tk,-20,0)

#fontion pour aller à droite 
def right(event):
    print('hey')
    can.move(bloc_tk,20,0)


#Touche fleche gauche pour aller à gauche
fenetre.bind('<Left>', left)
#Touche fleche droit pour aller à droit
fenetre.bind('<Right>',right)


fenetre.mainloop()