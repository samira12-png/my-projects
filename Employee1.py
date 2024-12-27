import tkinter as tk
from tkinter import ttk, messagebox

employees = []

def insert_empolye():
    def save_employee():
        name = name_entry.get()
        age = age_entry.get()

        if not name or not age:
            messagebox.showwarning("Input Error", "Please fill in both fields.")
            return

        employees.append({"name": name, "age": age})
        tree.insert("", tk.END, values=(name, age))
        insert.destroy()

    insert = tk.Toplevel(root)
    insert.title("Insert Employee")

    tk.Label(insert, text="Name").grid(row=0, column=0)
    name_entry = tk.Entry(insert)
    name_entry.grid(row=0, column=1)

    tk.Label(insert, text="Age").grid(row=1, column=0)
    age_entry = tk.Entry(insert)
    age_entry.grid(row=1, column=1)

    tk.Button(insert, text="Submit", bg="green", fg="white", command=save_employee).grid(row=5, column=0, pady=10)
    tk.Button(insert, text="Cancel", command=insert.destroy, bg="red", fg="white").grid(row=5, column=1, pady=10)

def delete_employe():
    selected_item = tree.selection()
    if selected_item:
        conf = messagebox.askokcancel('Confirmation', 'Voulez-vous vraiment supprimer ?')
        if conf:
            tree.delete(selected_item)

root = tk.Tk()
root.title("Treeview Insert/Delete Example")
root.geometry("400x300")

tree = ttk.Treeview(root, columns=("Name", "Age"), show="headings")
tree.heading("Name", text="Name")
tree.heading("Age", text="Age")
tree.place(x=10, y=15, width=380, height=150)

btn_insert = tk.Button(root, text="Insert", bg="green", fg="white", command=insert_empolye)
btn_insert.place(x=100, y=180, width=100, height=30)

btn_delete = tk.Button(root, text="Delete", bg="red", fg="white", command=delete_employe)
btn_delete.place(x=210, y=180, width=100, height=30)

root.mainloop()
