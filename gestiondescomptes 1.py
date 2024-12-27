import tkinter as tk
from tkinter import ttk
from abc import ABC, abstractmethod


class Compte(ABC):
    def __init__(self, numero, proprietaire, solde_initial):
        self.numero = numero
        self.proprietaire = proprietaire
        self.solde_initial = solde_initial


    @abstractmethod
    def obtenir_informations(self):
        pass

class CompteCourant(Compte):
    def __init__(self, numero, proprietaire, solde_initial, montant_decouvert):
        self.numero = numero
        self.proprietaire = proprietaire
        self.solde_initial = solde_initial
        self.montant_decouvert = montant_decouvert
       

    def obtenir_informations(self):
        return (self.numero, self.proprietaire, self.solde_initial, "Courant", "", self.montant_decouvert)


class CompteEpargne(Compte):
    def __init__(self, numero, proprietaire, solde_initial, taux_interet):
        self.numero = numero
        self.proprietaire = proprietaire
        self.solde_initial = solde_initial
        self.taux_interet = taux_interet

    def obtenir_informations(self):
        return (self.numero, self.proprietaire, self.solde_initial, "Epargne", self.taux_interet, "")
    

compte_id = 1
comptes = []

def update_fields():
    if type_var.get() == "Courant":
        taux_interet_entry.config(state="disabled")
        montant_decouvert_entry.config(state="normal")
    elif type_var.get() == "Epargne":
        taux_interet_entry.config(state="normal")
        montant_decouvert_entry.config(state="disabled")

def creer_compte():
    global compte_id
    proprietaire = proprietaire_var.get()
    solde_initial = solde_initial_var.get()
    type_compte = type_var.get()
    taux_interet = taux_interet_var.get() if type_compte == "Epargne" else ""
    montant_decouvert = montant_decouvert_var.get() if type_compte == "Courant" else ""

    if proprietaire and solde_initial.replace('.', '', 1).isdigit():
        if type_compte == "Courant":
            compte = CompteCourant(compte_id, proprietaire, float(solde_initial), float(montant_decouvert))
        elif type_compte == "Epargne":
            compte = CompteEpargne(compte_id, proprietaire, float(solde_initial), float(taux_interet))

        comptes.append(compte)
        table.insert("", "end", values=compte.obtenir_informations())


        compte_id += 1
        numero_var.set(compte_id)
        proprietaire_var.set("")
        solde_initial_var.set("")
        taux_interet_var.set("")
        montant_decouvert_var.set("")
    else:
        print("Veuillez remplir correctement les champs obligatoires.")


root = tk.Tk()
root.title("Gestion des Comptes")

"""les variables"""
numero_var = tk.IntVar(value=compte_id)
proprietaire_var = tk.StringVar()
solde_initial_var = tk.StringVar()
type_var = tk.StringVar(value="Courant")
taux_interet_var = tk.StringVar()
montant_decouvert_var = tk.StringVar()

"""la formulaire de la fenetre"""
tk.Label(root, text="Numéro:").grid(row=0, column=0, padx=5, pady=5)
tk.Entry(root, textvariable=numero_var, state="readonly").grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Propriétaire:").grid(row=1, column=0, padx=5, pady=5)
tk.Entry(root, textvariable=proprietaire_var).grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Solde Initial:").grid(row=2, column=0, padx=5, pady=5)
tk.Entry(root, textvariable=solde_initial_var).grid(row=2, column=1, padx=5, pady=5)
tk.Label(root, text="Euro").grid(row=2, column=2, padx=5, pady=5)

tk.Label(root, text="Type:").grid(row=3, column=0, padx=5, pady=5)
tk.Radiobutton(root, text="Courant", variable=type_var, value="Courant", command=update_fields).grid(row=3, column=1, padx=5, pady=5)
tk.Radiobutton(root, text="Epargne", variable=type_var, value="Epargne", command=update_fields).grid(row=3, column=2, padx=5, pady=5)

tk.Label(root, text="Taux Intérêt:").grid(row=4, column=0, padx=5, pady=5)
taux_interet_entry = tk.Entry(root, textvariable=taux_interet_var, state="disabled")
taux_interet_entry.grid(row=4, column=1, padx=5, pady=5)
tk.Label(root, text="%").grid(row=4, column=2, padx=5, pady=5)

tk.Label(root, text="M. Découvert:").grid(row=5, column=0, padx=5, pady=5)
montant_decouvert_entry = tk.Entry(root, textvariable=montant_decouvert_var, state="normal")
montant_decouvert_entry.grid(row=5, column=1, padx=5, pady=5)

tk.Button(root, text="Création Compte", command=creer_compte).grid(row=6, column=0, columnspan=3, pady=10)


columns = ("Numéro", "Propriétaire", "Solde Initial", "Type", "Taux Intérêt", "Montant Découvert")
table = ttk.Treeview(root, columns=columns, show="headings", height=10)
table.grid(row=7, column=0, columnspan=3, padx=10, pady=10)

for col in columns:
    table.heading(col, text=col)
    table.column(col, width=100)


update_fields()
root.mainloop()