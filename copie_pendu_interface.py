from param�tres_pendu import*
from fonctions_pendu import*
from tkinter import*

jeu = Tk()
jeu.title('Jeu du pendu')
jeu.geometry("600x600")
image_affichee=Canvas(jeu,width=200,height=200)

image1=PhotoImage(file="bonhomme1.gif")
image2=PhotoImage(file="bonhomme2.gif")
image3=PhotoImage(file="bonhomme3.gif")
image4=PhotoImage(file="bonhomme4.gif")
image5=PhotoImage(file="bonhomme5.gif")
image6=PhotoImage(file="bonhomme6.gif")
image7=PhotoImage(file="bonhomme7.gif")
image8=PhotoImage(file="bonhomme8.gif")
liste_images = [image1,image2,image3,image4,image5,image6,image7,image8]


def jouer_pendu():
    """
    cette fonction sert à jouer au pendu
    entrée : aucune
    sortie : affiche si l'utilisateur a gagné ou perdu,l'éventuel meilleur score
    """
    i=7 
    mot_choisi = choix_mot()
    lettres_correctes = []
    lettres_fausses = []
    nb_vies = nb_chances
    mot = renvoyer_mot(mot_choisi,lettres_correctes)
    print('\n Prêt à jouer ? le score à battre est de {} \n Le mot à trouver est: {}\n'.format(meilleur_score,mot))
    
    #Le joueur commence la partie et propose des lettres 
    while mot != mot_choisi and nb_vies > 0 :
        lettre = entrer_lettre()
        
        #1e possibilité : la lettre a déjà été donnée
        if lettre in lettres_correctes or lettre in lettres_fausses :
            print('Vous avez déjà donné cette lettre')
            
        #2e posibilité : la lettre est dans le mot
        elif lettre in mot_choisi:
            lettres_correctes.append(lettre)
            print('\n Bravo ! Vous avez trouvé une lettre. Il vous reste {} vies'.format(nb_vies))
            
        #3e possibilité : la lettre n'est pas dans le mot, le joueru perd une vie
        else:
            lettres_fausses.append(lettre)
            item = image_affichee.create_image(5,5,ANCHOR=NW, image=liste_images[i])
            print("Avanc�e du pendu",item)
            image_affichee.pack()
            jeu.mainloop()
            i=i-1
            nb_vies-=1
            print('\n Non, cette lettre ne figure pas dans le mot, il vous reste {} vies'.format(nb_vies))
        mot = renvoyer_mot(mot_choisi,lettres_correctes)
        print(mot)
    
    #le mot a été trouvé 
    if mot == mot_choisi :
        #on enregistre l'éventuel meilleur score
        if nb_vies > meilleur_score:
            print('\n Vous avez battu le meilleur score, le nouveau meilleur score est: {}'.format(nb_vies))
            with open('meilleur_score.txt','w') as ms:
                ms.write(str(nb_vies))
                ms.close()
        print('\n Félicitations vous avez trouvé le mot:', mot_choisi)
        
    #le nombre de vies du jouer est tombé à 0
    else :
        print('\n Perdu, vous avez gaspillé toutes vos chances sans trouver le mot')
        print('Le mot à trouver était: {}'.format(mot_choisi))
        
    #Si le joueur souhaite relancer une partie:
    reponse = input('Souhaitez vous relancer une partie ?')
    if reponse in ['oui','OUI','O','Oui','o']:
        jouer_pendu()