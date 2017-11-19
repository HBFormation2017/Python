# Application TODO : Ajouter une tâche / Supprimer une tâche / Evaluer la charge de travail
TacheTab = []
AjouterTache = "1"
SupprimerTache = "2"
ListerTache = "3"
i = 0
n = 0
Tache = 0

while True:
    SaisieUser = input("Que voulez-vous faire ? Ajouter : 1, Supprimer : 2, Lister : 3 une(des) tâche(s) : ")
    print(SaisieUser)
    if SaisieUser == AjouterTache:
        AjoutTache = input("Ecrivez votre tâche : ")
        TacheTab.append(AjoutTache)
        print(TacheTab[n])
        n = n+1

    if SaisieUser == ListerTache:
        print(TacheTab[:])
        if TacheTab == 0:
            print("Vous n'avez saisi aucune tâche.")

    if SaisieUser == SupprimerTache:
        SaisieTache = input("Quelle tâche voulez-vous supprimer ? : ")
        for SaisieTache in TacheTab:
            if SaisieTache == TacheTab:
                print("Vous avez supprimé la tâche")

