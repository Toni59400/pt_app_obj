from cProfile import label
from cgitb import text
from dbconnection import * 
from tkinter import * 
from client import *

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
    

# -------------------------------------------------------------------------------------------- 

root_client = Tk()
root_client.title("Prospects")
root_client.geometry("800x700")
root_client.resizable(False, False)
menu_ = Menu(root_client, tearoff=0)
menu_.add_command(label="Ajouter Prospect")
menu_.add_command(label="Rendez-vous")
root_client.config(menu=menu_)
l_id = Label(root_client, text="",  width=13, height=1, borderwidth=3)
l_nom = Label(root_client, text="Nom",  width=13, height=1, borderwidth=3, relief="groove",  bg="#747e8b")
l_prenom = Label(root_client, text="Prenom",  width=13, height=1, borderwidth=3, relief="groove", bg="#747e8b")
l_siret = Label(root_client, text="Siret",  width=13, height=1, borderwidth=3, relief="groove", bg="#747e8b")
l_adresse = Label(root_client, text="Adresse",  width=13, height=1, borderwidth=3, relief="groove", bg="#747e8b")
l_cp = Label(root_client, text="Code Postal",  width=13, height=1, borderwidth=3, relief="groove", bg="#747e8b")
l_ville = Label(root_client, text="Ville",  width=13, height=1, borderwidth=3, relief="groove", bg="#747e8b")
l_physique = Label(root_client, text="Clients Physiques",  width=13, height=1, borderwidth=3, relief="groove", bg="#747e8b")
l_moral = Label(root_client, text="Clients moraux",  width=13, height=1, borderwidth=3, relief="groove", bg="#747e8b")
l_adresse2 = Label(root_client, text="Adresse",  width=13, height=1, borderwidth=3, relief="groove", bg="#747e8b")
l_cp2 = Label(root_client, text="Code Postal",  width=13, height=1, borderwidth=3, relief="groove", bg="#747e8b")
l_ville2 = Label(root_client, text="Ville",  width=13, height=1, borderwidth=3, relief="groove", bg="#747e8b")
l_id2 = Label(root_client, text="",  width=13, height=1, borderwidth=3)
l_nom2 = Label(root_client, text="Nom",  width=13, height=1, borderwidth=3, relief="groove", bg="#747e8b")




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
        tmp_id = Label(root_client, text="",  width=13, height=1, borderwidth=3)
        tmp_nom = Label(root_client, text=i.get_nom(),  width=13, height=1, borderwidth=3, relief="groove", bg="#B4BBC4")
        tmp_prenom = Label(root_client, text=i.get_prenom(),  width=13, height=1, borderwidth=3, relief="groove", bg="#B4BBC4")
        tmp_adresse = Label(root_client, text=i.get_adresse(),  width=13, height=1, borderwidth=3, relief="groove", bg="#B4BBC4")
        tmp_cp = Label(root_client, text=i.get_codePostal(),  width=13, height=1, borderwidth=3, relief="groove", bg="#B4BBC4")
        tmp_ville = Label(root_client, text=i.get_ville(),  width=13, height=1, borderwidth=3, relief="groove", bg="#B4BBC4")
    else : 
        tmp_id = Label(root_client, text="",  width=13, height=1, borderwidth=3)
        tmp_nom = Label(root_client, text=i.get_nom(),  width=13, height=1, borderwidth=3, relief="groove")
        tmp_prenom = Label(root_client, text=i.get_prenom(),  width=13, height=1, borderwidth=3, relief="groove")
        tmp_adresse = Label(root_client, text=i.get_adresse(),  width=13, height=1, borderwidth=3, relief="groove")
        tmp_cp = Label(root_client, text=i.get_codePostal(),  width=13, height=1, borderwidth=3, relief="groove")
        tmp_ville = Label(root_client, text=i.get_ville(),  width=13, height=1, borderwidth=3, relief="groove")

    tmp_id.grid(column=0, row=count+1)
    tmp_nom.grid(column= 1,row=count+1)
    tmp_prenom.grid(column= 2,row=count+1)
    tmp_adresse.grid(column= 3,row=count+1)
    tmp_cp.grid(column= 4,row=count+1)
    tmp_ville.grid(column= 5,row=count+1)
    
label_pass_ligne = Label(root_client, text = "").grid(column=0, columnspan=6, row=count+2)
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
        tmp_id = Label(root_client, text="",  width=13, height=1, borderwidth=3)
        tmp_nom = Label(root_client, text=j.get_nom(),  width=13, height=1, borderwidth=3, relief="groove")
        tmp_siret = Label(root_client, text=j.get_numSiret(),  width=13, height=1, borderwidth=3, relief="groove")
        tmp_adresse = Label(root_client, text=j.get_adresse(),  width=13, height=1, borderwidth=3, relief="groove")
        tmp_cp = Label(root_client, text=j.get_codePostal(),  width=13, height=1, borderwidth=3, relief="groove")
        tmp_ville = Label(root_client, text=j.get_ville(),  width=13, height=1, borderwidth=3, relief="groove")
    else : 
        tmp_id = Label(root_client, text="",  width=13, height=1, borderwidth=3)
        tmp_nom = Label(root_client, text=j.get_nom(),  width=13, height=1, borderwidth=3, relief="groove", bg="#B4BBC4")
        tmp_siret = Label(root_client, text=j.get_numSiret(),  width=13, height=1, borderwidth=3, relief="groove", bg="#B4BBC4")
        tmp_adresse = Label(root_client, text=j.get_adresse(),  width=13, height=1, borderwidth=3, relief="groove", bg="#B4BBC4")
        tmp_cp = Label(root_client, text=j.get_codePostal(),  width=13, height=1, borderwidth=3, relief="groove", bg="#B4BBC4")
        tmp_ville = Label(root_client, text=j.get_ville(),  width=13, height=1, borderwidth=3, relief="groove", bg="#B4BBC4")

    tmp_id.grid(column=0, row=count+4)
    tmp_nom.grid(column= 1,row=count+4)
    tmp_siret.grid(column= 2,row=count+4)
    tmp_adresse.grid(column= 3,row=count+4)
    tmp_cp.grid(column= 4,row=count+4)
    tmp_ville.grid(column= 5,row=count+4)



root_client.mainloop()