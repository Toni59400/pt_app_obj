from dbconnection import * 
from client import * 


try : 
    cursor.execute("CREATE TABLE PROSPECT(id_prospect INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, nom TEXT, prenom TEXT, numSiret TEXT, adressePostale TEXT, codePostal TEXT, ville TEXT)")
    cursor.execute("CREATE TABLE PRODUIT(id_produit INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, nom TEXT, prix TEXT, caracteristique TEXT)")
    cursor.execute("CREATE TABLE RDV(id_rdv INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, dateHeure DATETIME, commentaireAvant TEXT, commentaireApres TEXT, id_prospect INTEGER NOT NULL,  FOREIGN KEY(id_prospect) REFERENCES PROSPECT(id_prospect))")
    cursor.execute("CREATE TABLE UTILISATEUR(id_utilisateur INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, identifiant TEXT, mdp TEXT)")
except : 
    print("DB deja crée, table egalement.")

try : 
    #cursor.execute("INSERT INTO UTILISATEUR(identifiant, mdp) VALUES ('toni59400', '123456')")
    #cursor.execute("INSERT INTO PROSPECT(nom, prenom, numSiret, adressePostale, codePostal, ville) VALUES ('PIRA', 'Toni', '','60 rue du Temple', '62000', 'Arras')")
    connection.commit()
except : 
    print("User non ajouté")

data = cursor.execute("SELECT * FROM PROSPECT")
for row in data : 
    id = row['id_prospect']
    nom = row['nom']
    prenom = row['prenom']
    siret = row['numSiret']
    adresse = row["adressePostale"]
    cp = row["codePostal"]
    ville = row['ville']

    toni = Client(id, nom, prenom, siret, adresse, cp, ville)

    toni.affiche_client()
    toni.set_adresse('61 rue du Temple')
    toni.affiche_client()

  