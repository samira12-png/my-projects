from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import messagebox

pro = Tk()
pro.geometry('600x800')
pro.resizable(False,False)
pro.config(background="silver")
#############################################################################
from datetime import datetime

def validate_date(date):
    try:
        birth_date = datetime.strptime(date, "%m/%d/%y")
        if birth_date > datetime.now():
            messagebox.showwarning("Erreur", "La date de naissance ne peut pas être dans le futur!")
            return False
        return True
    except ValueError:
        messagebox.showwarning("Erreur", "Format de date invalide!")
        return False


def register_student():
    name = en_name.get()
    email = en_email.get()
    phone = en_phone.get()
    gender = combo_gender.get()
    city = en_address.get()
    date = date_entry.get()

    if not name or not email or not phone or not gender or not city:
        messagebox.showwarning("Erreur", "Tous les champs doivent être remplis!")
        return

    if not validate_date(date):  # Check if the date is valid
        return


    tree_view.insert("", "end", values=(name, email, phone, gender, city, date))
    messagebox.showinfo("Succès", f"L'étudiant {name} a été enregistré!")
    clear_fields()


def update_student():
    selected_item = tree_view.selection()
    if not selected_item:
        messagebox.showwarning("Erreur", "Veuillez sélectionner un étudiant à mettre à jour.")
        return

    if not validate_date(date):  # Check if the date is valid
        return

    
    # Mettre à jour l'élément sélectionné avec les nouvelles valeurs
    tree_view.item(selected_item, values=(
        en_name.get(),
        en_email.get(),
        en_phone.get(),
        combo_gender.get(),
        en_address.get(),
        date_entry.get()
    ))
    messagebox.showinfo("Succès", "Les informations de l'étudiant ont été mises à jour!")


def delete_student():
    selected_item = tree_view.selection()
    if not selected_item:
        messagebox.showwarning("Erreur", "Veuillez sélectionner un étudiant à supprimer.")
        return
    
    # Supprimer l'élément sélectionné
    tree_view.delete(selected_item)
    messagebox.showinfo("Succès", "L'étudiant a été supprimé!")

def clear_fields():
    # Efface les champs d'entrée
    en_name.delete(0, END)
    en_email.delete(0, END)
    en_phone.delete(0, END)
    combo_gender.set("")
    en_address.delete(0, END)
    date_entry.set_date("")

def show_all_students():
    # Affiche tous les étudiants dans une boîte de dialogue
    students = tree_view.get_children()
    if not students:
        messagebox.showinfo("Information", "Aucun étudiant enregistré.")
        return

    all_data = []
    for student in students:
        all_data.append(tree_view.item(student, "values"))
    messagebox.showinfo("Liste des étudiants", "\n".join(map(str, all_data)))


def search_student():
    query = en_search.get().strip().lower()
    if not query:
        messagebox.showinfo("Info", "Veuillez entrer un nom pour rechercher.")
        return
    for child in tree_view.get_children():
        values = tree_view.item(child, "values")
        if query in values[0].lower():
            tree_view.selection_set(child)
            tree_view.see(child)
            return
    messagebox.showinfo("Info", "Aucun étudiant trouvé avec ce nom.")

##############################################################################
title=Label(pro,text='Student Managemennt System',font=('Arial',20,'bold'),bg='yellow')
title.place(x=100,y=10)

lbl_name = Label(pro,text='Name of Student:',bg='silver')
lbl_name.place(x=80,y=80)
en_name = Entry(pro,bd='2',justify='center')
en_name.place(x=180,y=80)

lbl_email = Label(pro,text='Email',bg='silver')
lbl_email.place(x=80,y=120)
en_email = Entry(pro,bd='2',justify='center')
en_email.place(x=180,y=120)

lbl_phone = Label(pro,text='Phone of Student',bg='silver')
lbl_phone.place(x=80,y=160)
en_phone = Entry(pro,bd='2',justify='center')
en_phone.place(x=180,y=160)

lbl_gender = Label(pro,text ='Choose gender ',bg='silver')
lbl_gender.place(x=80,y=200)
combo_gender = ttk.Combobox(pro,state='readonly')
combo_gender['value']= ('male','female')
combo_gender.place(x=180,y=200)

lbl_address = Label(pro,text='Citty',bg='silver')
lbl_address.place(x=80,y=240)
en_address = Entry(pro,bd='2',justify='center')
en_address.place(x=180,y=240)

Date_lbl = Label(pro,text="Date birth :",bg='silver')
Date_lbl.place(x=80,y=280)
date_entry = DateEntry(pro,selected_mode="days",width=30)
date_entry.place(x=180,y=280)
        
add_btn = Button(pro,text='REGISTER',bg='#85929E',fg='white',command=register_student)
add_btn.place(x=190,y=320)
upd_btn = Button(pro,text='UPDATE',bg='#85929E',fg='white',command=update_student)
upd_btn.place(x=260,y=320)
del_btn = Button(pro,text='DELETE',bg='#85929E',fg='white',command=delete_student)
del_btn.place(x=330,y=320)
clear_btn = Button(pro,text='CLEAR',bg='#85929E',fg='white',command=clear_fields)
clear_btn.place(x=400,y=320)
show_btn = Button(pro,text='showALL',bg='#85929E',fg='white',command=show_all_students)
show_btn.place(x=470,y=320)

mini_title = Label(pro,text='Please select one record below to update or delete',bg='orange')
mini_title.place(x=180,y=360)
###########################################################
dietal_fr= Frame(pro,bg='gray')
dietal_fr.place(x=5,y=385,width=580,height=210)

tree_view = ttk.Treeview(dietal_fr, columns=("name", "email", "phone", "gender", "city","date"), show="headings")

x_scroll = Scrollbar(dietal_fr, orient=HORIZONTAL, command=tree_view.xview)
x_scroll.pack(side=BOTTOM, fill=X)
y_scroll = Scrollbar(dietal_fr, orient=VERTICAL, command=tree_view.yview)
y_scroll.pack(side=RIGHT, fill=Y)


tree_view.heading("name", text="Name of Student")
tree_view.heading("email", text="Email")
tree_view.heading("phone", text="Phone")
tree_view.heading("gender", text="Gender")
tree_view.heading("city", text="City")
tree_view.heading("date", text="Date of Birth")

tree_view.pack(fill=BOTH, expand=True)

tree_view.configure(xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set)

tree_view.column('name',width=170)
tree_view.column('email',width=90)
tree_view.column('phone',width=100)
tree_view.column('gender',width=100)
tree_view.column('city',width=100)
tree_view.column('date',width=120)

lbl_search=Label(pro,text='Please Enter name:')
lbl_search.place(x=90,y=620)
en_search=Entry(pro)
en_search.place(x=200,y=620)
btn_search=Button(pro,text="Search",bg='orange',fg='white',command=search_student)
btn_search.place(x=330,y=620)

btn_exit=Button(pro,text='Exit',bg='silver',fg='white', command=pro.destroy)
btn_exit.place(x=270,y=670,width=100,height=20)
pro.mainloop()
