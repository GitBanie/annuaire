# Annuaire de jeu vidéo by Christopher Navas
# On va mettre en place un système de CRUD pour le projet
# Pour lancé le programme on utilise la fonction init()

# Déclaration de l'annuaire via un dictionnaire avec comme keys les consoles de jeux
book = {
    'PC' : [],
    'PS4' : [],
    'ONE' : [],
    'NINTENDO SWITCH' : [],
    'WII U' : [],
    'PS3' : [],
    'XBOX 360' : [],
    '3DS' : [],
    'PS VITA' : [],
    'DS' : [],
    'WII' : [],
    'IOS' : [],
    'ANDROID' : []
}

##
### Début du CRUD
##

# Création d'un jeu
def create(console, game):
    # On enlève tous les espaces de début et fin et on met tout en maj pour éviter les effets de bord
    console = console.strip().upper()
    game = game.strip().upper()
    if console in book: # On vérifie si la console existe dans l'annuaire
        for value in book[console]: # On vérifie si le jeu existe déjà pour une console
            if value == game:
                print('Le jeu existe déjà')
                return
        book[console].append(game)
    else:
        print("La console n'existe pas")
        return
    return book

# Lecture de l'annuaire
def read():
    return(book)

# Modification d'un jeu
def update(console, old_game, new_game):
    console = console.strip().upper()
    old_game = old_game.strip().upper()
    new_game = new_game.strip().upper()
    for value in book[console]: # On vérifie si le jeu existe déjà pour une console
        if value == new_game:
            print('Le jeu existe déjà')
            return
    # On modifie toutes les anciennes occurrences de la list par la nouvelle
    book[console] = list(map(lambda x:x if x!= old_game else new_game,book[console]))
    return book

# Suppression d'un jeu
def delete(console, game):
    console = console.strip().upper()
    game = game.strip().upper()
    book[console].remove(game)
    return book

##
### Fin du CRUD
##

# Boucle infinie qui prend en paramètre le message et les valeurs de sortie de la boucle qui seront affichées à l'utilisateur
def infinite_loop(message, list_of_value):
    list_of_value = list(map(str, list_of_value)) # Conversion des elements du tableau en str
    i = 0
    while 1:
        if i in list_of_value:
            break
        # On formate le message, avec affichage des valeurs de sortie
        i = input("%s ? (%s) :"%(message.strip(), "/".join(list_of_value))).upper()
    return i

# Liste des jeux par console
def list_of_games(console):
    value_of_console = []
    for jeu in book[console]:
        value_of_console.append(jeu)
    return value_of_console

# Lancement du programme
def init():
    print("Annuaire de jeu video :\n", read())
    i = infinite_loop("Souhaitez vous faire une opération", ["O","N"])
    if  i == "N":
        print("Très bien, bonne journée.")
        return
    else:
        i = infinite_loop("Création, modification, suppréssion", ["C","M","S"])
        keys = []
        for c,v in book.items(): # Liste des consoles qui ont des valeurs
            if v != []:
                keys.append(c)
        if i == "C":
            keys = []
            for console in book.keys(): # Liste de toutes les consoles
                keys.append(console)
            console = infinite_loop("Console", keys)
            game = input("Jeu à ajouter ? :")
            create(console, game)
        if keys != []: # Si aucune valeur n'est renseignée pour le update et delete, on passe
            if i == "M":
                console = infinite_loop("Console", keys)
                value_of_console = list_of_games(console)
                old_game = infinite_loop("Jeu à changer", value_of_console)
                new_game = input("Nom du nouveau jeu ?")
                update(console, old_game, new_game)
            if i == "S":
                console = infinite_loop("Console", keys)
                value_of_console = list_of_games(console)
                game = infinite_loop("Jeu à supprimer", value_of_console)
                delete(console, game)
        else:
            print("Pas de valeur")
            return
        print(read())

try :
    init()
except NameError:
    print("La variable book n'est pas définie")
except:
    print("Erreur")
