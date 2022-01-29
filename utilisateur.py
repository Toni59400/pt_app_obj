from dbconnection import *

class Utilisateur:
    def __init__(self,id,identifiant,mdp):
        self.__id = id
        self.__identifiant = identifiant
        self.__mdp = mdp


    #get
    def get_id(self) :
        return self.__id

    def get_identifiant(self):
        return self.__identifiant
    
    def get_passwd(self):
        return self.__mdp

    #maj
    def maj_data(self) :
        cursor.execute("UPDATE UTILISATEUR set identifiant = ? , mdp = ? WHERE id_utilisateur = ?", (self.__identifiant, self.__mdp, self.__id))
        connection.commit()

    #set
    def set_identifiant(self,new):
        self.__identifiant = new
        self.maj_data()

    def set_mdp(self,new):
        self.__mdp = new
        self.maj_data()
