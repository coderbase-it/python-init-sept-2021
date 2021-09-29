from tkinter import Tk, Label, StringVar, Entry, Button

def insert():
    print('insert')
    print(name_var.get())
    print(phone_var.get())

def show():
    print('show')


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
    init()