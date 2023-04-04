from copy import deepcopy
from random import randrange
import tkinter as tk
from random import*
from tkinter import*
from tkinter import ttk 
from PIL import Image,ImageTk  

"""" Les liens vers des tutoriels desquels nous nous sommes inspirés pour réaliser les deux interfaces : 
       https://www.youtube.com/channel/UCFB0dxMudkws1q8w5NJEAmw   , Auteur : non-défini
       https://www.codespeedy.com/tkinter-pack-grid-method-in-python/ , Auteur : Jitendra Kumar 
       https://riptutorial.com/tkinter/example/17181/getting-the-value-of-an-entry-widget ,Auteur : non-défini
       https://www.geeksforgeeks.org/python-tkinter-text-widget/  , Auteur : KaranGupta5 """



# Interface utilisateur : La première interface qui s’affiche lorsqu’on exécute le programme, contient le choix de niveau de complexité.

class Interface_utilisateur:
    WIN=tk.Tk()
    WIN.geometry("300x200")
    

    WIN.title("  SUDOKU  ")
    WIN.resizable(0,0)
    WIN.config(bg="snow2")
    

    LABEL=Label(WIN, text = "Choisir un niveau :",
          font = ("Helvetica", 14),bg="snow2")
    LABEL.grid(column=0, row=5, padx=10, pady=25)
    VALEURS=["Simple","Moyen","Avancé"]
    
    
    def __init__(self):
        
     self.n = tk.StringVar()
     self.niveau= ttk.Combobox(Interface_utilisateur.WIN, width = 10, textvariable = self.n, 
                                state='readonly')
     self.niveau["values"]=Interface_utilisateur.VALEURS
     self.niveau.grid(column=1, row=5, padx=10, pady=25)
     self.niveau.current(0)
    
     self.btn_nouv_fenetre=Button(Interface_utilisateur.WIN,bd=4,text="Nouvelle Partie",command=lambda:[Interface_utilisateur.WIN.destroy(),Interface_sudoku(self.n.get()) ])
     self.btn_nouv_fenetre.grid(column=0, row=10, padx=10, pady=20)
     self.btn_quitter=Button(Interface_utilisateur.WIN,bd=4,text="Quitter",command=lambda:[Interface_utilisateur.WIN.destroy() ])
     self.btn_quitter.grid(column=1, row=10, padx=5, pady=25,ipadx=10)
     Interface_utilisateur.WIN.mainloop()

# L’interface du jeu : Elle va s’afficher après que l’utilisateur fasse un choix de niveau et presse le bouton nouvelle partie, initialisée
# avec le niveau choisi par l’utilisateur

class Interface_sudoku:
    
    def __init__(self,etat):
        self.etat=etat
        self.entries=[]
        self.entry=[]
        # le self.complexite représente le nombre de cases vides dans la matrice afficher a l’utilisateur 
        if self.etat=="Simple":
            self.complexite=25  
        elif self.etat=="Moyen":
            self.complexite=40
        else:
            self.complexite=55
        
        self.win2=tk.Tk()
        self.win2.geometry("500x700")
        self.win2.config(bg="snow2")
        
        self.win2.title("  SUDOKU  ")
        self.win2.resizable(0,0)
        
        
        # Ajout d’une image à l’interface
        self.img = ImageTk.PhotoImage(Image.open(r"image_s.png")) 
        self.canvas_img=Canvas(self.win2,height=100,width=436,bg="snow2",highlightbackground = "light salmon")
        self.canvas_img.create_image(0,0,image=self.img,anchor="nw")
        self.canvas_img.pack(side="top")
        self.canvas_resultat=Canvas(self.win2,height=10,bg="snow2",highlightbackground = "snow2")
        self.canvas_resultat.pack(pady=10,padx=25,side="bottom")
        
        
        self.canvas=Canvas(self.win2,background="snow2")
        self.canvas.pack(pady=2,padx=25,side="left")
        
        self.canvas_bouton=Canvas(self.win2,bd=0,bg="snow2",highlightbackground = "snow2")
        self.canvas_bouton.pack(pady=2,padx=25,side="left")
        # Ajout des boutons     
        self.button_supprimer=Button(self.canvas_bouton,text="Supprimer",bd=4,command=self.supprimer)
        self.button_supprimer.pack(pady=15,padx=5,ipadx=20,side="top")
        self.button_evaluer=Button(self.canvas_bouton,text="Évaluer",bd=4,command=self.evaluer)
        self.button_evaluer.pack(pady=15,padx=5,ipadx=20,side="top")
        self.button_terminer=Button(self.canvas_bouton,text="Terminer",bd=4,command=self.terminer)
        self.button_terminer.pack(pady=15,padx=5,ipadx=20,side="top")
        self.button_quitter=Button(self.canvas_bouton,text="Quitter",bd=4,command=lambda:[self.win2.destroy() ])
        self.button_quitter.pack(pady=15,ipadx=20,side="top")
        self.text=Text(self.canvas_resultat,height=10,bd=3,highlightbackground = "snow2")
        
        # Instancier la classe Sudoku(Matrice) avec l’état choisi pas l’utilisateur et générer une matrice
        self.s=Sudoku(self.complexite)
        self.s.generer_matrice()
        
        # Afficher à la console le niveau de complexité 
        print("niveau de complexité  :",self.complexite)
        
        # Afficher les valeurs de la matrice générée à l’interface et remplacer les 0 par des espaces vides.
        for i in range (9):
           self.entry=[]
           for j in range (9):
              e=Entry(self.canvas,width=3,highlightthickness=1,highlightbackground = "grey62",justify="center",font=("Times New Roman", 13))
              self.entry.append(e)
              e.grid(row=i,column=j,ipady=2)
              if self.s.matrice_tuiles[i][j].valeur==0:
                  e.insert("end","")
              else:
                  e.insert("end",self.s.matrice_tuiles[i][j].valeur) 
                  e.config(state=DISABLED,disabledbackground="snow2",disabledforeground="black")
          
           self.entries.append(self.entry)
       

        self.win2.mainloop()

    # On cliquant sur le bouton évaluer cette fonction va permettre de comparer les valeurs entrées par l’utilisateur avec les valeurs de la matrice
    #  solution si les valeurs sont égales ils vont s’afficher en vert sinon elles vont s’afficher en rouge

    def evaluer(self):
            for i in range(9):
                for j in range(9):
               
                    if self.s.matrice_tuiles[i][j].valeur==0:
                       
                        if self.entries[i][j].get() =="":
                           
                           self.entries[i][j].config(fg='black')
                        elif self.entries[i][j].get() == str(self.s.matrice_solution[i][j].valeur):
                          
                           self.entries[i][j].config(fg='green')
                        else :
                          
                            self.entries[i][j].config(fg='red')
                
    # On cliquant sur le bouton terminer cette fonction va permettre de comparer les valeurs entrées par l’utilisateur 
    # avec les valeurs de la matrice solution, afficher le résultat et afficher succès ou échec et les erreurs.
        
    def terminer(self)  :
        self.text.pack(pady=10,padx=25,side="bottom")
        
        self.succes=True 

        for i in range (9):
            for j in range(9):
                 if self.entries[i][j].get() != str(self.s.matrice_solution[i][j].valeur) or self.entries[i][j].get() =="":
                    self.succes=False
        
        if  self.succes==False :
            self.text.tag_config("echec", background="yellow", foreground="red")
            self.text.insert("end","----------------------ECHEC--------------------","echec") 
            
            for i in range(9):
                for j in range(9):
                    
                    if self.entries[i][j].get() != str(self.s.matrice_solution[i][j].valeur) or self.entries[i][j].get() =="":
                        print("Erreur à la ligne "+str(i+1)+", colonne "+str(j+1)+":"+self.entries[i][j].get()+"-->"+str( self.s.matrice_solution[i][j].valeur)+" ✓")
                        self.text.insert("end","\nErreur à la ligne "+str(i+1)+", colonne "+str(j+1)+":"+self.entries[i][j].get()+"--> "+str(self.s.matrice_solution[i][j].valeur)+" ✓")
            # Désactiver les boutons Terminer , Évaluer et supprimer à la fin d’une partie  de jeu (Échec ou succès )          
            self.text.config(state="disabled")
            self.button_terminer.config(state="disabled")  
            self.button_evaluer.config(state="disabled") 
            self.button_supprimer.config(state="disabled")  



        else:
            self.text.tag_config("succes", background="white", foreground="green")
            self.text.insert("end","\n**********★*******************★***********","succes") 
            self.text.insert("end","******★********* ★彡[SUCCES]彡★******★******** ","succes") 
            self.text.insert("end","\n**********★********★***************★********** ","succes")  
            self.text.config(state="disabled")
            self.button_terminer.config(state="disabled") 
            self.button_evaluer.config(state="disabled") 
            self.button_supprimer.config(state="disabled") 

        # Afficher les valeurs correctes à l’interface en vert    
        for i in range(9):
            for j in range(9):
                if self.entries[i][j].get() != str(self.s.matrice_solution[i][j].valeur) or self.entries[i][j].get() =="":
                   self.entries[i][j].delete(0,"end")
                   self.entries[i][j].insert("end",self.s.matrice_solution[i][j].valeur)
                   self.entries[i][j].config(fg="green")
                   
              

    # En cliquant sur le bouton supprimer , cette fonction va permettre de supprimer toutes les cases entrées par l’utilisateur  .
    def supprimer(self):
        
        for i in range(9):
            for j in range(9):
                if  self.s.matrice_tuiles[i][j].valeur==0:
                   self.entries[i][j].delete(0,"end")
                   self.entries[i][j].config(fg="black")
        
        
# Classe Tuile : Un objet Tuile représente un composant de la classe Sudoku .
class Tuile:

    def __init__(self,position_l,position_c,valeur):
        self.position_l=position_l
        self.position_c=position_c
        self.valeur=valeur
 

 # La classe Sudoku est composée de 81 (9*9) éléments Tuile

class Sudoku:
    
    def __init__(self,etat):
        self.etat=etat
        self.matrice_tuiles=[]
        self.matrice_solution=[] 
        
        for i in range(9):  
            tuile=[]
            for j in range(9):
                # Initialiser les tuiles avec la valeur 0
                t=Tuile(i,j,0) 
                tuile.append(t)
                # Assigner un nombre aléatoire a la case 0,0 de la Matrice des tuile (Sudoku),
                # Cette action à pour but d’avoir une matrice différente à chaque exécution.
            self.matrice_tuiles.append(tuile)
        self.matrice_tuiles[0][0].valeur=randrange(1,9) 
       
    # Pour générer une matrice il suffit de la résoudre, et après en fonction de niveau de complexité , remplacer des valeurs par des 0.     
    
    def generer_matrice(self):
        self.solution(0,0)
        # Copier la matrice résolue dans matrice solution et remplir la matrice tuiles 
        # de 0 selon l’état de complexité
        self.matrice_solution=deepcopy(self.matrice_tuiles) 


    # Niveau facile : 25 cases vides
        if self.etat==25 :
           compteur=0
           while compteur <self.etat:      
               i=randrange(9)
               j=randrange(9)
               if self.matrice_tuiles[i][j].valeur!=0:
                  self.matrice_tuiles[i][j].valeur=0
                  compteur+=1

            
            
    # Niveau moyen : 40 cases vides      
        elif self.etat==40:
            compteur=0
            while compteur <self.etat :
            
              i=randrange(9)
              j=randrange(9)
              if self.matrice_tuiles[i][j].valeur!=0:
                 self.matrice_tuiles[i][j].valeur=0
                 compteur+=1

    # Niveau Avancé : 55 cases vides 
        elif self.etat==55:
            compteur=0

            while compteur <self.etat :

              i=randrange(9)
              j=randrange(9)
              if self.matrice_tuiles[i][j].valeur!=0:
                 self.matrice_tuiles[i][j].valeur=0
                 compteur+=1

    # Afficher à la console la matrice Qu’on va afficher à l’utilisateur 
        for i in range (len(self.matrice_tuiles)):
        
              for j in range(len(self.matrice_tuiles)):  
                  print(self.matrice_tuiles[i][j].valeur, end=" ")
              print()  
           

    # Fonction permettant de vérifier si on peut assigner à la ligne « ln » et la colonne « cl » le chiffre num         
       
    def possible(self,ln, cl, num):
   
        for i in range(0,9):
          if self.matrice_tuiles[ln][i].valeur == num:
             return False

   
        for i in range(0,9):
            if self.matrice_tuiles[i][cl].valeur == num:
               return False
        # Référence :https://stackoverflow.com/questions/17605898/sudoku-checker-in-python , Auteur : dspyz , Utilise pour identifier
        # les carrés de 3*3 
        x = (cl // 3) * 3 
        y = (ln // 3) * 3  
        for i in range(0,3):
           for j in range(0,3):
              if self.matrice_tuiles[y+i][x+j].valeur == num:
                return False
        return True

    # Fonction permettant de résoudre une matrice (générer une matrice ): inspiré de :https://lvngd.com/blog/generating-and-solving-sudoku-puzzles-python/
    # Auteur : Christina
    
    def solution(self,ln,cl):
        # La matrice est bien remplie si ln=8 et cl=9
        if ln == 8 and cl == 9:
            return True
         
        # Passer à la ligne suivante et remettre cl à zero si cl = 9 (une ligne est bien remplie )
        if cl == 9 :
            ln += 1
            cl = 0

        if self.matrice_tuiles[ln][cl].valeur > 0:
        # Vérifier de manière récursive pour savoir si le fait de placer le nombre choisi dans cette cellule conduira à une solution valide 
            return self.solution( ln, cl + 1)


        for num in range(1, 10):
            # Vérifier si num peut aller dans la cellule, et s'il est valide (pas déjà dans la même ligne/colonne/carre de 3*3).
            if self.possible(ln,cl, num):
               self.matrice_tuiles[ln][cl].valeur = num
               if self.solution(ln,cl+1):
                  return True
               # Sinon remettre la cellule à zero et essayer le choix de nombre suivant.           
                          
               self.matrice_tuiles[ln][cl].valeur = 0
        
        return False
     

   
Interface_utilisateur()  