# Compter le nombre de lettres dans une chaîne de caractères
"""
mot = str(input("Saisissez un mot ou une phrase : "))

#Création de la liste des voyelles
liste_voyelles = ["a","e","i","o","u","y"] 

#Compteur des voyelles
nb_voyelles = 0         

#Boucle pour compter les voyelles
for lettre in mot: 
    if lettre in liste_voyelles:
        nb_voyelles += 1
if nb_voyelles == 0: 
        print("Il n'y a pas de voyelles dans ce mot ou cette phrase :" , mot)
elif nb_voyelles == 1:
    print("Il y a une seule voyelle dans ce mot ou cette phrase : " , mot)
else:  
    print("Le mot :" , mot , "contient" , int(nb_voyelles) , "voyelles.")
print("Fin")

 Seconde proposition """

# Compter le nombre de voyelles dans un mot ou une phrase
i = 0
j = 0
nb = 0

mot = str(input("Saisissez un mot ou une phrase : "))
voyelles = "aeiouAEIOU"

compteur = 0

while i < len(mot):

    while j < len(voyelles):

        if (mot[i] == voyelles[j]):
            compteur +=1
        j= j+1
    j=0
    i = i+1

print("Le nombre de voyelles dans" , mot , "est de : " , compteur)