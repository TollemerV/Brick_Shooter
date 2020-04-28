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
fond = PhotoImage(file='fond.gif')
#bloc_joueur
bloc_joueur = PhotoImage(file="fusee.png")
#bloc ennemi 
bloc_ennemi = PhotoImage(file="ennemi.png")
#Projectile (tir) 
img_projectile = PhotoImage(file="projectile.png")

# fond d'ecran
can.create_image(320,240,image=fond)
#bloc_joueur
bloc_tk = can.create_image(320,430, image=bloc_joueur)

#projectile = can.create_image(320,350, image=img_projectile)

xennemi = 60
yennemi = 40
i=0
j=0
k=0
nombre_tir=0
xtir =0
ytir=0
l=0
horizon_tir = 320
projectile = []

#definition d'un bloc ennemi
def ennemi():
    global xennemi,yennemi,listexennemi,listeyennemi,k
    listebloc=[k]
    listexennemi=[k]
    listeyennemi=[k]
    listebloc.append(can.create_image(xennemi,yennemi,image=bloc_ennemi))
    #On décale de 60px bloc entre chaque blo! 
    xennemi = xennemi + 60
    k = k+1

# Ajouter une nouvelle ligne | On décale de 60 pixels vers la droite entre chaque bloc | On remet X à 60 quand on arrive au bout de la ligne ainsi que le compteur i
def ajouter_uneligne():
    global i,yennemi,xennemi
    while i<10 :
        ennemi()
        i=i+1
    yennemi = yennemi + 60
    xennemi = 60
    i=0


ajouter_uneligne()
ajouter_uneligne()

if nombre_tir==18 :
    ajouter_uneligne()
    nombre_tir = 0



#Fonction de destruction d'un bloc
def destruction_bloc ():
    global listexennemi,listeyennemi,l,xtir,ytir,listebloc
    
    while (l<len(listexennemi))and (l<len(listeyennemi)):
        if (xtir==listexennemi[l]) and (ytir==listeyennemi[l]) :
            listebloc = []
            can.delete(projectile)
            can.delete(listebloc[l])
        l = l+1
     

########################################################################
##################### VARIABLE #########################################
########################################################################

#limite cotés de la carte
limit = 0

vitesse_deplacement = 15
vitesse_defilement = 2
vitesse_tir = 5

affiche_deplacement = []
affiche_defilement = []
affiche_tir = []
########################################################################
##################### FENETRE BOUTIQUE #################################
########################################################################

'Button(fenetre,text="Deplacement +",font=("Fixedsys"),command=boutique_vitesse_deplacement).grid(row=2,column=2,sticky=N,padx=5)'
'Button(fenetre,text="Defilement + ",font=("Fixedsys"),command=boutique_vitesse_defilement).grid(row=3,column=2,sticky=N,padx=5)'
'Button(fenetre,text="Tir +",font=("Fixedsys"),command=boutique_vitesse_tir).grid(row=3,column=2,sticky=N,padx=5)'

def boutique_vitesse_deplacement(vitesse_deplacement):
    if vitesse_deplacement <40:
        vitesse_deplacement=vitesse_deplacement+5
#affiche_deplacement.append(can.create_text(vitesse_deplacement,font=('Fixedsys',8),text=str(vitesse_deplacement)+': Vitesse de Deplacement',fill='red'))

def boutique_vitesse_defilement(vitesse_defilement):
    if vitesse_deplacement <10 :
        vitesse_defilement=vitesse_defilement+5
#affiche_defilement.append(can.create_text(font=('Fixedsys',8),text=str(vitesse_defilement)+': Vitesse de Defilement',fill='red'))

def boutique_vitesse_tir(vitesse_tir):
    if vitesse_tir <20 :
        vitesse_tir=vitesse_tir +5
#affiche_tir.append(can.create_text(font=('Fixedsys',8),text=str(vitesse_tir)+': Vitesse de Tir',fill='red'))


########################################################################
##################### FENETRE JEU ######################################
########################################################################

#fontion pour aller à gauche
def left(event):
    global limit,horizon_tir
    if limit > -280 :
     limit = limit - vitesse_deplacement
     can.move(bloc_tk,-vitesse_deplacement,0)
     horizon_tir = horizon_tir - vitesse_deplacement


#fontion pour aller à droite 
def right(event):
    global limit,horizon_tir
    if limit < 280 :
        limit = limit + vitesse_deplacement
        can.move(bloc_tk,vitesse_deplacement,0)
        horizon_tir = horizon_tir + vitesse_deplacement

tir_unique = 1
lateral_tir = 350
compteur = 0

dx = 0
dy = -10
# NE PAS OUBLIER TIR_UNIQUE
projectile =[can.create_image(horizon_tir,lateral_tir, image=img_projectile)]
def tir():
    global tir_unique,lateral_tir,horizon_tir,projectile
    can.move(projectile,dx,dy)
    fenetre.after(20,tir)



   
'''
def déplacement_projo():
    global projectile,horizon_tir,lateral_tir,compteur,tir_unique
    if len(projectile)==1:
            #projectile = can.create_image(horizon_tir,lateral_tir, image=img_projectile)
            compteur = compteur + 1
            lateral_tir = lateral_tir - 20
            can.delete(projectile[0])
            can.move(projectile,0,-20)
            projectile =[can.create_image(horizon_tir,lateral_tir, image=img_projectile)]
            fenetre.after(20,déplacement_projo)
    compteur = 0
    lateral_tir = 350
'''

tir()
#Touche fleche gauche pour aller à gauche
fenetre.bind('<Left>', left)
#Touche fleche droit pour aller à droit
fenetre.bind('<Right>',right)

fenetre.bind('<space>',tir)



fenetre.mainloop()