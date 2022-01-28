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
    def maj_data(self) :
        cursor.execute("UPDATE PROSPECT set nom = ? , prenom = ? , numSiret = ?, adressePostale = ?, codePostale = ?, ville = ? WHERE id_prospect = ?", self.__nom, self.__prenom, self.__numSiret, self.__adresse, self.__codePostal, self.__ville, self.__id)
        connection.commit()

    """
    setteur de la class client
    """
    def set_nom(self, new) : 
        self.__nom = new
        self.maj_data()

    def set_prenom(self, new) : 
        self.__prenom = new 
        self.maj_data()

    def set_numSiret(self, new) : 
        self.__numSiret = new
        self.maj_data()

    def set_adresse(self, new) : 
        self.__adresse = new 
        self.maj_data()

    def set_codePostal(self, new) : 
        self.__codePostal = new 
        self.maj_data()

    def set_ville(self, new) : 
        self.__ville = new 
        self.maj_data()

    def affiche_client(self) : 
        if self.__numSiret == "" : 
            # client physique
            return "Client Physique, {} {} habite au {} à {} {}".format(self.__prenom, self.__nom, self.__adresse, self.__codePostal, self.__ville)
        else : 
            return "Client Moral, {} recensé au {} à {} {}".format(self.__nom, self.__adresse, self.__codePostal, self.__ville)
