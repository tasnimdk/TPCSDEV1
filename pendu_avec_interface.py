from tkinter import*
from fonctions_pendu import*
from paramètres_pendu import*
from copie_pendu_interface import*

jeu = Tk()
jeu.title('Jeu du pendu')
jeu.geometry("600x600")
l = Label(text="label")
l.pack()
entree_lettre = entry()
entree_lettre.pack()
BouttonProposer = Button(jeu,text="Proposer",command=jouer_pendu)
BouttonProposer.pack()
jeu.mainloop()









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



    
