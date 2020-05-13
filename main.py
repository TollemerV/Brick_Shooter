from tkinter import *
from random import *
from function import *
import time
import pickle
import tkinter as tk
import random


fenetre=Tk()
can=Canvas(fenetre,width=640,height=480,bg='black')
fenetre.title('The Big Brick Shooter')

# fond d'ecran
fond = PhotoImage(file='fond.gif')
# fond d'ecran
can.create_image(320,240,image=fond)

nouveau_vaisseau=0
# Titre de la fenetre
def new_game():
    global bloc_joueur,bloc_ennemi,img_projectile,xennemi,yennemi,i,j,k,nombre_tir,xtir,ytir,l,horizon_tir,bloc_tk,projectile,bloc_coin,coin

    can.pack()

    coin = PhotoImage(file="coin.png")
    #bloc ennemi 
    bloc_ennemi = PhotoImage(file="ennemi.png")
    #Projectile (tir) 
    img_projectile = PhotoImage(file="projectile.png")
    

    if nouveau_vaisseau == 0 :
        #bloc_joueur
        bloc_joueur = PhotoImage(file="fusee.png")
        #bloc_joueur
        bloc_tk = can.create_image(320,430, image=bloc_joueur)

    #projectile = can.create_image(320,350, image=img_projectile)
    bloc_coin = can.create_image(625,459, image=coin)
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
    
    Bouton_Vitesse= Button(fenetre, text ='Vitesse +', command = vitesse_plus)
    #On ajoute l'affichage du bouton dans la fenêtre tk:
    Bouton_Vitesse.pack(side = LEFT, padx = 10, pady = 5)

    Bouton_Tir = Button(fenetre, text ='Vitesse Tir +', command = vitesse_tir)
    Bouton_Tir.pack(side = LEFT, padx = 10, pady = 5)

    BoutonQuitter = Button(fenetre, text ='Quitter', command = Quitter)
    BoutonQuitter.pack(side = RIGHT, padx = 10, pady = 5)

    
    asteroide()


########################################################################
##################### ENNEMIS #########################################
########################################################################
'''
#definition d'un bloc ennemi
def ennemi():
    global xennemi,yennemi,listexennemi,listeyennemi,k
    listebloc=[k]
    listexennemi=[k]
    listeyennemi=[k]
    listebloc.append(can.create_image(xennemi,yennemi,image=bloc_ennemi))
    #On décale de 60px bloc entre chaque bloc ! 
    xennemi = xennemi + 60
    k = k+1

# Ajouter une nouvelle ligne | On décale de 60 pixels vers la droite entre chaque bloc | On remet X à 60 quand on arrive au bout de la ligne ainsi que le compteur i

def ajouter_uneligne():
    global i,yennemi,xennemi
    while i<20 :
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
     
'''
compteur_ennemi = 0
asteroide_unique = 1
ax = 0
ay = 2
lateral_asteroide = 0
horizon_asteroide = 320
limite_asteroide = 180
a=0
def asteroide():
    global asteroide, asteroide_unique,lateral_asteroide,horizon_asteroide,compteur_tour_ast
    if asteroide_unique == 1 :
        asteroide.append =[can.create_image(horizon_asteroide,lateral_asteroide, image=bloc_ennemi)]
        asteroide_unique = 0
        compteur_tour_ast = 0
        asteroide_anim()

compteur_dizaine = 0
compteur_tour_ast = 0
# can.move fait bouger l'asteroide projectile de ax en horizontal et ay en vertical
def asteroide_anim():
    global asteroide_unique,lateral_asteroide,horizon_asteroide,asteroide,compteur_ennemi,compteur_tour_ast,compteur_dizaine
    if compteur_ennemi < limite_asteroide :
        compteur_ennemi = compteur_ennemi + 1
        can.move(asteroide.append,ax,ay)
        fenetre.after(10,asteroide_anim) 
        compteur_dizaine = compteur_dizaine + 1
        if compteur_dizaine == 5 : 
            compteur_tour_ast=compteur_tour_ast + 1
            compteur_dizaine = 0
         #Le compteur dizaine permet de mettre +1  tout les 5 avancement car l'asteroide avance de 2 en 2 donc il lui faut 5 coup pour avancer de 5 en 5 , il comte 1 pour chaque dzaine   
    else:
        asteroide_unique=1
        compteur_ennemi=0
        Spawn = random.randint(1, 11) 
        print("Spwan =  % s" % (Spawn))
        if Spawn == 1 :
            horizon_asteroide = 40
            asteroide()
        if Spawn == 2 :
            horizon_asteroide = 80
            asteroide()
        if Spawn == 3 :
            horizon_asteroide = 140
            asteroide()
        if Spawn == 4 :
            horizon_asteroide = 200
            asteroide()
        if Spawn == 5 :
            horizon_asteroide = 260
            asteroide()
        if Spawn == 6 :
            horizon_asteroide = 320
            asteroide()
        if Spawn == 7 :
            horizon_asteroide = 380
            asteroide()
        if Spawn == 8 :
            horizon_asteroide = 440
            asteroide()
        if Spawn == 9 :
            horizon_asteroide = 500
            asteroide()
        if Spawn == 10 :
            horizon_asteroide = 560
            asteroide()
        if Spawn == 11 :
            horizon_asteroide = 600
            asteroide()



########################################################################
##################### VARIABLE #########################################
########################################################################

#limite cotés de la carte
limit = 0

vitesse_deplacement = 10

########################################################################
######################## SCORE ##################################
########################################################################
Score = 0
def incrémentation_score():  
    points = infos['valeur']
    points += 50
    infos['valeur'] = points   
    can.itemconfig(texte, text=str(points)) # création du nouveau texte
infos = {'valeur': Score, }
texte = can.create_text((50, 460), text=Score,font="Arial 24 italic", fill="white")  


########################################################################
##################### FENETRE JEU ######################################
########################################################################
position_actuelle = 320
#fontion pour aller à gauche
def left(event):
    global limit,horizon_tir,position_actuelle
    if limit > -280 :
     limit = limit - vitesse_deplacement
     position_actuelle = position_actuelle - vitesse_deplacement
     can.move(bloc_tk,-vitesse_deplacement,0)
     horizon_tir = horizon_tir - vitesse_deplacement


#fontion pour aller à droite 
def right(event):
    global limit,horizon_tir,position_actuelle
    if limit < 280 :
        limit = limit + vitesse_deplacement
        position_actuelle = position_actuelle + vitesse_deplacement
        can.move(bloc_tk,vitesse_deplacement,0)
        horizon_tir = horizon_tir + vitesse_deplacement
        


########################################################################
######################## TIR ##################################
########################################################################

#tir unique permet de tirer un projectile
tir_unique = 1
# placement verticale du départ des projectiles
lateral_tir = 380

#projectile déplacement horizontal (ne pas toucher)
dx = 0
# dy : vitesse du projectile , plus il tend vers moins l'infinie plus il est rapide
dy = -10
#compteur du nombre d'animation tir
compteur_tir = 0
# compte le nombre de projectile pour ajouter une ligne
ligne_en_plus = 0
# Limite du projectile en haut de l'ecran
limite_projectile = 40

# compteur tir = permet de compter le nombre de fois que tir_anim est lancer !
# Au bout de 40 fois le projectile, arrive au bout de l'ecran et on sort de la boucle compteur_tir , elle se remet à 0 pour le prochain tir
# tir unique permet de limiter le nombre de projectile sur l'écran à un seul
#Lorsque nous tirons X projectile , une nouvelle ligne s'ajoute
compteur_avancement_tir = 38 
def tir(event):
    global projectile, tir_unique, ligne_en_plus
    if tir_unique == 1 :
        projectile =[can.create_image(horizon_tir,lateral_tir, image=img_projectile)]
        tir_unique = 0
        ligne_en_plus = ligne_en_plus + 1
        tir_anim()
        #Incrémentation du Score
        incrémentation_score()
        incrémentation_gold()
        # Si on a titrer 8 fois , une ligne d'ennemis s'ajoute
        if ligne_en_plus == 8:
             '''ajouter_uneligne()'''
             ligne_en_plus = 0
 
# After , permet d'attendre 20 millisecondes avant de lancer rappeler la fonction tiranim()
# can.move fait bouger le projectile de dx en horizontal et dy en vertical
def tir_anim():
    global tir_unique,lateral_tir,horizon_tir,projectile,compteur_tir,compteur_avancement_tir,compteur_avancement_tir,compteur_tour_ast
    if compteur_tir < limite_projectile :
        compteur_tir = compteur_tir + 1
        can.move(projectile,dx,dy)
        compteur_avancement_tir = compteur_avancement_tir - 1
        fenetre.after(20,tir_anim)
        destroy()
    else:
        tir_unique=1
        compteur_tir=0
        compteur_avancement_tir = 38 

########################################################################
##################### DESTRUCTION BLOC #########################################
########################################################################
'''
# PARTIE ASTEROIDE
 if compteur_dizaine == 5 : 
            compteur_tour_ast=compteur_tour_ast + 1
            compteur_dizaine = 0
         #Le compteur dizaine permet de mettre +1  tout les 5 avancement car l'asteroide avance de 2 en 2 donc il lui faut 5 coup pour avancer de 5 en 5 , il comte 1 pour chaque dzaine   
#/////////////////////////////////
#PARTIE TIR

compteur_avancement_tir = 38 
#
compteur_avancement_tir = compteur_avancement_tir - 1
#/////////////////////////////////

# PARTIE COMMUNE
if compteur_tour_ast == compteur_avancement_tir:    #and horizon_asteroide == horizon_tir:
    #destroy
    print(" DESTROY ")
'''
'''
if (horizon_asteroide == horizon_tir) and (lateral_tir==lateral_asteroide) : 
    can.delete("asteroide")
    print("test")
      '''
def destroy():
        '''print(compteur_tour_ast)
        print(compteur_avancement_tir)'''
        if compteur_tour_ast == compteur_avancement_tir:    #and horizon_asteroide == horizon_tir:
         print(" DESTROY ")

########################################################################
##################### BOUTIQUE ######################################
########################################################################
prix_vitesse = 1000
prix_tir = 1000
nombre_amélioration_vitesse = 0



def vitesse_plus():
    global gold,prix_vitesse,vitesse_deplacement,nombre_amélioration_vitesse,bloc_joueur,bloc_tk,nouveau_vaisseau
    #SI nous avons plus de gold ou autant que le prix de l'augmentation vitesse alors :
    if gold >= prix_vitesse :
        # La vitesse est augmenté
        vitesse_deplacement=vitesse_deplacement+10
        # Le prix est enlevé de nos gold
        gold = gold - prix_vitesse 
        décrementation_gold_vitesse()
        # Le prix de le vitesse double pour le prochain achat
        prix_vitesse=prix_vitesse*2
        # On affiche dans la console notre nouveaux solde de gold et le nouveau rix de la vitesse
        print("Gold : ",gold)
        print ("Prix Vitesse + : ",prix_vitesse)
        print ("Vitesse augmenté ")
        print("")
        nombre_amélioration_vitesse = nombre_amélioration_vitesse + 1
    else:
        print(" PAS ASSEZ DE GOLD ! ")
    if nombre_amélioration_vitesse == 3 :
        bloc_joueur = PhotoImage(file="spaceship.png")
        bloc_tk = can.create_image(position_actuelle,430, image=bloc_joueur)
        nouveau_vaisseau = 1
        
def vitesse_tir():
    global gold,prix_tir,dy,limite_projectile
    #SI nous avons plus de gold ou autant que le prix de l'augmentation vitesse de tir alors :
    if gold >= prix_tir :
        # La vitesse de tir  est augmenté
        dy= dy - 5
        limite_projectile = limite_projectile - 5
        # Le prix est enlevé de nos gold
        gold = gold - prix_tir
        décrementation_gold_vitesse_tir()
        # Le prix de le vitesse double pour le prochain achat
        prix_tir=prix_tir*2
        # On affiche dans la console notre nouveaux solde de gold et le nouveau rix de la vitesse
        print("Gold : ",gold)
        print ("Prix Vitesse + : ",prix_tir)
        print ("Vitesse de tir augmenté ")
        print("")
    else:
        print(" PAS ASSEZ DE GOLD ! ")
#################################################
##########   AFFICHAGE GOLD    ###################
#################################################

#gold = 10000 # FAIRE RECUPERATION DE FICHIER 
mesgolds="gold.txt"
Goldus=open(mesgolds,'r')
Goldi=Goldus.read()
Goldus.close()
print(Goldi)
gold = int(Goldi)

def incrémentation_gold():  
    global gold
    gold = gold3['value']
    gold += 10
    gold3['value'] = gold
    can.itemconfig(text, text=str(gold)) # création du nouveau texte
    

def décrementation_gold_vitesse():
    global gold,prix_vitesse
    gold = gold3['value']
    gold = gold - prix_vitesse
    gold3['value'] = gold
    can.itemconfig(text, text=str(gold)) # création du nouveau texte

def décrementation_gold_vitesse_tir():
    global gold,prix_tir
    gold = gold3['value']
    gold = gold - prix_tir
    gold3['value'] = gold
    can.itemconfig(text, text=str(gold)) # création du nouveau texte

gold3 = {'value': gold, }
text = can.create_text((580, 460), text=gold,font="Arial 16 italic", fill="white") 

########################################################################
##################### MENU ######################################
########################################################################
class MenuOptions(Frame):
        def __init__(self, master):
                super().__init__()

                # INITIALISATION DES VARIABLES
                master = fenetre
                # Créations des widgets
                
                self.message = Label(self, text="SPACE INVADER")
                self.message.pack(side="top", fill=X)


                self.btn_jouer = Button(self, text="Jouer", command=self.call_play)
                self.btn_jouer.pack(padx = 150, pady = 20)

                self.btn_instruc = Button(self, text="Instruction", command=self.call_instruct)
                self.btn_instruc.pack(padx = 150, pady = 20)

                self.btn_equip = Button(self, text="Equipements", command=self.call_equipment)
                self.btn_equip.pack(padx = 150, pady = 20)

                self.btn_quitter = Button(self, text="Quitter",cursor="pirate", command=self.master.quit)
                self.btn_quitter.pack(padx = 150, pady = 20)


        # méthode d'appel de la page de jeu
        
        def call_play(self):
                self.destroy()  # On détruit la frame en cour 
                page_jeu = Jeu(self.master)  # et on créé la nouvelle
                new_game()  # ON COMMENCE LA PARTIE
                page_jeu.pack()

        # méthode d'appel de la page d'instruction

        def call_instruct(self):
                self.destroy()
                page_instruction = Instructions(self.master)
                page_instruction.pack()

        # méthode d'appel de la page d'équipement

        def call_equipment(self):
                self.destroy()
                page_equipement = Equipements(self.master)
                page_equipement.pack()
    

class Jeu(Frame):
    def __init__(self,master):
        super().__init__()
        # INITIALISATION DES VARIABLES
        master = fenetre
        '''
        btn_retour = Button(self, text="Retour", command=self.call_menu)
        btn_retour.pack()'''

    
    # méthode d'appel de page menu

    def call_menu(self):
        self.destroy()
        page_menu = MenuOptions(self.master)
        page_menu.pack()

 

class Equipements(Frame):
    def __init__(self,master):
        super().__init__()
        # INITIALISATION DES VARIABLES
        master = fenetre
        # Créations des widgets
        Bouton_Vitesse= Button(self, text ='Vitesse +', command = vitesse_plus)
        #On ajoute l'affichage du bouton dans la fenêtre tk:
        Bouton_Vitesse.pack( padx = 150, pady = 20)
        Bouton_Tir = Button(self, text ='Vitesse Tir +', command = vitesse_tir)
        Bouton_Tir.pack( padx = 150, pady = 20)
        btn_retour = Button(self, text="Retour", command=self.call_menu)

        btn_retour.pack()
        
    # méthode d'appel de page menu
        
    def call_menu(self):
        self.destroy()
        page_menu = MenuOptions(self.master)
        page_menu.pack()

       
class Instructions(Frame):
    def __init__(self,master):
        super().__init__()
        # INITIALISATION DES VARIABLES
        master = fenetre
        # Créations des widgets
        btn_retour = Button(self, text="Retour", command=self.call_menu)
        btn_retour.pack()

    # méthode d'appel de page menu

    def call_menu(self):
        self.destroy()
        page_menu = MenuOptions(self.master)
        page_menu.pack()

def Quitter() :
    global goldsorti
    fenetre.destroy()
    mesgolds="gold.txt"
    Goldus2=open(mesgolds,'w')
    print(gold) 
    goldsorti=str(gold)
    Goldus2.write(goldsorti)
    Goldus2.close()

# Widget
menu = MenuOptions(master=fenetre)
menu.pack()

#Touche fleche gauche pour aller à gauche
fenetre.bind('<Left>', left)
#Touche fleche droit pour aller à droit
fenetre.bind('<Right>',right)

fenetre.bind('<space>',tir)
fenetre.mainloop()



'''
def déplacement_projo():
    global projectile,horizon_tir,lateral_tir,compteur,tir_unique
    if len(projectile)==1:
            #projectile = can.create_image(horizon_tir,lateral_tir, image=img_projectile)
            compteur = compteur + 1
            lateral_tir = lateral_tir - 20
            can.delete(projectile[0])
            can.move(projectile,0,-20)
            fenetre.after(20,déplacement_projo)
    compteur = 0
    lateral_tir = 350
'''