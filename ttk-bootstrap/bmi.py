import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        bmi = weight * 10000 / (height ** 2)
        if bmi < 19:
            status = "Sous poids"
        elif 19 <= bmi <= 25:
            status = "Normal"
        else:
            status = "Surpoids"
        result_label.config(text=f"BMI: {bmi:.2f} ({status})")
    except ValueError:
        messagebox.showerror("Erreur", "Entrée invalide!")

root = ttk.Window(themename="cosmo")
root.title("Calcul BMI")

# Poids Input
ttk.Label(root, text="Poids (kg):", font=("Arial", 12)).pack(pady=5)
weight_entry = ttk.Entry(root, font=("Arial", 12), width=20)
weight_entry.pack(pady=5)

# Taille Input
ttk.Label(root, text="Taille (cm):", font=("Arial", 12)).pack(pady=5)
height_entry = ttk.Entry(root, font=("Arial", 12), width=20)
height_entry.pack(pady=5)

# Calculer Button
calculate_button = ttk.Button(root, text="Calculer", bootstyle=SUCCESS, command=calculate_bmi)
calculate_button.pack(pady=10)

# Result Label
result_label = ttk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
