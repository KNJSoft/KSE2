import re
import sqlite3
from hashlib import sha512
from subprocess import call
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename

user=sqlite3.connect("note_eleve.db")
User=user.cursor()
User.execute(" create table if not exists utilisateur(username varchar(20) primary key not null,password varchar(100) not null,ets varchar(50) not null,logo blob);")
def connection():
    root.destroy()
    call(['python','main.py'])
def inscription():
    usersname = userenter.get()
    usermdp = mdpenter.get()
    ets=etsenter.get()
    #table d'users

    u = User.execute("select * from utilisateur")
    l = 0
    for i in u:
        if usersname == i[0]:
            l = 1
            break
        else:
            l = 0

    if len(usersname)<4:
        messagebox.showwarning("Note d'information","Le Nom d'utilisateur doit avoir au moins quatre caractères")
        userenter.delete("0", "end")
    elif len(usermdp)<8:
        messagebox.showwarning("Note d'information", "Le mot de passe doit avoir au moins huit caractères")
        mdpenter.delete("0", "end")
    elif(l==1):
        messagebox.showwarning("Note d'information", "Ce Nom d'utilisateur existe déjà")
        userenter.delete("0", "end")
        mdpenter.delete("0", "end")

    else:
        usermdp=sha512(usermdp.encode('utf-8')).digest()
        val=(usersname,usermdp,ets,img)
        user.execute("insert into utilisateur(username,password,ets,logo) values(?,?,?,?)",val)
        user.commit()
        user.close()
        messagebox.showinfo("Note d'information", "Votre compte a été créer avec succes")
        root.destroy()
        call(["python", "main.py"])
""""""
root=Tk()
root.title("FENÊTRE D'INSCRIPTION")
root.configure(background="#091821")
root.geometry("400x400+450+200")
root.resizable(False,False)
titre=Label(root,borderwidth=3,relief=SUNKEN
            ,text="Formulaire d'inscription",font=("sans serif",23),background="#091821",fg="white")
titre.place(x=0,y=0,width=400)
#user
username=Label(root,text="Nom d'utilisateur:",font=("Arial",14),bg="#091821",fg="white")
username.place(x=5,y=100,width=150)
userenter=Entry(root,bd=5,font=("Arial",13))
userenter.place(x=150,y=100,width=200,height=30)
#mot de passe
mdp=Label(root,text="Mot de passe:",font=("Arial",14),bg="#091821",fg="white")
mdp.place(x=5,y=150,width=150)
mdpenter=Entry(root,show="*",bd=5,font=("Arial",13))
mdpenter.place(x=150,y=150,width=200,height=30)
#ets
etsname=Label(root,text="Nom de Ets:",font=("Arial",14),bg="#091821",fg="white")
etsname.place(x=5,y=200,width=150)
etsenter=Entry(root,bd=5,font=("Arial",13))
etsenter.place(x=150,y=200,width=200,height=30)
#logo
logoname=Label(root,text="Logo:",font=("Arial",14),bg="#091821",fg="white")
logoname.place(x=5,y=250,width=150)
logoenter=Label(root, text="aucune image selectionnée", font='arial 8 bold', fg="#ff7800", bg="white")

def parcourrir():
    global img
    """"img="/home/knjprod/PycharmProjects/apptkinter/knj.png"""""
    img=askopenfilename(initialdir="/",title="selectionner une image",filetypes=(("png files","*.png"),("jpeg files","*.jpeg")))
    if img:
        logoenter.configure(text=img)
        """User.execute("insert into utilisateur(logo) values(?,?)",img)"""

logoenter.place(x=150,y=250,width=150,height=30)
#bouton parcourrir
btn=Button(root,text="Logo",font=("Arial",16),bg="#FF4500",fg="white",command=parcourrir)
btn.place(x=300,y=250,width=50,height=30)
#bouton d'inscription
btn=Button(root,text="Creer un compte",font=("Arial",16),bg="#FF4500",fg="white",command=inscription)
btn.place(x=150,y=300,width=200)
#bouton de connection
btn=Button(root,text="Connexion",font=("Arial",16),bg="#FF4500",fg="white",command=connection)
btn.place(x=150,y=350,width=200)
#execution
root.mainloop()