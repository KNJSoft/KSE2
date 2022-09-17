#importation
import sqlite3
import tkinter
from cProfile import label
from subprocess import call
from tkinter import *
from tkinter import messagebox
from tkinter import ttk,Tk
# Importation de quelques éléments de la bibliothèque ReportLab :
from reportlab.pdfgen.canvas import Canvas # classe d’objets "canevas"
from reportlab.lib.units import cm # valeur de 1 cm en points pica
from reportlab.lib.pagesizes import A4 # dimensions du format A4

"""import mysql.connector"""#poun l'utilisation de mysql comme base de données

def ajout():
    #recuperation des valeurs
    Matricule=matriculeenter.get()
    Nom=nomenter.get()
    Prenom=prenomenter.get()
    Sexe=sexe.get()
    Classe=classedispo.get()
    Matiere=matiereenter.get()
    Note=noteenter.get()
    #connection a la base de données
    base = sqlite3.connect("note_eleve.db")
    connexion = base.cursor()
    """bd = mysql.connector.connect(host='127.0.0.1', user='root', password='', database='note_eleve')
    connexion = bd.cursor()"""
    #insertion des valeurs si possible
    try:
        sql="insert into note(mat,nom,prenom,sexe,classe,matiere,note) values (?,?,?,?,?,?,?) "
        val=(Matricule,Nom,Prenom,Sexe,Classe,Matiere,Note)
        connexion.execute(sql,val)
        base.commit()
        dernierematricule=connexion.lastrowid
        messagebox.showinfo("information","Note ajouter")
        root.destroy()
        call(['python','page2.py'])
    except Exception as e:
        messagebox.showwarning("information", "Erreur")
        print(e)
        #retour
        base.rollback()
        base.close()
def modifier():
    # recuperation des valeurs
    Matricule = matriculeenter.get()
    Nom = nomenter.get()
    Prenom = prenomenter.get()
    Sexe = sexe.get()
    Classe = classedispo.get()
    Matiere = matiereenter.get()
    Note = noteenter.get()
    # connection a la base de données
    """bd = mysql.connector.connect(host='localhost', user='root', password='', database='note_eleve')
    connexion = bd.cursor()"""
    base = sqlite3.connect("note_eleve.db")
    connexion = base.cursor()
    # mise a jour des valeurs si possible
    try:
        sql="update note set nom=?,prenom=?,sexe=?,classe=?,matiere=?,note=? where mat=?"
        val=(Nom,Prenom,Sexe,Classe,Matiere,Note,Matricule)
        connexion.execute(sql,val)
        base.commit()
        dernierematricule=connexion.lastrowid
        messagebox.showinfo("information","Note modifier")
        root.destroy()
        call(['python','page2.py'])
    except Exception as e:
        messagebox.showwarning("information", "Erreur")
        print(e)
        #retour
        base.rollback()
        base.close()

def supprimer():
    Matricule=matriculeenter.get()
    # connection a la base de données
    #bd = mysql.connector.connect(host='127.0.0.1', user='root', password='', database='note_eleve')
    #connexion = bd.cursor()
    base = sqlite3.connect("note_eleve.db")
    connexion = base.cursor()
    sql = "delete from note where mat=?"
    val = (Matricule,)
    try:
        connexion.execute(sql,val)
        base.commit()
        dernierematricule=connexion.lastrowid
        messagebox.showinfo("information","Note supprimer")
        root.destroy()
        call(['python','page2.py'])
    except Exception as e:
        messagebox.showwarning("information","Erreur")
        print(e)
        #retour
        base.rollback()
        base.close()

root=Tk()
root.title("MENU PRINCIPAL")
root.geometry("1350x700+0+0")
root.resizable(False,False)
root.configure(background="#091821")
#ajout du titre
titre=Label(root,borderwidth=3
            ,text="GESTION NOTES DES ETUDIANTS",font=("sans serif",25),background="#2F4F4F",fg="#FFFAFA")
titre.place(x=0,y=0,width=1350,height=100)
titre1=Label(root,borderwidth=3
            ,text="KSE",font=("sans serif",75),background="#2F4F4F",fg="#FFFAFA")
titre1.place(x=0,y=0,width=350,height=100)
#details des eleves

#matricule
matricule=Label(root,text="MATRICULE",font=("Arial",18),bg="#091821",fg="white")
matricule.place(x=70,y=150,width=150)
matriculeenter=Entry(root,bd=4,font=("Arial",14))
matriculeenter.place(x=250,y=150,width=150)

#Nom
nom=Label(root,text="NOM",font=("Arial",18),bg="#091821",fg="white")
nom.place(x=70,y=200,width=150)
nomenter=Entry(root,bd=4,font=("Arial",14))
nomenter.place(x=250,y=200,width=300)

#Prenom
prenom=Label(root,text="PRENOM",font=("Arial",18),bg="#091821",fg="white")
prenom.place(x=70,y=250,width=150)
prenomenter=Entry(root,bd=4,font=("Arial",14))
prenomenter.place(x=250,y=250,width=300)

#sexe
sexe=StringVar()
sexemas=Radiobutton(root,text="MASCULIN",value="M",variable=sexe,indicatoron=0,font=("Arial",18),bg="#091821",fg="#696969")
sexemas.place(x=250,y=300,width=130)
sexefem=Radiobutton(root,text="FEMININ",value="F",variable=sexe,indicatoron=0,font=("Arial",18),bg="#091821",fg="#696969")
sexefem.place(x=420,y=300,width=130)

#CLASSE
classe=Label(root,text="CLASSE",font=("Arial",18),bg="#091821",fg="white")
classe.place(x=70,y=350,width=150)
classedispo=ttk.Combobox(root,font=("Arial",14))
classedispo['values']=['SIL','CP','CE1','CE2','CM1','CM2','6e','5e','4e','3e','2nd','P','Tle','L1','L2','L3','M1','M2','Autres']
classedispo.place(x=250,y=350,width=130)

#matiere
matiere=Label(root,text="MATIERE",font=("Arial",18),bg="#091821",fg="white")
matiere.place(x=70,y=400,width=150)
matiereenter=Entry(root,bd=4,font=("Arial",14))
matiereenter.place(x=250,y=400,width=300)

#Note
note=Label(root,text="NOTE",font=("Arial",18),bg="#091821",fg="white")
note.place(x=70,y=450,width=150)
noteenter=Entry(root,bd=4,font=("Arial",14))
noteenter.place(x=250,y=450,width=200)

#Enregistrer
enregist=Button(root,text="Enregistrer",font=("Arial",16),bg="#D2691E",fg="white",command=ajout)
enregist.place(x=250,y=500,width=200)

#Modifier
modifier=Button(root,text="Modifier",font=("Arial",16),bg="#D2691E",fg="white",command=modifier)
modifier.place(x=250,y=550,width=200)

#Supprimer
supprimer=Button(root,text="Supprimer",font=("Arial",16),bg="#D2691E",fg="white",command=supprimer)
supprimer.place(x=250,y=600,width=200)

#table
table=ttk.Treeview(root,columns=(1,2,3,4,5,6,7),height=5,show="headings")
table.place(x=560,y=150,width=790,height=650)
#entete
table.heading(1,text="MATRICULE")
table.heading(2,text="NOM")
table.heading(3,text="PRENOM")
table.heading(4,text="SEXE")
table.heading(5,text="CLASSE")
table.heading(6,text="MATIERE")
table.heading(7,text="NOTE")
#dimensions des colonnes
table.column(1,width=75)
table.column(2,width=150)
table.column(3,width=150)
table.column(4,width=100)
table.column(5,width=50)
table.column(6,width=100)
table.column(7,width=50)
#intraction dans les tables
"""bd=mysql.connector.connect(host='127.0.0.1',user='root',password='',database='note_eleve')
connexion=bd.cursor()
connexion.execute("select * from note ")"""
base=sqlite3.connect("note_eleve.db")
connexion=base.cursor()
connexion.execute("create table if not exists note(mat varchar(20) primary key not null,"
                  "nom varchar(20) not null,"
                  "prenom varchar(15) not null,"
                  "sexe char(1) not null,"
                  "classe varchar(15) not null ,"
                  "matiere varchar(20) not null,"
                  "note integer not null);")
us=connexion.execute("select * from utilisateur")
for i in us:
    us=i[3]
    break
logo=us
base.close()
def pdf():
    base = sqlite3.connect("note_eleve.db")
    connexion = base.cursor()
    connexion.execute(
        "create table if not exists note(mat varchar(20) primary key not null,nom varchar(20) not null,prenom varchar(15) not null,sexe char(1) not null,classe varchar(15) not null ,matiere varchar(20) not null,note integer not null);")
    bd = connexion.execute("select * from note order by nom,prenom")
    #configuration du pdf
    # 1) Choix d'un nom de fichier pour le document à produire :
    fichier ="document_1.pdf"
    # 2) Instanciation d'un "objet canevas" Reportlab lié à ce fichier :
    can = Canvas("{0}".format(fichier), pagesize=A4)
    # 3) Installation d'éléments divers dans le canevas :
    texte ="Nom"
    texte2="KOGNOUJU NGOUAGNA JOEL"
    texte3="Prénom"
    sexe="Sexe"
    mat="Matière"
    note="Note"
    # ligne de texte à imprimer
    can.setFont("Times-Roman", 16)
    # choix d'une police de caractères
    x,y=0.1,25 # emplacement sur la feuille
    Y=24.1
    can.drawString(0.1 * cm, Y * cm, "N°")
    can.drawString(3*cm, Y*cm, texte)
    can.drawString(8.1*cm,Y*cm,texte3)
    can.drawString(11.3*cm,Y*cm,sexe)
    can.drawString(14*cm,Y*cm,mat)
    can.drawString(17.8*cm,Y*cm,note)
    can.setFont("Times-Roman", 11)
    #image
    can.drawImage(logo, 8 * cm, 26 * cm,
                  width=5 * cm, height=5 * cm, mask="auto")
    """can.drawString(18.6*cm,27.1*cm,moy)
    can.drawString(posX,27.1*cm,texte2)
    can.drawString(7.1*cm,27.1*cm,texte3)"""
    v,u=0,21
    can.line(v*cm,y*cm,u*cm,y*cm) #hori
    can.line(v*cm,(y-1)*cm,u*cm,(y-1)*cm)#hor
    can.line(v*cm,(y-2)*cm,u*cm,(y-2)*cm)
    can.line(v*cm,y*cm,v*cm,v*cm) #verti
    can.line(1 * cm, y * cm, 1 * cm, 1 * cm)  # verti_nu
    can.line(7*cm,y*cm,7*cm,1*cm) #verti_NOM
    can.line(11*cm,y*cm,11*cm,1*cm) #verti_preNOM
    can.line(12.5*cm,y*cm,12.5*cm,1*cm) #verti_sexe
    can.line(17.5*cm,y*cm,17.5*cm,1*cm) #verti_mat
    can.line(19*cm,y*cm,19*cm,1*cm) #verti_note
    can.line(12.5 * cm, y * cm, 12.5 * cm, 1 * cm)  # verti_vide
    can.line(21*cm,y*cm,21*cm,1*cm)
    j=22
    while j>0:
        can.line(v * cm, j * cm, u * cm, j * cm)
        j-=1
    """can.showPage()
    can.drawString(posX*3, posY, texte)"""
    """a=can.getPageNumber()
    print(a)"""
    # dessin du texte dans le canevas
    o=0.1
    a=2.1
    b=7.1
    c=11.1
    d=12.6
    e=17.6
    h=23.1
    i=1
    for z in bd:
        Nom=z[1]
        Prenom=z[2]
        SexeP=z[3]
        Mat=z[5]
        Note=z[6]
        can.drawString(o * cm, h * cm, str(i))
        can.drawString(a*cm, h * cm, Nom)
        can.drawString(b * cm, h * cm, Prenom)
        can.drawString(c * cm, h * cm, SexeP)
        can.drawString(d * cm, h * cm, Mat)
        can.drawString(e * cm, h * cm, str(Note))
        h-=1
        i+=1
    base.close()


    # 4) Sauvegarde du résultat dans le fichier PDF :
    can.save()
base=sqlite3.connect("note_eleve.db")
connexion=base.cursor()
bd = connexion.execute("select * from note order by nom,prenom")
for i in bd:
    table.insert('', END, values=i)
base.close()
#quitter l'application
btn=Button(root,text="Quitter",font=("Arial",16),bg="#ff002f",fg="white",command=root.destroy)
btn.place(x=1100,y=50,width=200)
btnpdf=Button(root,text="Générer pdf",font=("Arial",16),bg="#00deff",fg="white",command=pdf)
btnpdf.place(x=1100,y=650,width=200)
#execution
root.mainloop()