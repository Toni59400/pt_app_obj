from dbconnection import *
class Rdv():

    def __init__(self, id, date, com_avant, com_apres, prosp) : 
        self.__id = id 
        self.__date = date
        self.__com_avant = com_avant
        self.__com_apres = com_apres 
        self.__prosp = str(prosp)

    def get_id(self) : 
        return self.__id

    def get_date(self) : 
        return self.__date

    def get_com_avant(self):
        return self.__com_avant
    
    def get_com_apres(self):
        return self.__com_apres

    def get_prosp(self) : 
        print(type(self.__prosp))
        sql = "SELECT * FROM PROSPECT where id_prospect = {}".format(self.__prosp)
        data = cursor.execute(sql)
        name = ""
        for row in data : 
            name = str(row['prenom']) + " " + str(row['nom'])
        return name