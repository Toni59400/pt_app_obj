from select import select
from tkinter import *
from utilisateur import *
from tkinter import messagebox

def seConnecter():
    cpt = 0
    user = cursor.execute("SELECT * FROM Utilisateur WHERE identifiant= ?", (e1.get(),))
    connection.commit
    for row in user:
        cpt+=1
    if cpt == 0:
        messagebox.showinfo("Mauvais identifiant", "L'identifiant renseigné n'est pas bon !")

def quitter():
    connection.quit()
    quit()

login = Tk()

login.title("Connection")

identifiant = Label(login, text="Identifiant").grid(row=0, column=0, padx=20, pady=20)
e1 = Entry(login)
e1.grid(row=0, column=1, padx=20, pady=20)
mdp = Label(login, text="Mot de passe").grid(row=1, column=0, padx=20, pady=20)
e2 = Entry(login, show="*")
e2.grid(row=1, column=1, padx=20, pady=20)
submit = Button(login, text="Se connecter", command=seConnecter).grid(row=2, column=0, padx=20, pady=20)
exit = Button(login, text="Quitter", command=quitter).grid(row=2, column=1, padx=20, pady=20)

login.mainloop()

connection.close()