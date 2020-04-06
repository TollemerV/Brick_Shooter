from tkinter import *

def InitVarEnv():
    debutJeu = 0
    score = 0
    return debutJeu, score

def afficherGlobal(x, y):
    print(x, y)

# Cette fonction affiche l'écran de présentation du jeu

def EcranDePresentation(Score, Canvas, Fenetre, DebutJeu):
    if DebutJeu == 0:
        print("blue")
        Score.configure(text="", font=('Fixedsys',16))
        Canvas.delete(ALL)
        Fenetre.after(1500,Titre(Canvas, DebutJeu))
        DebutJeu = 1
        return DebutJeu


# On afficher le nom du jeu à l'écran

def Titre(Canvas, debutJeu):
    if debutJeu!=1:
        print('red')
        Canvas.create_text(320,240,font=('Fixedsys',24),text="SPACE INVADERS",fill='blue')

