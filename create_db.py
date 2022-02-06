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

"""
#insertion des donnes dans la bdd
prenom = ["","","","valentin","kelian","julien","antoine","floria"]
nom = ["pira","danco","neuville","quide","lenglet","toussaint","marechal","meresse"]
siret = ["98889998", "899988888", "8999999987453", "","","","",""]
adresse = ["1 rue john doe","2 rue john doe","3 rue john doe","4 rue john doe","5 rue john doe","6 rue john doe","7 rue john doe","8 rue john doe"]
cp = ["62000","62000","59400","59161","59400","59000","62000","59161"]
ville = ["Arras","Arras","Cambrai","Escaudoeuvres","Cambrai","Lille","Arras","Cagnoncles"]

for i in range(8) : 
    cursor.execute("INSERT INTO PROSPECT(nom, prenom, numSiret, adressePostale, codePostal, ville) VALUES (?, ?, ?,?, ?, ?)", (prenom[i], nom[i], siret[i], adresse[i], cp[i], ville[i]))
    connection.commit()
    print("ok {}".format(i))
"""




'''
lst_propect = []
# RECUPERER LES DATA DE LA BDD ET LES TRANSFORMER EN OBJ ET METTRE CES OBJ DANS UNE LISTE D'OBJ

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
    lst_propect.append(tmp)

'''

data= cursor.execute("SELECT * FROM RDV")
for row in data : 
    print("g")


