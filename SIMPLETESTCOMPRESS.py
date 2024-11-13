print("Programme de compression de texte simple écrit par les membres du Groupe5") #Affichage du titre du programme
def compresser_texte(texte):   #Fonction de compression de texte
    if not texte:  #Vérification si le texte est vide
        return ""
    #Initialisation des variables
    resultat = []
    compteur = 1
    
    for i in range(1, len(texte)):  #Parcours du texte
        if texte[i] == texte[i - 1]:  #Verification si le caractère est identique au precedent
            compteur += 1 #Incrementation du compteur qui permet de compter le nombre de fois le caractère est répété 
        else:
            resultat.append(texte[i - 1] + str(compteur)) #enregiste le caractère et son nombre de répétitions dans "résultat" 
            compteur = 1 #Reinitialisation du compteur pour le nouveau caractère 

    resultat.append(texte[-1] + str(compteur)) #Ajoute le dernier caractère et le compteur au resultat
    return ''.join(resultat)#Retourne le résultat, c'est à dire le texte compressé sous forme de chaine
  
   

# Exemple d'utilisation
texte = "aaabbcccc"
texte_compresse = compresser_texte(texte) #appel de notre fonction afin qu'il compresse le texte
print("\nExemple d'utilisation") #Affichage d'un exemple pour utilisateur, pour lui montrer un exemple d'utilisation du programme 
print("La version compressée de aaabbcccc est:", texte_compresse)  # Affiche "a3b2c4", la version compressé de "aaabbcccc"
texte_user=input("\nVeuillez entrer votre texte personnel à compressé pour tester l'efficacité du programme:") #demande à l'utilisateur d'entrer son propre texte pour que le programme compresse ce texte
compress_texte=compresser_texte(texte_user) #Appel de notre fonction pour qu'il compresse le texte de l'utilisateur 
print("La version compressé de votre texte(", texte_user,") est: ", compress_texte) #Affche le texte compressé à l'utilisateur 
print("\nHave a Good day sir")  #Souhaite bonne journée au Docteur Wohwe, notre enseignant qui nous a encouragés à apprendre python