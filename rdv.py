from dbconnection import *
class Rdv():

    def __init__(self, id, date, com_avant, com_apres, prosp, produit) : 
        self.__id = id 
        self.__date = date
        self.__com_avant = com_avant
        self.__com_apres = com_apres 
        self.__prosp = str(prosp)
        self.__produit = str(produit)

    def get_produit(self) : 
        sql = "SELECT * FROM PRODUIT where id_produit = {}".format(self.__produit)
        data = cursor.execute(sql)
        name_produit = ""
        for row in data : 
            name_produit = str(row['nom'])
        return name_produit

    def get_id(self) : 
        return self.__id

    def get_date(self) : 
        return self.__date

    def get_com_avant(self):
        return self.__com_avant
    
    def get_com_apres(self):
        return self.__com_apres

    def get_prosp(self) :
        sql = "SELECT * FROM PROSPECT where id_prospect = {}".format(self.__prosp)
        data = cursor.execute(sql)
        name = ""
        for row in data : 
            name = str(row['prenom']) + " " + str(row['nom'])
        return name