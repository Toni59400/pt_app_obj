from dbconnection import * 


try : 
    cursor.execute("CREATE TABLE PROSPECT(id_prospect INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, nom TEXT, prenom TEXT, numSiret TEXT, adressePostale TEXT, codePostal TEXT, ville TEXT)")
    cursor.execute("CREATE TABLE PRODUIT(id_produit INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, nom TEXT, prix TEXT, caracteristique TEXT)")
    cursor.execute("CREATE TABLE RDV(id_rdv INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, dateHeure DATETIME, commentaireAvant TEXT, commentaireApres TEXT, id_prospect INTEGER NOT NULL,  FOREIGN KEY(id_prospect) REFERENCES PROSPECT(id_prospect))")
    cursor.execute("CREATE TABLE UTILISATEUR(id_utilisateur INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, identifiant TEXT, mdp TEXT)")
except : 
    print("DB deja crée, table egalement.")

try : 
    cursor.execute("INSERT INTO UTILISATEUR(identifiant, mdp) VALUES ('toni59400', '123456')")
    connection.commit()
except : 
    print("User non ajouté")