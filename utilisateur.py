class Users:
    def __init__(self,idUser,identifiant,passwd):
        self.idUser = idUser
        self.__identifiant = identifiant
        self.__passwd = passwd

    def get_iduser(self):
        return self.__iduser

    def get_identifiant(self):
        return self.__identifiant
    
    def get_passwd(self):
        return self.__passwd


    def set_identifiant(self,id):
        self.__identifiant = id

    def set_mdp(self,mdp):
        self.__passwd = mdp



    