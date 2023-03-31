import tkinter as tk
from random import randint
from PIL import ImageTk,Image
from tkinter.messagebox import*
import time

#######################################################
####### Declaration des Fonctions #####################
#######################################################


def regle():
    fenetre.withdraw()
    fenetre1.deiconify()
    

def arriere():
    fenetre1.withdraw()
    fenetre.deiconify()
    
def quitter():
    fenetre.quit()
    fenetre1.quit()
    fenetre2.quit()

def back():
    fenetre2.withdraw()
    fenetre.deiconify()
    reinit()

def tksleep(t):
    ms = int(t*1000)
    fenetre2= tk._get_default_root('sleep')
    var= tk.IntVar(fenetre2)
    tk.IntVar(fenetre2)
    fenetre2.after(ms,var.set,1)
    fenetre.wait_variable(var)



    


def jeu():
    fenetre2.deiconify()
    fenetre.withdraw()

def jouer(coup_utilisateur):
 global score_ordinateur, score_utilisateur, score1, score2,imagerien,imagerien1
 coup_ordinateur = randint(1,3)
 if coup_ordinateur==1:                             
    imagerien1.configure(image=pierre)              #pierre=1
 elif coup_ordinateur==2:                           
    imagerien1.configure(image=papier)              #papier=2
 else:                                                  
    imagerien1.configure(image=ciseaux)             #ciseaux=3
 augmenter_scores(coup_ordinateur,coup_utilisateur)
 score1.configure(text=str(score_utilisateur))
 score2.configure(text=str(score_ordinateur))
 if score_ordinateur==3 :
    showinfo("Perdu!","L'ordinateur a gagné!")
    if askyesno("Retry", "Voulez-vous recommencer?"):
        reinit()
    else:
        back() 
 elif score_utilisateur==3:
    showinfo("Félicitations!","Vous avez gagné!")
    if askyesno("Retry ", "Voulez-vous recommencer?"):
        reinit()
    else:
        back()
    


def jouer_pierre():
    global bouton5
    bouton5.configure(image=rougep)
    tksleep(0.2)
    bouton5.configure(image=pierre)
    imagerien.configure(image=pierre)
    jouer(1)
    

def jouer_papier():
    global bouton6
    bouton6.configure(image=rougef)
    tksleep(0.2)
    bouton6.configure(image=papier)
    imagerien.configure(image=papier)
    jouer(2)
    

def jouer_ciseaux():
    global bouton7
    bouton7.configure(image=rougec)
    tksleep(0.2)
    bouton7.configure(image=ciseaux)
    imagerien.configure(image=ciseaux)
    jouer(3)
    
    


def augmenter_scores(coup_ordinateur,coup_utilisateur):
    global score_ordinateur, score_utilisateur
    if coup_ordinateur == 1 and coup_utilisateur == 2:
        score_utilisateur = score_utilisateur + 1
    elif coup_ordinateur == 2 and coup_utilisateur == 1:
        score_ordinateur = score_ordinateur + 1
    elif coup_ordinateur == 1 and coup_utilisateur == 3:
        score_ordinateur = score_ordinateur + 1
    elif coup_ordinateur == 3 and coup_utilisateur == 1:
        score_utilisateur = score_utilisateur + 1
    elif coup_ordinateur == 3 and coup_utilisateur == 2:
        score_ordinateur = score_ordinateur + 1
    elif coup_ordinateur == 2 and coup_utilisateur == 3:
        score_utilisateur = score_ordinateur + 1


def reinit():
 global score_ordinateur, score_utilisateur, score1, score2, imagerien, imagerien1
 score_utilisateur = 0
 score_ordinateur = 0
 score1.configure(text=str(score_utilisateur))
 score2.configure(text=str(score_ordinateur))
 imagerien.configure(image=rien)
 imagerien1.configure(image=rien)

##################################################
################## Variables Globales#############
##################################################


# variables globales
score_utilisateur = 0
score_ordinateur = 0




####################################################
################### LES FENETRES ###################
####################################################


#création de la fenêtre:
fenetre=tk.Tk()
fenetre.geometry('1600x1200')
fenetre.title('pierre/papier/ciseaux')
fenetre.iconbitmap(r'favicon.ico')
fenetre.config(bg='black')
fenetre.protocol("WM_DELETE_WINDOW", quitter)
fenetre.resizable(width=True,height=True)
fenetre.attributes('-fullscreen', True)

#fond écran Menu principal
homer1 = Image.open("wallpaper.jpg") 
homer1 = ImageTk.PhotoImage(homer1)
texte = tk.Label(fenetre, image=homer1)
texte.place(x=0,y=0, width=1600, height=1200)




#Création de la fenêtre de Règles du Jeu 
fenetre1=tk.Toplevel()
fenetre1.geometry('1600x1200')
fenetre1.config(bg='black')
fenetre1.title('Règles du jeu')
fenetre1.iconbitmap(r'favicon.ico')

#cacher la fenêtre
fenetre1.withdraw()
fenetre1.protocol("WM_DELETE_WINDOW", quitter)
fenetre1.attributes('-fullscreen', True)
fenetre1.resizable(width=True,height=True)


#Creation de la fenetre JEU
fenetre2=tk.Toplevel()
fenetre2.geometry('1600x1200')
fenetre2.config(bg='#28B4E5')
fenetre2.title('LE JEU')
fenetre2.iconbitmap(r'favicon.ico')

#cacher la fenêtre
fenetre2.withdraw()
fenetre2.protocol("WM_DELETE_WINDOW", quitter)
fenetre2.attributes('-fullscreen', True)
fenetre2.resizable(width=True,height=True)

#################################################
######## IMPORTATION DES IMAGES #################
#################################################

# images
rien=ImageTk.PhotoImage(Image.open('fond-rien.jpg'))
rien1=ImageTk.PhotoImage(Image.open('fond-rien.jpg'))
versus= ImageTk.PhotoImage(Image.open('VS.png'))
pierre = ImageTk.PhotoImage(Image.open('pierrev2.png'))
papier = ImageTk.PhotoImage(Image.open('papierv2.png'))
ciseaux = ImageTk.PhotoImage(Image.open('ciseauxv2.png'))
rougep=ImageTk.PhotoImage(Image.open('rougepierre.png'))
rougef=ImageTk.PhotoImage(Image.open('rougepapier.png'))
rougec=ImageTk.PhotoImage(Image.open('rougeciseaux.png'))


 

####################################################
################# LES BOUTTONS #####################   
####################################################




#afficher la chaine de caractère menu principal
libelle_affiche = tk.Label(fenetre, text="Menu Principal",font=("Verdana",30,'italic bold'),bg='red',fg='white')
libelle_affiche.place(x=600,y=40, width=340, height=45)



#boutton règles du jeu
bouton= tk.Button(fenetre,text='Règles du jeu',font=("Helvetica",13),width=80,height=20,command=regle)
bouton.place(x=650,y=200,width=240,height=40)




#boutton lancer le jeu
bouton1= tk.Button(fenetre,text='Lancer le jeu',font=("Helvetica",13), width=80,height=20,command=jeu)
bouton1.place(x=650,y=300,width=240,height=40)


#boutton retour en arrière règles du jeu
bouton2= tk.Button(fenetre1,text='<-', width=80,height=20,command=arriere)
bouton2.place(x=50,y=40,width=40,height=40)



#boutton retour en arrière jeu
bouton4= tk.Button(fenetre2,text='<-', width=80,height=20,command=back)
bouton4.place(x=50,y=40,width=40,height=40)

#boutton recommencer
bouton4 = tk.Button(fenetre2,text='Recommencer',font=("Helvetica",10),command=reinit)
bouton4.place(x=1380,y=10,width=100,height=40)



#boutton pour quitter le jeu
bouton3= tk.Button(fenetre,text='Quitter',fg='red',font=("Helvetica",13), width=80,height=20,command=quitter)
bouton3.place(x=650,y=400,width=240,height=40)


#BOUTTON PIERRE
bouton5 = tk.Button(fenetre2,command=jouer_pierre)
bouton5.configure(image=pierre)
bouton5.place(x=100,y=600,width=200,height=200)

#BOUTTON PAPIER
bouton6 = tk.Button(fenetre2,command=jouer_papier)
bouton6.configure(image=papier)
bouton6.place(x=650,y=600,width=200,height=200)

#BOUTTON CISEAUX
bouton7 = tk.Button(fenetre2,command=jouer_ciseaux)
bouton7.configure(image=ciseaux)
bouton7.place(x=1200,y=600,width=200,height=200)

#################################################################
######### AFFICHAGE DES LABELS ET DES IMAGES ####################
#################################################################



#LABEL + IMAGE LABEL
imageversus= tk.Label(fenetre2,image=versus)
imageversus.place(x=600,y=250,width=300,height=256)
imagerien=tk.Label(fenetre2,image=rien)
imagerien.place(x=250,y=300,width=200,height=200)
imagerien1=tk.Label(fenetre2,image=rien)
imagerien1.place(x=1050,y=300,width=200,height=200)
imageversus= tk.Label(fenetre2,image=versus)
imageversus.place(x=600,y=250,width=300,height=256)
imagerien=tk.Label(fenetre2,image=rien)
imagerien.place(x=250,y=300,width=200,height=200)
imagerien1=tk.Label(fenetre2,image=rien)
imagerien1.place(x=1050,y=300,width=200,height=200)
texte1 = tk.Label(fenetre2, text="Utilisateur :", font=("Helvetica", 16))
texte1.place(x=250,y=60,width=150,height=60)
texte2 = tk.Label(fenetre2, text="Machine :", font=("Helvetica", 16))
texte2.place(x=1050,y=60,width=150,height=60)
texte3 = tk.Label(fenetre2, text="Pour jouer, cliquez sur une des icones ci-dessous.",font=("Helvetica",10))
texte3.place(x=600,y=10,width=300,height=40)
score1 = tk.Label(fenetre2, text="0", font=("Helvetica", 16))
score1.place(x=250,y=100,width=150,height=60)
score2 = tk.Label(fenetre2, text="0", font=("Helvetica", 16))
score2.place(x=1050,y=100,width=150,height=60)





#################################################################
######### REGLES DU JEU AFFICHAGE ################################
#################################################################


texte="""Pierre Papier Ciseaux
Vous connaissez peut-être ce jeu sous l’une de ses multiples appellations pierre papier ciseaux, pierre feuille ciseaux, chifoumi (ou shifumi) 
Pierre papier ciseaux est le jeu idéal pour vous aider à prendre des décisions. 
Exemple Pourquoi ne pas décider de ça en faisant une partie de chifoumi? 
Le perdant fait la vaisselle et en quelques secondes le problème est réglé. 
Bien évidemment il existe de nombreux cas possible dans lequel une partie de chifoumi vous sera bien utile !
Comment jouer à pierre papier ciseaux ?
Les règles du jeu sont vraiment très simples et vous n’avez besoin de rien pour jouer, si ce n’est que votre sourit.
Comme il existe plusieurs variantes je vais vous présenter les règles de la version classique du shifumi qui se joue à 1 joueurs contre l’ordi. 
A l’aide de vos mains vous aurez la possibilité de choisir entre 3 signes : la pierre, le papier ou les ciseaux.
1.    Le joueur doit sélectionner 1 des 3 signes la pierre, le papier ou les ciseaux.
2.    Le jouer qui a accumulé 5 points à gagner 
Une fois que le joueur est l’ordi ont dévoilés leurs signes voici comment est déterminé le gagnant.
•    La pierre casse les ciseaux, la pierre gagne contre les ciseaux
•    Les ciseaux coupent le papier, les ciseaux gagnent contre le papier
•    Le papier recouvre la pierre, le papier gagne contre la pierre
En cas d’égalité vous rejouez jusqu’à ce qu’il y ait un gagnant.
Jouer en ligne 
Vous vous ennuyez et vous n’avez pas d’amis à proximité avec lesquels vous pourriez jouer à pierre papier ciseaux ? 
Grâce à notre jeu de chifoumi en ligne vous pourrez jouer gratuitement et affronter l’ordinateur"""

#ZONE D'AFFICHAGE DU TEXTE
libelle_affiche1 = tk.Label(fenetre1, text=texte,bg='black',fg='white',font=("Helvetica", 16),anchor='w',justify=tk.CENTER,wraplength = 695)
libelle_affiche1.place(x=410,y=50,width=1000)




#Boucle fenetre
fenetre.mainloop()




