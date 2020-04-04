# Cette fonction affiche l'écran de présentation du jeu

def EcranDePresentation(score, canvas, fenetre):
    if not DebutJeu:
        score.configure(text="",font=('Fixedsys',16))
        canvas.delete(ALL)
        fenetre.after(1500,Titre)
        DebutJeu = 1
        return DebutJeu
    else :
        DebutJeu = 0
        return DebutJeu

# On afficher le nom du jeu à l'écran

def Titre(canvas, DebutJeu):
    if DebutJeu!=1:
        canvas.create_text(320,240,font=('Fixedsys',24),text="SPACE INVADERS",fill='blue')


# Cette fonction va permettre d'enregistrer
# le meilleur score

def SaveMeilleurScore(resultat):
    FichierScore=open('HighScore', 'r')
    lecture=pickle.load(FichierScore)

    # Si le score réalisé à la fin de la partie
    # est sup�rieur à celui déjà enregistré dans le fichier
    # alors on remplace ce dernier par le nouveau score record
    
    if resultat > lecture:
        FichierScore=open('HighScore', 'w')
        pickle.dump(resultat,FichierScore)
        FichierScore.close()
    else:
        fenetre.after(15000,EcranDePresentation)
    FichierScore.close()

# Cette fonction permet de v�rifier
# l'existence d'un fichier

def existe(fname):
    try:
        f=open(fname,'r')
        f.close()
        return 1
    except:
        return 0

# Cette fonction permet de r�initialiser le jeu
# selon la volont� du joueur de recommencer une partie

def new_game(canvas,):
    global xe,ye,xe2,ye2,xe3,ye3,LimiteAvancement,dx,ListeCoordEnnemis,ListeEnnemis,ObusEnnemi,flag,photo,NbreEnnemis,Score,ViesJoueur
    global CoordonneesBriques,projectile,feu,feuEnnemi,PasAvancement
    global dyobus,dyobusEnnemi,DebutJeu,dxeb,Mort,photo
    
    DebutJeu=1

    # FOND DU JEU

    photo=PhotoImage(file='fond.gif')
    canvas.create_image(320,240,image=photo)

    Mort=0

    # On efface tout � l'�cran
    
    canvas.delete(ALL)
    canvas.create_image(320,240,image=photo)

    # Coordonnées de départ des ennemis
    # pour chaque catégorie
    
    xe,ye=20,20
    xe2,ye2=20,80
    xe3,ye3=20,160
    
    LimiteAvancement=1
    if len(ObusEnnemi)==1:
        can.delete(ObusEnnemi[0])
    dx=1

    # Pas d'avancement d'un obus
    # tir� par le joueur
    
    dyobus=20

    # Pas d'avancement d'un obus
    # tir� par un ennemi
    
    dyobusEnnemi=10

    ViesJoueur=3
    Score=0
    feuEnnemi=0
    
    Ennemis1=[]
    Ennemis2=[]
    Ennemis3=[]
    ListeEnnemis=[Ennemis1,Ennemis2,Ennemis3]
    

    projectile=[]
    
    CoordEnnemis1=[]
    CoordEnnemis2=[]
    CoordEnnemis3=[]
    ListeCoordEnnemis=[CoordEnnemis1,CoordEnnemis2,CoordEnnemis3]
    
    NbreEnnemis1=6
    NbreEnnemis2=6
    NbreEnnemis3=6
    PasAvancement=0
    NbreEnnemis=[NbreEnnemis1,NbreEnnemis2,NbreEnnemis3]
    
    v=0

    dxeb=5

    Creation_CanonMobile()

    # On d�termine de mani�re al�atoire
    # le nombre de temps avant qu'apparaisse
    # le premier ennemi bonus du jeu :)


    AffichageScore.configure(text="Score : "+str(Score),font=('Fixedsys',16))
    AffichageVie.configure(text="Lives : "+str(ViesJoueur),font=('Fixedsys',16))
    

    # Appel des fonctions de cr�ation des ennemis
    # pour recr�er un bataillon de vaisseaux hostiles
    # pr�ts � en d�coudre � nouveau avec le joueur !!
    
    while v<6:
        Ennemi_Categorie1()
        Ennemi_Categorie2()
        Ennemi_Categorie3()
        v+=1

    flag=1
   
    

# Cette fonction permet de cr�er le nerf de la guerre
# ==> Le canon mobile \o/

def Creation_CanonMobile():
    global canon,xc1,xc2,yc1,yc2
    canon=[]

    xc1=20
    yc1=440

    # Cr�ation du canon

    canon.append(canvas.create_rectangle(xc1,yc1,xc1+20,yc1+20,fill='blue'))

    xc2=xc1-20
    yc2=yc1+20

    # Cr�ation de la plate-forme du canon
    
    

# Les 3 fonctions ci-dessous vont permettre de cr�er les ennemis du jeu

# Cr�ation de la 1er cat�gorie d'ennemis du jeu

def Generer_Ennemis():
    global ListeEnnemis,ListeCoordEnnemis,xe,ye
    ListeCoordEnnemis[0].append([xe,ye])
    Ennemis=[]
    Ennemis.append(canvas.create_rectangle(xe,ye,xe,ye,fill='red'))
    Ennemis.append(canvas.create_rectangle(xe,ye,xe,ye,fill='red'))
    Ennemis.append(canvas.create_rectangle(xe,ye,xe,ye,fill='red'))
    ListeEnnemis[0].append(Ennemis)
    xe=xe+80

# Cette fonction permet d'afficher
# le nombre de points gagn�s � la suite
# de la destruction d'un ennemi

def score(donnee,x,y,x2,y2):
    global afficherScore
    afficherScore.append(can.create_text(x+x2,y+y2,font=('Fixedsys',8),text=str(donnee)+' pts',fill='red'))
    fen.after(1500,EffacerScore)

# Cette fonction permet d'effacer
# le nombre de point gagn�s et affich�s
# suite � la destruction d'un ennemi

def EffacerScore():
    global afficherScore
    i=0
    while i<len(afficherScore):
        can.delete(afficherScore[i])
        i+=1

# La fonction ci-dessous permet
# d'animer le canon mobile selon
# la direction choisie par le joueur

def move(dx):
    global xc1,xc2,yc1,yc2,ViesJoueur,flag

    if ViesJoueur!=0 or flag!=0:
   
        xc1=xc1+dx
        xc2=xc2+dx

        # Si on arrive au bord de l'�cran
        # le canon mobile se retrouve bloqu�
        # afin de ne pas aller plus loin :p
        
        if xc2<=0:
            xc1=20
            #limite
            xc2=0
            can.coords(canon[0],xc1,yc1,xc1+20,yc1+20)
        elif xc2>=600:
            xc1=600
             #limite
            xc2=580
            can.coords(canon[0],xc1,yc1,xc1+20,yc1+20)
        else:
            can.coords(canon[0],xc1,yc1,xc1+20,yc1+20)

# Cette fonction va s'occuper de faire les ennemis se d�placer
# automatiquement dans le canevas histoire qu'ils puissent esquiver
# les tirs du joueur ( un genre d'IA à deux balles quoi !! XD )

def ennemis():
    global dx,NbreEnnemis,Xobus,Yobus,ListeCoordEnnemis,DebutJeu
    global ListeEnnemis,PasAvancement,NbreEnnemis,flag,LimiteAvancement,BonusActif

    if flag!=0 and len(NbreEnnemis)>=1 and DebutJeu!=0:

        # Si tous les ennemis ont �t� d�truits
        # ce n'est pas la peine d'ex�cuter l'animation
        # de quelque chose qui n'existe plus :p

        if NbreEnnemis!=0:
            i=0
            t=0
            PasAvancement+=1

            # Si jamais les ennemis atteignent le bas
            # de l'�cran la partie s'arr�te et le joueur
            # a perdu !! :p
           
            while i<len(ListeCoordEnnemis):
                while t<len(ListeCoordEnnemis[i]):
                    if ListeCoordEnnemis[i][t][1]>=420:
                        can.delete(ALL)
                        image()
                        flag=0
                        can.create_text(320,240,font=('Fixedsys',18),text="Game Over !!",fill='red')
                        can.delete(canon[0])
                        can.delete(canon[1])
                        DebutJeu=0
                        SaveMeilleurScore(Score)
                    t+=1
                t=0
                i+=1

            i=0

            # Si les ennemis arrive au bout de l'�cran
            # leur direction s'inverse et ils vont
            # dans le sens oppos�

            dy=0
            

            if dx>0:

                # On va utiliser cette 2e variable afin
                # de s'assurer de l'inversion de la direction
                # des ennemis
                
                dx2=dx
                if len(ListeCoordEnnemis[0])!=0:
                    if ListeCoordEnnemis[0][len(ListeCoordEnnemis[0])-1][0]>=560:
                        dx=-dx2
                        dy=10
                if len(ListeCoordEnnemis[1])!=0:
                    if ListeCoordEnnemis[1][len(ListeCoordEnnemis[1])-1][0]>=560:
                        dx=-dx2
                        dy=10
                if len(ListeCoordEnnemis[2])!=0:
                    if ListeCoordEnnemis[2][len(ListeCoordEnnemis[2])-1][0]>=560:
                        dx=-dx2
                        dy=10
            elif dx<0:
                dx2=dx
                if len(ListeCoordEnnemis[0])!=0:
                    if ListeCoordEnnemis[0][0][0]<=20:
                        dx=-dx2
                        dy=10
                if len(ListeCoordEnnemis[1])!=0:
                    if ListeCoordEnnemis[1][0][0]<=20:
                        dx=-dx2
                        dy=10
                if len(ListeCoordEnnemis[2])!=0:
                    if ListeCoordEnnemis[2][0][0]<=20:
                        dx=-dx2
                        dy=10

            i=0
            t=0

            # On fait avancer tous les ennemis
            # du canevas
            
            while i<len(ListeCoordEnnemis):
                while t<len(ListeCoordEnnemis[i]):
                    ListeCoordEnnemis[i][t][0]=ListeCoordEnnemis[i][t][0]+dx
                    ListeCoordEnnemis[i][t][1]=ListeCoordEnnemis[i][t][1]+dy
                    t+=1
                i+=1
                t=0
            i=0
            while i<NbreEnnemis[0]:
                can.coords(ListeEnnemis[0][i][0],ListeCoordEnnemis[0][i][0],ListeCoordEnnemis[0][i][1],ListeCoordEnnemis[0][i][0]+60,ListeCoordEnnemis[0][i][1]+20)
 
                i+=1
            i=0
            while i<NbreEnnemis[1]: 
                can.coords(ListeEnnemis[1][i][0],ListeCoordEnnemis[1][i][0],ListeCoordEnnemis[1][i][1],ListeCoordEnnemis[1][i][0]+20,ListeCoordEnnemis[1][i][1]+40)

                i+=1
            i=0
            while i<NbreEnnemis[2]:
                can.coords(ListeEnnemis[2][i][0],ListeCoordEnnemis[2][i][0]+20,ListeCoordEnnemis[2][i][1],ListeCoordEnnemis[2][i][0]+40,ListeCoordEnnemis[2][i][1]+60)
               
                i+=1
            fen.after(50,ennemis)
    else:
        fen.after(50,ennemis)

# Cette fonction permet d'animer l'obus tir�
# par un ennemi

def AnimationObusEnnemi():
    global xe,ye,dyobusEnnemi,Yobus,Xobus,ObusEnnemi,feuEnnemi,yc1,feu,ViesJoueur
    global flag,projectile,DebutJeu,Score,Mort,ArretAnimation,canon
    if flag!=0:
        if feuEnnemi==1:
            Yobus=Yobus+dyobusEnnemi
            appelvarglob()
                                
'''
Si le joueur meurt on delte tout et on met un ecran de fin 
                if ViesJoueur = 0:
                    
                    can.delete(ALL)
                    image()
                    can.create_text(320,240,font=('Fixedsys',18),text="Game Over !!",fill='red')
                    feu=0
                    ArretAnimation=0
                    can.delete(canon[0])
                    can.delete(canon[1])
                    DebutJeu=0

                    # On v�rifie le score
                    
                    SaveMeilleurScore(Score)


                    # Suspension des animations
                    
                    flag=0
'''

# Cette fonction va permettre d'afficher un
# paysage post-apocalyptique si le joueur
# fait un game over !! :( :(

def image():
    global photo
    photo=PhotoImage(file='apocalypse.GIF')
    can.create_image(320,240,image=photo)
    
    
# Cette fonction va permettre de g�rer le tir du canon
# ainsi que les collisions avec les cibles situ�es en
# haut du canevas :)

def tir_joueur(event):
    global xc2,yc2,xtir,ytir,projectile,feu,VieEnnemi,flag,DebutJeu
    if DebutJeu!=0:
        if flag!=0:
            if feu!=1 :
                feu=1
                xtir=xc2+20
                ytir=yc2-40
                projectile=[(can.create_oval(xtir,ytir,xtir+20,ytir+20,fill='yellow'))]
                time.sleep(0.09)

                # On lance l'animation de l'obus
                # tir� par le joueur
                
                AnimationObus()



def appelvarglob():
    global xtir,ytir,feu,Xobus,Yobus,feuEnnemi,ObusEnnemi,projectile

# Cette fonction va permettre d'animer l'obus tir� par
# le canon mobile

def AnimationObus():
    global projectile,xtir,ytir,feu,xe,ye,xe2,ye2,xe3,ye3,PasAvancement,dx,BonusActif
    global VieEnnemi,feuEnnemi,NbreEnnemis,ListeCoordEnnemis,Score,NbreEnnemis,ListeEnnemis,flag,LimiteAvancement
    global xeb,yeb,EnnemiBonus,ArretAnimation

    if flag!=0 and len(projectile)==1 and ArretAnimation!=1:
        if feu==1:
            ytir=ytir-dyobus
            appelvarglob()
            if ytir<=20:
                feu=0
                can.delete(projectile[0])

            # Le bloc d'instructions qui suit permet de g�rer l'int�raction entre
            # un tir d'obus provoqu� par le joueur et un ennemi, donc si l'obus
            # touche un ennemi il est logique de dire que celui-ci est d�truit
            
            i=0
            t=0

            while i<len(ListeCoordEnnemis):

                # Pour qu'il n'y ai pas d'erreur au cas o�
                # La liste des coordonn�es des ennemis est vide
                # on execute le bloc d'instructions suivant
                # uniquement quand la liste des coordonn�es n'est
                # pas vide
                
                if len(ListeCoordEnnemis)>=1:
                    if len(ListeCoordEnnemis[i])>=1:
                        while t<len(ListeCoordEnnemis[i]):
                            if xtir+5>=ListeCoordEnnemis[i][t][0] and xtir-5<=ListeCoordEnnemis[i][t][0]+60 :
                                if ytir<=ListeCoordEnnemis[i][t][1]+5 and ytir>=ListeCoordEnnemis[i][t][1]-60 :
                                    Score=Score+50
                                    feu=0
                                    AffichageScore.configure(text="Score : "+str(Score),font=('Fixedsys',16))
                                    can.delete(projectile[0])
                                    score(50,ListeCoordEnnemis[i][t][0],ListeCoordEnnemis[i][t][1],30,20)
                                    if i==0:
                                        NbreEnnemis[0]=NbreEnnemis[0]-1
                                        can.delete(ListeEnnemis[i][t][0])
                                        can.delete(ListeEnnemis[i][t][1])
                                        can.delete(ListeEnnemis[i][t][2])
                                        del ListeEnnemis[i][t]
                                        del ListeCoordEnnemis[i][t]
                                    elif i==1:
                                        NbreEnnemis[1]=NbreEnnemis[1]-1
                                        can.delete(ListeEnnemis[i][t][0])
                                        can.delete(ListeEnnemis[i][t][1])
                                        can.delete(ListeEnnemis[i][t][2])
                                        del ListeEnnemis[i][t]
                                        del ListeCoordEnnemis[i][t]
                                    elif i==2:
                                        NbreEnnemis[2]=NbreEnnemis[2]-1
                                        can.delete(ListeEnnemis[i][t][0])
                                        can.delete(ListeEnnemis[i][t][1])
                                        del ListeEnnemis[i][t]
                                        del ListeCoordEnnemis[i][t]

                            t+=1
                    t=0
                    i+=1

            # Quand il n'y a plus d'ennemis ben on recommence
            # le carnage mais cette fois en rendant la bataille
            # plus �pic�e !! T_T
            
            if NbreEnnemis[0]+NbreEnnemis[1]+NbreEnnemis[2]==0:

                # On efface le canon mobile pour le recr�er

                can.delete(canon[0])
                can.delete(canon[1])

                Creation_CanonMobile()

                # On reprend tous les param�tres de d�part
                # afin qu'il n'y ai aucune erreur

                xe,ye=20,20
                xe2,ye2=20,80
                xe3,ye3=20,160

                # On accel�re la cadence des ennemis !!
                # Caramba !! XD
                    
                dx=dx+1
                
                flag=0

                # Le joueur et les ennemis pourront
                # � nouveau tirer !!
                
                feu=0
                feuEnnemi=0

                BonusActif=0
                
                Ennemis1=[]
                Ennemis2=[]
                Ennemis3=[]
                ListeEnnemis=[Ennemis1,Ennemis2,Ennemis3]
                
                
                CoordEnnemis1=[]
                CoordEnnemis2=[]
                CoordEnnemis3=[]
                
                ListeCoordEnnemis=[CoordEnnemis1,CoordEnnemis2,CoordEnnemis3]
                
                NbreEnnemis1=6
                NbreEnnemis2=6
                NbreEnnemis3=6
                PasAvancement=0
                NbreEnnemis=[NbreEnnemis1,NbreEnnemis2,NbreEnnemis3]
                
                v=0

                # Appel des fonctions de cr�ation des ennemis
                # pour recr�er un bataillon de vaisseaux hostiles
                # pr�ts � en d�coudre � nouveau avec le joueur !!
                
                while v<6:
                    Ennemi_Categorie1()
                    Ennemi_Categorie2()
                    Ennemi_Categorie3()
                    v+=1
                flag=1
            else:
                can.coords(projectile[0],xtir,ytir,xtir+20,ytir+20)
                fen.after(50,AnimationObus)
    

# Les deux fonctions ci-dessous permettent
# de diriger le canon mobile de gauche � droite

def right(event):
    global flag,DebutJeu
    if DebutJeu!=0:
        if flag!=0:
            move(20)

def left(event):
    global flag,DebutJeu
    if DebutJeu!=0:
        if flag!=0:
            move(-20)