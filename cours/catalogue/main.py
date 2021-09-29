from tkinter import Tk, Label, StringVar, Entry, Button
import sqlite3

def create_database():
    # DB-API
    connection = sqlite3.connect('base.db')
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS contacts(name TEXT, phone TEXT)")
    connection.commit()
    cursor.close()
    connection.close()


def insert():
    print('insert')
    print(name_var.get())
    print(phone_var.get())
    connection = sqlite3.connect('base.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO contacts values (?,?)", (name_var.get(), phone_var.get() ))
    connection.commit()
    cursor.close()
    connection.close()

def show():
    print('show')
    connection = sqlite3.connect('base.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * from contacts")
    #connection.commit() pas commit car pas de modifications
    for element in cursor.fetchall():
        print(element)
        name, phone = element
        print(name, phone)
    cursor.close()
    connection.close()

def init():
    # creation de la fenetre
    fenetre = Tk()
    # personnaliser la fenetre
    fenetre.geometry('410x450')
    fenetre.title('Phone Catalogue')
    fenetre.configure(background="powder blue")

    # création d'un label + positionnement
    name_label = Label(fenetre, text="Name :")
    #name_label.pack() # position automatiquement
    name_label.place(x=0, y=0) # position manuel
    phone_label = Label(fenetre, text="Phone :")
    phone_label.place(x=0, y=30)

    # création de variable Tkinter
    global name_var
    global phone_var
    name_var , phone_var = StringVar(), StringVar()

    # création des inputs
    name_entry = Entry(fenetre, width=20, textvar=name_var)
    name_entry.place(x=80, y=0)
    phone_entry = Entry(fenetre, width=20, textvar=phone_var)
    phone_entry.place(x=80, y=30)

    # création des boutons
    bouton_insert = Button(fenetre, text="Insert:", command=insert)
    bouton_insert.place(x=80, y=100)

    bouton_show = Button(fenetre, text="Show :", command=show)
    bouton_show.place(x=150, y=100)

    # lancement de la boucle principale
    fenetre.mainloop()


if __name__ == "__main__":
    create_database()
    init()
