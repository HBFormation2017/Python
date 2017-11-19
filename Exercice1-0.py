#Convertir une température Celsius en Farenheit

while True: #Tant que cette condition est Vrai alors essaye
    try:
        celsius = int(input("Saisissez la température actuelle en Celsius : "))
        faren = (celsius * 1.8) + 32
        print("La température en Farenheit est de :" , (int(faren)))
        break
    except ValueError: #Sinon affiche :
        print("Merci de saisir un nombre valide.")