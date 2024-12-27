import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class Produits:
    def __init__(self, pro):
        self.pro = pro
        self.pro.title("Produits management system")
        self.pro.geometry("700x300")  
        self.pro.resizable(False, False)
        self.pro.configure(bg='silver')

        self.title = tk.Label(pro, text="Store Name", font=("Arial", 20, "bold"))
        self.title.pack(pady=15)
############################################
        """variables"""
        self.id = tk.StringVar()
        self.name = tk.StringVar()
        self.price = tk.StringVar()
        self.quantite = tk.StringVar()

        detail_fr = tk.Frame(pro, bg='gray')
        detail_fr.place(x=5, y=60, width=250, height=170)
        """champs id"""
        lbl_id = tk.Label(detail_fr, text='ID', bg='silver')
        lbl_id.place(x=20, y=10)
        self.en_id = tk.Entry(detail_fr, bd='2',textvariable=self.id)
        self.en_id.place(x=80, y=10)

        """champs name"""
        lbl_name = tk.Label(detail_fr, text='Name', bg='silver')
        lbl_name.place(x=20, y=40)
        self.en_name = tk.Entry(detail_fr, bd='2',textvariable=self.name)
        self.en_name.place(x=80, y=40)

        """champs price"""
        lbl_price = tk.Label(detail_fr, text='Price', bg='silver')
        lbl_price.place(x=20, y=70)
        self.en_price = tk.Entry(detail_fr, bd='2',textvariable=self.price)
        self.en_price.place(x=80, y=70)

        """champs quantite"""
        lbl_quantite = tk.Label(detail_fr, text='Quantite', bg='silver')
        lbl_quantite.place(x=20, y=100)
        self.en_quantite = tk.Entry(detail_fr, bd='2',textvariable=self.quantite)
        self.en_quantite.place(x=80, y=100)
        """Buttons"""
        btn_add = tk.Button(detail_fr, text='Add', bg='green', fg='white',command=self.add_product)
        btn_add.place(x=20, y=140, width=60)

        btn_update = tk.Button(detail_fr, text='Update', bg='yellow', fg='black',command=self.update_product)
        btn_update.place(x=100, y=140, width=60)

        btn_delete = tk.Button(detail_fr, text='Delete', bg='red', fg='white',command=self.delete_product)
        btn_delete.place(x=180, y=140, width=60)

############################################
        self.fr = tk.Frame(pro, bg='gray')
        self.fr.place(x=270, y=60, width=420, height=170)

       
        self.tree = ttk.Treeview(self.fr, columns=("id", "name", "price", "quantite"), show="headings")
        self.tree.heading("id", text="ID ")
        self.tree.heading("name", text="Name ")
        self.tree.heading("price", text="Price")
        self.tree.heading("quantite", text="Quantity")
        self.tree.pack(fill=tk.BOTH, expand=True)

        self.tree.column('id',width=70)
        self.tree.column('name',width=70)
        self.tree.column('price',width=70)
        self.tree.column('quantite',width=70)
        """Fonctions"""
    def clear_fields(self):
        self.id.set("")
        self.name.set("")
        self.price.set("")
        self.quantite.set("")
    def add_product(self):
            id = int(self.id.get())
            name = self.name.get()
            price = float(self.price.get())
            quantity = int(self.quantite.get())

            if not id or not name or not price or not  quantity:
                messagebox.showwarning("Erreur", "Tous les champs doivent être remplis!")
                return

            self.tree.insert("", "end", values=(id, name, price, quantity))
            messagebox.showinfo("Succès", f"L'étudiant {name} a été enregistré!")
            self.clear_fields()

    def update_product(self):
            selected_item = self.tree.selection()
            if not selected_item:
                messagebox.showwarning("Erreur", "Veuillez sélectionner un étudiant à mettre à jour.")
                return

            self.tree.item(selected_item, values=(
                self.id.get(),
                self.name.get(),
                self.price.get(),
                self.quantite.get()
            ))
            messagebox.showinfo("Succès", "Les informations de l'étudiant ont été mises à jour!")

    def delete_product(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Erreur", "Veuillez sélectionner un étudiant à supprimer.")
            return

        self.tree.delete(selected_item)
        messagebox.showinfo("Succès", "L'étudiant a été supprimé!")
#############################################################






pro = tk.Tk()
app = Produits(pro)
pro.mainloop()
