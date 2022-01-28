class Produit:
    def __init__(self, id, caracteristique, prix, nom):
        self.__id = id
        self.__caracteristique = caracteristique
        self.__prix = prix
        self.__nom = nom


    #set
    def set_caracteristique(self,new):
        self.__caracteristique = new

    def set_nom(self,new):
        self.__nom = new

    def set_prix(self,new):
        self.__prix = new


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

    