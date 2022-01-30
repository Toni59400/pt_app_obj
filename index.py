from select import select
from tkinter import *
from utilisateur import *
from tkinter import messagebox
from cProfile import label
from cgitb import text
from dbconnection import * 
from client import *

def seConnecter():
    cpt = 0
    user = cursor.execute("SELECT * FROM Utilisateur WHERE identifiant= ?", (e1.get(),))
    connection.commit
    for row in user:
        cpt+=1
    if cpt == 0:
        messagebox.showinfo("Mauvais identifiant", "L'identifiant renseigné n'est pas bon !")
    else : 
        if (e2.get()) == row['mdp'] : 
            valider()
        else : 
            messagebox.showinfo("Mauvais mot de passe", "Le mot de passe renseigné n'est pas bon !")



def quitter():
    connection.close()
    quit()

root = Tk()

root.title("Connection")


identifiant = Label(root, text="Identifiant")
identifiant.grid(row=0, column=0, padx=20, pady=20)
e1 = Entry(root)
e1.grid(row=0, column=1, padx=20, pady=20)
mdp = Label(root, text="Mot de passe")
mdp.grid(row=1, column=0, padx=20, pady=20)
e2 = Entry(root, show="*")
e2.grid(row=1, column=1, padx=20, pady=20)
submit = Button(root, text="Se connecter", command=seConnecter)
submit.grid(row=2, column=0, padx=20, pady=20)
exit = Button(root, text="Quitter", command=quitter)
exit.grid(row=2, column=1, padx=20, pady=20)



# RECUPERER LES DATA DE LA BDD ET LES TRANSFORMER EN OBJ ET METTRE CES OBJ DANS UNE LISTE D'OBJ
lst_propect_phy = []
lst_propect_mor = []
data = cursor.execute("SELECT * FROM PROSPECT")
for row in data : 
    id = row['id_prospect']
    nom = row['nom']
    prenom = row['prenom']
    siret = row['numSiret']
    adresse = row["adressePostale"]
    cp = row["codePostal"]
    ville = row['ville']
    tmp = Client(id, nom, prenom, siret, adresse, cp, ville)
    if prenom == "" : 
        lst_propect_mor.append(tmp)
    else : 
        lst_propect_phy.append(tmp)
    

# -------------------------------------------__  CONNEXION AUTHENTIFIER, AFFICHAGE DES CLIENTS (prospect)  __------------------------------------------------- 


 
def valider() : 
    e1.grid_forget()
    e2.grid_forget()
    identifiant.grid_forget()
    mdp.grid_forget()
    submit.grid_forget()
    exit.grid_forget()
    root.title("Prospects")
    root.geometry("800x700")
    root.resizable(False, False)
    menu_ = Menu(root, tearoff=0)
    menu_.add_command(label="Ajouter Prospect", command=create_new_prospect)
    menu_.add_command(label="Rendez-vous")
    root.config(menu=menu_)
    l_id = Label(root, text="",  width=13, height=1, borderwidth=3)
    l_nom = Label(root, text="Nom",  width=13, height=1, borderwidth=3, relief="groove",  bg="#747e8b")
    l_prenom = Label(root, text="Prenom",  width=13, height=1, borderwidth=3, relief="groove", bg="#747e8b")
    l_siret = Label(root, text="Siret",  width=13, height=1, borderwidth=3, relief="groove", bg="#747e8b")
    l_adresse = Label(root, text="Adresse",  width=13, height=1, borderwidth=3, relief="groove", bg="#747e8b")
    l_cp = Label(root, text="Code Postal",  width=13, height=1, borderwidth=3, relief="groove", bg="#747e8b")
    l_ville = Label(root, text="Ville",  width=13, height=1, borderwidth=3, relief="groove", bg="#747e8b")
    l_physique = Label(root, text="Clients Physiques",  width=13, height=1, borderwidth=3, relief="groove", bg="#747e8b")
    l_moral = Label(root, text="Clients moraux",  width=13, height=1, borderwidth=3, relief="groove", bg="#747e8b")
    l_adresse2 = Label(root, text="Adresse",  width=13, height=1, borderwidth=3, relief="groove", bg="#747e8b")
    l_cp2 = Label(root, text="Code Postal",  width=13, height=1, borderwidth=3, relief="groove", bg="#747e8b")
    l_ville2 = Label(root, text="Ville",  width=13, height=1, borderwidth=3, relief="groove", bg="#747e8b")
    l_id2 = Label(root, text="",  width=13, height=1, borderwidth=3)
    l_nom2 = Label(root, text="Nom",  width=13, height=1, borderwidth=3, relief="groove", bg="#747e8b")




    l_physique.grid(column=0, row=0, columnspan=6)
    l_id2.grid(column=0, row=1, padx=20)
    l_nom2.grid(column=1, row=1)
    l_prenom.grid(column=2, row=1)
    l_adresse2.grid(column=3, row=1)
    l_cp2.grid(column=4, row=1)
    l_ville2.grid(column=5, row=1)

    count = 0 
    for i in lst_propect_phy : 
        count += 1 
        if count%2 == 0 : 
            tmp_id = Label(root, text="",  width=13, height=1, borderwidth=3)
            tmp_nom = Label(root, text=i.get_nom(),  width=13, height=1, borderwidth=3, relief="groove", bg="#B4BBC4")
            tmp_prenom = Label(root, text=i.get_prenom(),  width=13, height=1, borderwidth=3, relief="groove", bg="#B4BBC4")
            tmp_adresse = Label(root, text=i.get_adresse(),  width=13, height=1, borderwidth=3, relief="groove", bg="#B4BBC4")
            tmp_cp = Label(root, text=i.get_codePostal(),  width=13, height=1, borderwidth=3, relief="groove", bg="#B4BBC4")
            tmp_ville = Label(root, text=i.get_ville(),  width=13, height=1, borderwidth=3, relief="groove", bg="#B4BBC4")
        else : 
            tmp_id = Label(root, text="",  width=13, height=1, borderwidth=3)
            tmp_nom = Label(root, text=i.get_nom(),  width=13, height=1, borderwidth=3, relief="groove")
            tmp_prenom = Label(root, text=i.get_prenom(),  width=13, height=1, borderwidth=3, relief="groove")
            tmp_adresse = Label(root, text=i.get_adresse(),  width=13, height=1, borderwidth=3, relief="groove")
            tmp_cp = Label(root, text=i.get_codePostal(),  width=13, height=1, borderwidth=3, relief="groove")
            tmp_ville = Label(root, text=i.get_ville(),  width=13, height=1, borderwidth=3, relief="groove")

        tmp_id.grid(column=0, row=count+1)
        tmp_nom.grid(column= 1,row=count+1)
        tmp_prenom.grid(column= 2,row=count+1)
        tmp_adresse.grid(column= 3,row=count+1)
        tmp_cp.grid(column= 4,row=count+1)
        tmp_ville.grid(column= 5,row=count+1)
        
    
    l_moral.grid(column=0, row=count+3, columnspan=6)
    l_id.grid(column=0, row=count+4)
    l_nom.grid(column=1, row=count+4)
    l_siret.grid(column=2, row=count+4)
    l_adresse.grid(column=3, row=count+4)
    l_cp.grid(column=4, row=count+4)
    l_ville.grid(column=5, row=count+4)


    
    for j in lst_propect_mor : 
        count += 1 
        if count%2 == 0 : 
            tmp_id = Label(root, text="",  width=13, height=1, borderwidth=3)
            tmp_nom = Label(root, text=j.get_nom(),  width=13, height=1, borderwidth=3, relief="groove")
            tmp_siret = Label(root, text=j.get_numSiret(),  width=13, height=1, borderwidth=3, relief="groove")
            tmp_adresse = Label(root, text=j.get_adresse(),  width=13, height=1, borderwidth=3, relief="groove")
            tmp_cp = Label(root, text=j.get_codePostal(),  width=13, height=1, borderwidth=3, relief="groove")
            tmp_ville = Label(root, text=j.get_ville(),  width=13, height=1, borderwidth=3, relief="groove")
        else : 
            tmp_id = Label(root, text="",  width=13, height=1, borderwidth=3)
            tmp_nom = Label(root, text=j.get_nom(),  width=13, height=1, borderwidth=3, relief="groove", bg="#B4BBC4")
            tmp_siret = Label(root, text=j.get_numSiret(),  width=13, height=1, borderwidth=3, relief="groove", bg="#B4BBC4")
            tmp_adresse = Label(root, text=j.get_adresse(),  width=13, height=1, borderwidth=3, relief="groove", bg="#B4BBC4")
            tmp_cp = Label(root, text=j.get_codePostal(),  width=13, height=1, borderwidth=3, relief="groove", bg="#B4BBC4")
            tmp_ville = Label(root, text=j.get_ville(),  width=13, height=1, borderwidth=3, relief="groove", bg="#B4BBC4")

        tmp_id.grid(column=0, row=count+4)
        tmp_nom.grid(column= 1,row=count+4)
        tmp_siret.grid(column= 2,row=count+4)
        tmp_adresse.grid(column= 3,row=count+4)
        tmp_cp.grid(column= 4,row=count+4)
        tmp_ville.grid(column= 5,row=count+4)


new = Toplevel(root)
def add_phy() : 
    nom = e_nom.get()
    prenom = e_prenom.get()
    adresse = e_adresse.get()
    cp = e_cp.get()
    ville = e_ville.get()
    try : 
        t = (nom, prenom, adresse, cp, ville)
        cursor.execute("INSERT INTO PROSPECT (nom, prenom, numSiret, adressePostale, codePostal, ville) values ( ? , ? , '' , ? , ? , ?)", t)
        connection.commit()
        messagebox.showinfo("Ajout", "Le prospect physique vient d'être ajouté.")
    except : 
        messagebox.showinfo("Erreur dans l'ajout", "Le prospect n'a pas pu être ajouté à la base de donnée.")
    

def add_mor() : 
    nom = e_nom.get()
    adresse = e_adresse.get()
    cp = e_cp.get()
    ville = e_ville.get()
    siret = e_siret.get()
    try : 
        t = (nom, siret, adresse, cp, ville)
        cursor.execute("INSERT INTO PROSPECT (nom, prenom, numSiret, adressePostale, codePostal, ville) values ( ? , '' , ? , ? , ? , ?)", t)
        connection.commit()
        messagebox.showinfo("Ajout", "Le prospect moral vient d'être ajouté.")
    except : 
        messagebox.showinfo("Erreur dans l'ajout", "Le prospect n'a pas pu être ajouté à la base de donnée.")



l_phy = Label(new, text="Ajout d'un prospect Physique")
l_mor = Label(new, text="Ajout d'un prospect Moral")
l_quest = Label(new, text="Prospect Physique ? ")
l_nom = Label(new, text="Nom : ")
e_nom = Entry(new)
l_prenom = Label(new, text="Prenom : ")
e_prenom = Entry(new)
l_siret = Label(new, text="Siret : ")
e_siret = Entry(new)
l_adresse = Label(new, text="Adresse : ")
e_adresse = Entry(new)
l_ville = Label(new, text="Ville : ")
e_ville = Entry(new)
l_cp = Label(new, text="Code Postal : ")
e_cp = Entry(new)
btn_add_phy = Button(new, text='Ajouter', command=add_phy)
btn_add_mor = Button(new, text="Ajouter", command=add_mor)

l_espace = Label(new)
l_espace.grid(row=1, rowspan=2)

phy = False
mor = False



def prospect_phy():
    global mor, phy
    phy = True
    if mor==True:
        mor = False
        l_siret.grid_forget()
        e_siret.grid_forget()
        l_mor.grid_forget()
        btn_add_mor.grid_forget()
    l_phy.grid(row=3)
    l_nom.grid(row=3+1, column=0)
    e_nom.grid(row=3+1, column=1)
    l_prenom.grid(row=4+1, column=0)
    e_prenom.grid(row=4+1, column=1)
    l_adresse.grid(row=5+1, column=0)
    e_adresse.grid(row=5+1, column=1)
    l_ville.grid(row=6+1, column=0)
    e_ville.grid(row=6+1, column=1)
    l_cp.grid(row=7+1, column=0)
    e_cp.grid(row=7+1, column=1)
    btn_add_phy.grid(row=9, columnspan=2)


def prospect_mor():
    global mor, phy
    mor = True
    if phy==True:
        phy = False
        l_nom.grid_forget()
        e_nom.grid_forget()
        l_phy.grid_forget()
        btn_add_phy.grid_forget()
    l_mor.grid(row=3)
    l_nom.grid(row=3+1, column=0)
    e_nom.grid(row=3+1, column=1)
    l_siret.grid(row=4+1, column=0)
    e_siret.grid(row=4+1, column=1)
    l_adresse.grid(row=5+1, column=0)
    e_adresse.grid(row=5+1, column=1) 
    l_ville.grid(row=6+1, column=0)
    e_ville.grid(row=6+1, column=1)
    l_cp.grid(row=7+1, column=0)
    e_cp.grid(row=7+1, column=1)
    btn_add_mor.grid(row=9, columnspan=2)


btn_oui = Radiobutton(new, text="Oui", command=prospect_phy)
btn_non = Radiobutton(new, text="Non", command=prospect_mor)

def create_new_prospect() : 
    new.geometry("800x700")
    new.title("Nouveau Prospect")
    l_quest.grid(row=0, column=0)
    btn_non.grid(row=0, column=1)
    btn_oui.grid(row=0, column=2)





root.mainloop()
connection.close()