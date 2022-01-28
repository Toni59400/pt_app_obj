from dbconnection import * 

class Produit:
    def __init__(self, id, caracteristique, prix, nom):
        self.__id = id
        self.__caracteristique = caracteristique
        self.__prix = prix
        self.__nom = nom


    #set
    def set_caracteristique(self,new):
        self.__caracteristique = new
        self.maj_data()
        
    def set_nom(self,new):
        self.__nom = new
        self.maj_data()

    def set_prix(self,new):
        self.__prix = new
        self.maj_data()


    #get
    def get_caracteristique(self):
        return self.__caracteristique
    
    def get_nom(self):
        return self.__nom

    def get_prix(self):
        return self.__prix

    #afficher
    def afficher(self):
        return "Le produit {0} est {1} au prix de {2}€".format(self.__nom,self.__caracteristique,self.__prix)

    #maj
    def maj_data(self) :
        cursor.execute("UPDATE PRODUIT set nom = ? , caracteristique = ? , prix = ? WHERE id_produit = ?", self.__nom, self.__caracteristique, self.__prix, self.__id)
        connection.commit()