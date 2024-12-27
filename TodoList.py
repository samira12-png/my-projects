import ttkbootstrap as ttk
from ttkbootstrap.widgets import Label, Button, Entry, Frame, Checkbutton
import tkinter as tk

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x550")
        self.root.resizable(False, False)  

        self.header_frame = Frame(self.root, padding=10)
        self.header_frame.pack(fill="x", padx=20, pady=10)

        self.title_label = Label(self.header_frame, text="To-Do List", font=("Arial", 18, "bold"), anchor="center")
        self.title_label.pack(fill="x")

        input_frame = Frame(self.root, padding=(20, 10), style="TFrame")
        input_frame.pack(pady=15, padx=20, fill="x")

        self.task_entry = Entry(input_frame, width=25, font=("Arial", 12), bootstyle="success")
        self.task_entry.grid(row=0, column=0, padx=10)

        self.add_button = Button(input_frame, text="Ajouter", command=self.add_todo, style="primary.TButton")
        self.add_button.grid(row=0, column=1, padx=10)

        self.todo_frame = Frame(self.root, padding=10, style="TFrame")
        self.todo_frame.pack(fill="both", expand=True)

        self.info_label = Label(self.root, text="Ajoutez une tâche et cliquez sur 'Ajouter'.", anchor="center", bootstyle="info")
        self.info_label.pack(pady=10)

    def add_todo(self):
        task_text = self.task_entry.get().strip()
        if task_text:  
            task_frame = Frame(self.todo_frame, padding=10, bootstyle="light")
            task_frame.pack(fill="x", pady=5)

            var = tk.BooleanVar()

            checkbox = Checkbutton(
                task_frame, 
                variable=var, 
                command=lambda: self.toggle_strike(task_label, var),
                bootstyle="success"
            )
            checkbox.pack(side="left", padx=5)

            task_label = Label(task_frame, text=task_text, font=("Arial", 12), anchor="w",bootstyle="light ,inverse")
            task_label.pack(side="left", padx=5, fill="x")

            delete_button = Button(task_frame, text="Supprimer", command=lambda: self.delete_task(task_frame), style="danger.TButton")
            delete_button.pack(side="right", padx=5)

            self.task_entry.delete(0, tk.END)
            self.info_label.config(text="Tâche ajoutée avec succès !", bootstyle="info")  
        else:
            self.info_label.config(text="Veuillez entrer une tâche valide.", bootstyle="danger")  

    def toggle_strike(self, label, var):
        if var.get(): 
            label.config(font=("Arial", 12, "overstrike")) 
        else: 
            label.config(font=("Arial", 12, "normal")) 
    
    def delete_task(self, task_frame):
        task_frame.destroy()  


root = ttk.Window(themename="lumen")
app = TodoApp(root)
root.mainloop()
