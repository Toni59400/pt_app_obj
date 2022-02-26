from lib2to3.pytree import LeafPattern
from select import select
from tkinter import *
from utilisateur import *
from tkinter import messagebox
from cProfile import label
from cgitb import text
from dbconnection import * 
from client import *
from rdv import *
from produit import * 


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
lst_produit = []

data_produit = cursor.execute("SELECT * FROM PRODUIT")
for row in data_produit : 
    id = row["id_produit"]
    nom = row["nom"]
    prix = row["prix"]
    caracteristique = row["caracteristique"]
    tmp_prod = Produit(id, caracteristique, prix, nom)
    lst_produit.append(tmp_prod)

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

lst_rdv = [] 
data_rdv = cursor.execute("SELECT * FROM RDV")
for row2 in data_rdv : 
    id_rdv = row2['id_rdv']
    date = row2['dateHeure']
    com_avant = row2['commentaireAvant']
    com_apres = row2['commentaireApres']
    prosp = int(row2['id_prospect'])
    produit = int(row2['id_prod'])
    tmp2 = Rdv(id_rdv, date, com_avant, com_apres, prosp, produit)
    lst_rdv.append(tmp2)
    
lst_all_prospect = lst_propect_mor + lst_propect_phy
# -------------------------------------------__  CONNEXION AUTHENTIFIER, AFFICHAGE DES CLIENTS (prospect)  __------------------------------------------------- 

phy = False
mor = False
 
def valider() : 
    e1.grid_forget()
    e2.grid_forget()
    identifiant.grid_forget()
    mdp.grid_forget()
    submit.grid_forget()
    exit.grid_forget()
    root.title("Prospects")
    root.resizable(False, False)
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
        tmp_id.grid(column=6, row=count+4)
    
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
        tmp_id.grid(column=6, row=count+4)


    def add_phy() : 
        nom = e_nom.get()
        prenom = e_prenom.get()
        adresse = e_adresse.get()
        cp = e_cp.get()
        ville = e_ville.get()
        if nom == "" or prenom == "" or adresse == "" or cp == "" or ville == "" : 
            messagebox.showinfo("Erreur dans l'ajout", "Le prospect n'a pas pu être ajouté à la base de donnée. Tous les champs ne sont pas remplis.")
        else : 
            reponse = messagebox.askokcancel("Ajout d'un prospect", "Voulez vous vraiment ajouter le prospect ?")
            if reponse : 
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
        if nom == "" or adresse == "" or cp == "" or ville == "" or siret == "" : 
            messagebox.showinfo("Erreur dans l'ajout", "Le prospect n'a pas pu être ajouté à la base de donnée. Tous les champs ne sont pas remplis.")
        else : 
            reponse = messagebox.askokcancel("Ajout d'un prospect", "Voulez vous vraiment ajouter le prospect ?")
            if reponse : 
                try : 
                    t = (nom, siret, adresse, cp, ville)
                    cursor.execute("INSERT INTO PROSPECT (nom, prenom, numSiret, adressePostale, codePostal, ville) values ( ? , '' , ? , ? , ? , ?)", t)
                    connection.commit()
                    messagebox.showinfo("Ajout", "Le prospect moral vient d'être ajouté.")
                except : 
                    messagebox.showinfo("Erreur dans l'ajout", "Le prospect n'a pas pu être ajouté à la base de donnée.")



    l_phy = Label(root, text="Ajout d'un prospect Physique", width=25, height=1, borderwidth=3, relief="groove", bg="#B4BBC4")
    l_mor = Label(root, text="Ajout d'un prospect Moral", width=25, height=1, borderwidth=3, relief="groove", bg="#B4BBC4")
    l_quest = Label(root, text="Ajouter un prospect Physique ? ", width=26, height=1, borderwidth=3, relief="groove", bg="#B4BBC4")
    l_nom = Label(root, text="Nom : ", width=13, height=1, borderwidth=3, relief="groove", bg="#B4BBC4")
    e_nom = Entry(root)
    l_prenom = Label(root, text="Prenom : ", width=13, height=1, borderwidth=3, relief="groove", bg="#B4BBC4")
    e_prenom = Entry(root)
    l_siret = Label(root, text="Siret : ", width=13, height=1, borderwidth=3, relief="groove", bg="#B4BBC4")
    e_siret = Entry(root)
    l_adresse = Label(root, text="Adresse : ", width=13, height=1, borderwidth=3, relief="groove", bg="#B4BBC4")
    e_adresse = Entry(root)
    l_ville = Label(root, text="Ville : ", width=13, height=1, borderwidth=3, relief="groove", bg="#B4BBC4")
    e_ville = Entry(root)
    l_cp = Label(root, text="Code Postal : ", width=13, height=1, borderwidth=3, relief="groove", bg="#B4BBC4")
    e_cp = Entry(root)
    btn_add_phy = Button(root, text='Ajouter', command=add_phy)
    btn_add_mor = Button(root, text="Ajouter", command=add_mor)

    l_espace = Label(root)
    l_espace.grid(row=1, rowspan=2)





    def prospect_phy():
        global mor, phy
        phy = True
        if mor==True:
            mor = False
            l_siret.grid_forget()
            e_siret.grid_forget()
            l_mor.grid_forget()
            btn_add_mor.grid_forget()
        l_phy.grid(row=3, column=7)
        l_nom.grid(row=3+1, column=7)
        e_nom.grid(row=3+1, column=8)
        l_prenom.grid(row=4+1, column=7)
        e_prenom.grid(row=4+1, column=8)
        l_adresse.grid(row=5+1, column=7)
        e_adresse.grid(row=5+1, column=8)
        l_ville.grid(row=6+1, column=7)
        e_ville.grid(row=6+1, column=8)
        l_cp.grid(row=7+1, column=7)
        e_cp.grid(row=7+1, column=8)
        btn_add_phy.grid(row=9, columnspan=2, column=7)
        for i in range (7) : 
            tmp_id.grid(column=9, row=i+3)

    def prospect_mor():
        global mor, phy
        mor = True
        if phy==True:
            phy = False
            l_nom.grid_forget()
            e_nom.grid_forget()
            l_prenom.grid_forget()
            e_prenom.grid_forget()
            l_phy.grid_forget()
            btn_add_phy.grid_forget()
        l_mor.grid(row=3, column=7)
        l_nom.grid(row=3+1, column=7)
        e_nom.grid(row=3+1, column=8)
        l_siret.grid(row=4+1, column=7)
        e_siret.grid(row=4+1, column=8)
        l_adresse.grid(row=5+1, column=7)
        e_adresse.grid(row=5+1, column=8)
        l_ville.grid(row=6+1, column=7)
        e_ville.grid(row=6+1, column=8)
        l_cp.grid(row=7+1, column=7)
        e_cp.grid(row=7+1, column=8)
        btn_add_mor.grid(row=9, columnspan=2, column=7)
        for i in range (7) : 
            tmp_id.grid(column=9, row=i+3, columnspan=2)


    liste_client = Listbox(root, exportselection=0)
    c_cli = 0
    for cli in lst_all_prospect : 
        c_cli += 1
        who = (cli.get_nom() + " " + cli.get_prenom() + "#" + str(cli.get_id())).title()
        liste_client.insert(c_cli, who)


    liste_produit = Listbox(root, exportselection=0)
    c_prod = 0
    for prod in lst_produit : 
        c_prod += 1 
        produit = (prod.get_nom() + " #" + str(prod.get_id())).title()
        liste_produit.insert(c_prod, produit)


    
    l_commentaire_avant = Label(root,  text="Commantaire : ", width=13, height=1, borderwidth=3, relief="groove", bg="#B4BBC4")
    l_date_rdv = Label(root,  text="Date : ", width=13, height=1, borderwidth=3, relief="groove", bg="#B4BBC4")
    e_commentaire_avant = Entry(root, width=20)
    e_date_add = Entry(root)
    frame_btn_rdv = Frame(root)
    l_ajout_rdv = Label(root, text="Ajout d'un rendez-vous : ")
    


    def rm_add_rdv() : 
        liste_client.grid_forget()
        liste_produit.grid_forget()
        l_commentaire_avant.grid_forget()
        l_date_rdv.grid_forget()
        e_commentaire_avant.grid_forget()
        e_date_add.grid_forget()
        btn_annul_add_rdv.grid_forget()
        btn_add_rdv_confirm.grid_forget()
        l_ajout_rdv.grid_forget()

    def add_rdv_to_bdd() : 
        if e_commentaire_avant.get() == "" or e_date_add.get() == "" : 
            messagebox.showinfo("Erreur dans l'ajout", "Il manque des informations pour ajouter le rendez-vous.")
        else : 
            reponse = messagebox.askokcancel("Ajout du rendez-vous", "Voulez vous vraiment ajouter le rendez-vous ?")
            
            if reponse : 
                id_prospect_add_rdv = "".join(liste_client.get(ANCHOR)).split("#")[-1]
                id_produit_add_rdv = "".join(liste_produit.get(ANCHOR)).split("#")[-1]
                t_add_rdv = (e_date_add.get(), e_commentaire_avant.get(), id_prospect_add_rdv, id_produit_add_rdv)
                cursor.execute("INSERT INTO RDV (dateHeure, commentaireAvant, commentaireApres, id_prospect, id_prod) values ( ? , ? , '' , ? , ?)", t_add_rdv)
                connection.commit()
                messagebox.showinfo("Ajouter avec succès", "Le rendez-vous a été ajouter avec succès.")

    btn_annul_add_rdv = Button(frame_btn_rdv, text="Annuler", command=rm_add_rdv)
    btn_add_rdv_confirm = Button(frame_btn_rdv, text="Ajouter", command=add_rdv_to_bdd)


    def add_comm_to_bdd() : 
        if e_commentaire_apres_rdv.get() == "" : 
            messagebox.showinfo("Erreur dans l'ajout du commentaire", "Il manque des informations pour ajouter le commentaire d'apres rendez-vous.")
        else : 
            res = messagebox.askokcancel("Ajout du commentaire", "Voulez vous vraiment ajouter le commentaire ?")
            if res : 
                id_rdv = "".join(lst_rdv_for_add_comm.get(ANCHOR)).split("#")[-1]
                commentaire = e_commentaire_apres_rdv.get()
                sql = (commentaire, id_rdv)
                cursor.execute("UPDATE RDV SET commentaireApres = ? where id_rdv = ?", sql)
                connection.commit()
                messagebox.showinfo("Ajouter avec succès", "Le commentaire d'après rendez-vous a été ajouter avec succès.")

    l_commentaire_apres_rdv = Label(root, text="Entrez un commentaire d'apres rendez-vous :", width=40, height=1, borderwidth=3, relief="groove", bg="#B4BBC4")
    e_commentaire_apres_rdv = Entry(root, width=25)
    btn_valider_comm_apres_rdv = Button(root, text="Ajouter le commentaire", command=add_comm_to_bdd)
    lst_rdv_for_add_comm = Listbox(root, exportselection=0)
    compteur_rdv = 0
    for rdv2 in lst_rdv : 
        compteur_rdv += 1
        rdv = "#" + str(rdv2.get_id()) 
        lst_rdv_for_add_comm.insert(compteur_rdv, rdv)

    ### pour ajouter un rdv
    def add_rdv() : 
        liste_client.grid(row=0+1, column=13)
        liste_produit.grid(row=1, column=12)
        l_commentaire_avant.grid(row=1+1, column=12)
        l_date_rdv.grid(row=2+1, column=12)
        e_commentaire_avant.grid(row=1+1, column=13)
        e_date_add.grid(row=2+1, column=13)
        btn_annul_add_rdv.grid(row=0, column=0)
        btn_add_rdv_confirm.grid(row=0, column=1)
        frame_btn_rdv.grid(row=3+1, column=12, columnspan=2)
        l_ajout_rdv.grid(row=0, column=12, columnspan=2)




    def add_comm_apres_rdv_consult() : 
        l_commentaire_apres_rdv.grid(row=5, column=12)
        lst_rdv_for_add_comm.grid(row=6, column=12)
        e_commentaire_apres_rdv.grid(row=7, column=12, ipady=15)
        btn_valider_comm_apres_rdv.grid(row=8, column=12)


        



    btn_oui = Radiobutton(root, text="Oui", command=prospect_phy)
    btn_non = Radiobutton(root, text="Non", command=prospect_mor)

    l_quest.grid(row=0, column=7)
    btn_non.grid(row=0, column=8)
    btn_oui.grid(row=0, column=9)
    tmp_id.grid(row=0, column=10)


    # pour les rendez vous : 
    btn_add_com_apres_rdv = Button(root, text="Commenter le rendez vous", width=25, height=1, borderwidth=3, relief="groove", bg="#747e8b", command=add_comm_apres_rdv_consult)
    btn_add_rdv = Button(root, text="Ajouter un rendez-vous", width=25, height=1, borderwidth=3, relief="groove", bg="#747e8b", command=add_rdv)
    l_rdv = Label(root, text="Liste des rendez-vous : " , width=25, height=1, borderwidth=3, relief="groove", bg="#B4BBC4")

    tmp_id.grid(row=10, column=7)
    btn_add_rdv.grid(row=11, column=7)
    btn_add_com_apres_rdv.grid(row=12, column=7)
    l_rdv.grid(row=13, column=7)

    f_rdv = Frame(root)

    l_date = Label(f_rdv, text="Date",  width=13, height=1, borderwidth=3, relief="groove", bg="#747e8b")
    l_com_avant = Label(f_rdv, text="Commentaire",  width=13, height=1, borderwidth=3, relief="groove", bg="#747e8b")
    l_com_apres = Label(f_rdv, text="Com Apres RDV",  width=13, height=1, borderwidth=3, relief="groove", bg="#747e8b")
    l_prosp = Label(f_rdv, text="Prospect",  width=13, height=1, borderwidth=3, relief="groove", bg="#747e8b")
    l_produit = Label(f_rdv, text="Produit",  width=13, height=1, borderwidth=3, relief="groove", bg="#747e8b")

    f_rdv.grid(row=14, column=7)
    l_date.grid(row=0, column=0)
    l_com_avant.grid(row=0, column=1)
    l_com_apres.grid(row=0, column=2)
    l_prosp.grid(row=0, column=3)
    l_produit.grid(row=0, column=4)

    count2 = 0
    print(lst_rdv)
    for rdv in lst_rdv : 
        count2+=1
        if count2 % 2 == 0 : 
            tmp_date = Label(f_rdv, text= "# " + rdv.get_id() + rdv.get_date(), width=13, height=1, borderwidth=3, relief="groove", bg="#B4BBC4")
            tmp_com = Label(f_rdv, text= rdv.get_com_avant(),   width=13, height=1, borderwidth=3, relief="groove", bg="#B4BBC4")
            tmp_com_apres = Label(f_rdv, text= rdv.get_com_apres(),  width=13, height=1, borderwidth=3, relief="groove", bg="#B4BBC4")
            tmp_prosp = Label(f_rdv, text= rdv.get_prosp(), width=13, height=1, borderwidth=3, relief="groove", bg="#B4BBC4")
            tmp_prod = Label(f_rdv, text=rdv.get_produit(),  width=13, height=1, borderwidth=3, relief="groove", bg="#B4BBC4")
        else : 
            tmp_date = Label(f_rdv, text= rdv.get_date(), width=13, height=1, borderwidth=3, relief="groove")
            tmp_com = Label(f_rdv, text= rdv.get_com_avant(),   width=13, height=1, borderwidth=3, relief="groove")
            tmp_com_apres = Label(f_rdv, text= rdv.get_com_apres(),  width=13, height=1, borderwidth=3, relief="groove")
            tmp_prosp = Label(f_rdv, text= rdv.get_prosp(), width=13, height=1, borderwidth=3, relief="groove")
            tmp_prod = Label(f_rdv, text=rdv.get_produit(),  width=13, height=1, borderwidth=3, relief="groove")

        tmp_date.grid(row=count2 , column=0)
        tmp_com.grid(row=count2 , column=1)
        tmp_com_apres.grid(row=count2 , column=2)
        tmp_prosp.grid(row=count2 , column=3)
        tmp_prod.grid(row=count2, column=4)

root.mainloop()
connection.close()