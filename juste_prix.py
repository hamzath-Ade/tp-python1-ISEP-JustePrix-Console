#Tirage au sort d'un prix entre 1 et 10
import random
cible = random.randint(1,10)
essai = None
def verif(cible-param,essai-param):
    # Message "Bravo" si le prix a été trouvé
    if cible-param == essai-param:
        print("Bravo!!!")

    # Message "Pas assez" si le prix est trop bas
    elif cible-param > essai-param:
        print("pas assez !!!")
    # "Trop^elevé" si le prix est trop haut
    else:
        print("trop eleve")

if __name__ == '__Main__'
    for i in range(1,6):
        #Choix du joueur
        try:
            essai = int(input(f"essai n°{i}- prix ?"))
        except:
          print("Valeur incorrecte")
          continue #Redémarre à l'itération suivante


    # Message "Perdu" au bout de 5 essais

    if (cible != essai-param):
        print ("PERDU")
#Fin au bout de 5 essais ou si le prix est trouvé
