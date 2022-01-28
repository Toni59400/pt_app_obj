from dbconnection import * 

class Client() : 
    def __init__(self, id, nom, prenom, numSiret, adressePostale, codePostal, ville) : 
        self.__id = id 
        self.__nom = nom 
        self.__prenom = prenom
        self.__numSiret = numSiret
        self.__adresse = adressePostale
        self.__codePostal = codePostal
        self.__ville = ville 

    '''
    Getteur de la class client
    '''

    def get_id(self) :
        return self.__id
    
    def get_nom(self) : 
        return self.__nom
        
    def get_prenom(self) : 
        return self.__prenom
    
    def get_numSiret(self) : 
        return self.__numSiret

    def get_adresse(self) : 
        return self.__adresse

    def get_codePostal(self) : 
        return self.__codePostal

    def get_ville(self) : 
        return self.__ville

    '''
    Mise à jour des données dans la bd
    '''

    def set_nom(self, new) : 
        self.__nom = new