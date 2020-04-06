from tkinter import *

def InitVarEnv():
    global debutJeu, score
    debutJeu = 0
    score = 0
    return debutJeu, score

def afficherGlobal():
    print(debutJeu, score)

# Cette fonction affiche l'écran de présentation du jeu

def EcranDePresentation(Score, Canvas, Fenetre, DebutJeu):
    if DebutJeu == 0:
        Score.configure(text="", font=('Fixedsys',16))
        Canvas.delete(ALL)
        Fenetre.after(1500,Titre)
        DebutJeu = 1
        return DebutJeu


# On afficher le nom du jeu à l'écran

def Titre():
    if debutJeu!=1:
        Canvas.create_text(320,240,font=('Fixedsys',24),text="SPACE INVADERS",fill='blue')

