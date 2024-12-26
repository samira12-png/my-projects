from tkinter import *
from ttkbootstrap import *
import ttkbootstrap as tk
from tkinter import filedialog, messagebox
################fonctions
def clear_fields():
    en_name.delete(0, END)
    en_age.delete(0,END)
    combo_gender.set("")
    en_fi.delete(0,END)
    en_phone.delete(0, END)
    
    
    


def add_student():
    name = en_name.get()
    age = en_age.get()
    gender = combo_gender.get()
    filiere=en_fi.get()
    phone = en_phone.get()
    if not name or not age or not gender or not filiere or not phone:
        messagebox.showwarning("Erreur", "Tous les champs doivent être remplis!")
        return
    table.insert("", "end", values=(name, age, gender,filiere, phone))
    messagebox.showinfo("Succès", f"L'étudiant {name} a été enregistré!")
    clear_fields()


def update_student():
    selected_item = table.selection()
    if not selected_item:
        messagebox.showwarning("Erreur", "Veuillez sélectionner un étudiant à mettre à jour.")
        return
    table.item(selected_item, values=(
        en_name.get(),
        en_age.get(),
        combo_gender.get(),
        en_fi.get(),
        en_phone.get()
    ))
    messagebox.showinfo("Succès", "Les informations de l'étudiant ont été mises à jour!")

def delete_student():
    selected_item = table.selection()
    if not selected_item:
        messagebox.showwarning("Erreur", "Veuillez sélectionner un étudiant à supprimer.")
        return
    table.delete(selected_item)
    messagebox.showinfo("Succès", "L'étudiant a été supprimé!")

def show_all_students():
    students = table.get_children()
    if not students:
        messagebox.showinfo("Information", "Aucun étudiant enregistré.")
        return
    all_data = []
    for student in students:
        all_data.append(table.item(student, "values"))
    messagebox.showinfo("Liste des étudiants", "\n".join(map(str, all_data)))

def search_student():
    query = en_search.get().strip().lower()
    if not query:
        messagebox.showinfo("Info", "Veuillez entrer un nom pour rechercher.")
        return
    for child in table.get_children():
        values = table.item(child, "values")
        if query in values[0].lower():
            table.selection_set(child)
            table.see(child)
            return
    messagebox.showinfo("Info", "Aucun étudiant trouvé avec ce nom.")

pro = tk.Window(themename="lumen")
pro.title("Student management")
pro.geometry("900x500")

title=Label(pro,text="Student management System",font=('Cooper',25),bootstyle="success,inverse")
title.place(x=210,y=0,width=700)

fr=Frame(pro,bootstyle="light")
fr.place(x=2,y=0,width=210,height=700)

lbl_name = Label(fr,text='Name',bootstyle='light,inverse')
lbl_name.place(x=4,y=10)
en_name = Entry(fr,bootstyle="secondary")
en_name.place(x=4,y=30)

lbl_age = Label(fr,text='Age',bootstyle='light,inverse')
lbl_age.place(x=4,y=70)
en_age = Entry(fr,bootstyle="secondary")
en_age.place(x=4,y=90)

lbl_gender = Label(fr,text ='Gender',bootstyle='light,inverse')
lbl_gender.place(x=4,y=130)
combo_gender = tk.Combobox(fr,state='readonly',bootstyle="secondary")
combo_gender['value']= ('male','female')
combo_gender.place(x=4,y=150)

lbl_fi = Label(fr,text='Filiere',bootstyle='light,inverse')
lbl_fi.place(x=4,y=190)
en_fi = Entry(fr,bootstyle="secondary")
en_fi.place(x=4,y=210)

lbl_phone = Label(fr,text='Phone',bootstyle='light,inverse')
lbl_phone.place(x=4,y=250)
en_phone= Entry(fr,bootstyle="secondary")
en_phone.place(x=4,y=270)
#########################buttons
add_btn = Button(fr,text='ADD',bootstyle='secondary',command=add_student)
add_btn.place(x=30,y=310,width=150)
upd_btn = Button(pro,text='UPDATE',bootstyle='secondary',command=update_student)
upd_btn.place(x=30,y=350,width=150)
del_btn = Button(pro,text='DELETE',bootstyle='secondary',command=delete_student)
del_btn.place(x=30,y=390,width=150)
clear_btn = Button(pro,text='CLEAR',bootstyle='secondary',command=clear_fields)
clear_btn.place(x=30,y=430,width=150)
show_btn = Button(pro,text='showALL',bootstyle='secondary',command=show_all_students)
show_btn.place(x=30,y=470,width=150)

##############################################
sear_fr= Frame(pro,bootstyle="light")
sear_fr.place(x=210,y=40,width=700,height=50)
            ####################################
lbl_search=Label(sear_fr,text='Enter name of Student',bootstyle='light,inverse')
lbl_search.place(x=10,y=12)
en_search=Entry(sear_fr,bootstyle="secondary")
en_search.place(x=140,y=12)

btn_search= Button(sear_fr,text='Search',bootstyle='warning',command=search_student)
btn_search.place(x=300,y=12,width=100,height=25)

btn_exit=Button(sear_fr,text='Exit', command=pro.destroy,bootstyle='danger-outline')
btn_exit.place(x=450,y=12,width=100,height=25)
###############treeview
dietal_fr= Frame(pro,bootstyle='info')
dietal_fr.place(x=212,y=90,width=700,height=605)

table = ttk.Treeview(dietal_fr,bootstyle="success", columns=("name", "age", "gender", "filiere", "phone"), show="headings")
table.heading("name", text="Name")
table.heading("age", text="Age")
table.heading("gender", text="Gender")
table.heading("filiere", text="Filiere")
table.heading("phone", text="Phone")

table.pack(fill=BOTH, expand=True)

table.column('name',width=40)
table.column('age',width=40)
table.column('gender',width=40)
table.column('filiere',width=40)
table.column('phone',width=40)

pro.mainloop()
