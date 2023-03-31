from random import randint


choix = ["Pierre", "Feuille", "Ciseaux"]


ordi = choix[randint(0,2)]

print("Salut, ça va 😊")


def clear(nb):
    print("\n"*nb)

def regle():
    clear(5)
    print("La Pierre bat les Ciseaux\n\nLa Feuille bat la Pierre\n\nLes Ciseaux battent la Feuille\n\nSi vous et l'ordinateur avez\nle meme objet, il y a egalite")
    clear(1)
    go_menu = float(input("Ecrivez 1 chiffre quand vous\naurez fini de lire : "))
    if go_menu == 1:
        return menu()
    else:
        return menu()


def jeu():
    score_ordi = 0
    score_joueur = 0
    clear(9)
    point = int(input("Choississez le  nombre\nde points a atteindre\npour gagner : "))
    if point == 0:
        return jeu()
    clear(6)
    while score_ordi < point and score_joueur < point:
        print("Le score est de", score_joueur, "a", score_ordi,)
        clear(1)
        choix_joueur = int(input("Que voulez vous choisir\n1 = Pierre    2 = Feuille\n3 = Ciseaux : "))
        ordi = choix[randint(0,2)]
        clear(1)
        if choix_joueur == 1:
            print("Vous avez choisi Pierre")
            print("L'ordinateur a choisi", ordi)
        elif choix_joueur == 2:
            print("Vous avez choisi Feuille")
            print("L'ordinateur a choisi", ordi)
        elif choix_joueur == 3:
            print("Vous avez choisi Ciseaux")
            print("L'ordinateur a choisi", ordi)
        clear(1)
        if choix_joueur == 1 and ordi == "Ciseaux" or choix_joueur == 2 and ordi == "Pierre" or choix_joueur == 3 and ordi == "Feuille":
            score_joueur = score_joueur + 1
            print("Vous marquez 1 point")
        elif choix_joueur == 1 and ordi == "Feuille" or choix_joueur == 2 and ordi == "Ciseaux" or choix_joueur == 3 and ordi == "Pierre":
            score_ordi = score_ordi + 1
            print("L'ordinateur marque 1 point")
        elif choix_joueur == 1 and ordi == "Pierre" or choix_joueur == 2 and ordi == "Feuille" or choix_joueur == 3 and ordi == "Ciseaux":
            print("Egalite")
        else:
            print("1, 2 ou 3\nC'est pas complique")
            clear(1)
    if score_ordi == point:
        print("Le score est de", score_joueur, "a", score_ordi,"\n")
        print("DOMMAGE, vous gagnerez\nune prochaine fois\n")
        encore = int(input("Voulez vous recommencer ?\n1 = oui   2 = non : "))
        if encore == 1:
            return jeu()
        else:
            return menu()
    elif score_joueur == point:
        print("Le score est de", score_joueur, "a", score_ordi,"\n")
        print("BRAVO, vous avez gagnez")
        clear(1)
        encore = int(input("Voulez vous recommencer ?\n1 = oui   2 = non : "))
        if encore == 1:
            return jeu()
        else:
            return menu()



def menu():
    clear(3)
    print("        ______________")
    print("       |              |")
    print("       |    PIERRE    |")
    print("       |    FEUILLE   |")
    print("       |    CISEAUX   |")
    print("       |______________|")
    print("\n1 - Regle")
    print("2 - Jouer")
    clear(1)
    choix = int(input("Indiquer votre choix : " ))
    if choix == 1:
        regle()
    elif choix == 2:
        jeu()
    else:
        return menu()

menu()