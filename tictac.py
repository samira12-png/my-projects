import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
import random

# Initialisation de la fenêtre principale
root = ttk.Window(themename="cosmo")
root.title("Tic-Tac-Toe")
root.geometry("400x400")

# Variables globales
current_player = "X"
buttons = [[None for _ in range(3)] for _ in range(3)]
scores = {"X": 0, "O": 0}

# Gestion du clic sur un bouton
def handle_click(row, col):
    global current_player
    if buttons[row][col]['text'] == "":
        buttons[row][col].configure(text=current_player)
        if check_winner():
            messagebox.showinfo("Gagnant", f"Le joueur {current_player} a gagné!")
            scores[current_player] += 1
            update_score_label()
            reset_board()
        elif check_draw():
            messagebox.showinfo("Égalité", "La partie est terminée, égalité!")
            reset_board()
        else:
            switch_player()

# Changement de joueur
def switch_player():
    global current_player
    current_player = "O" if current_player == "X" else "X"
    if current_player == "O":
        computer_play()

# Vérification des conditions de victoire
def check_winner():
    for i in range(3):  # Vérifier les lignes et colonnes
        if all(buttons[i][j]['text'] == current_player for j in range(3)) or \
           all(buttons[j][i]['text'] == current_player for j in range(3)):
            return True
    # Vérifier les diagonales
    if all(buttons[i][i]['text'] == current_player for i in range(3)) or \
       all(buttons[i][2-i]['text'] == current_player for i in range(3)):
        return True
    return False

# Vérification de l'égalité
def check_draw():
    return all(buttons[i][j]['text'] != "" for i in range(3) for j in range(3))

# Jeu de l'ordinateur
def computer_play():
    empty_cells = [(i, j) for i in range(3) for j in range(3) if buttons[i][j]['text'] == ""]
    if empty_cells:
        row, col = random.choice(empty_cells)
        buttons[row][col].configure(text="O")
        if check_winner():
            messagebox.showinfo("Gagnant", "L'ordinateur a gagné!")
            scores["O"] += 1
            update_score_label()
            reset_board()
        elif check_draw():
            messagebox.showinfo("Égalité", "La partie est terminée, égalité!")
            reset_board()
        else:
            switch_player()

# Réinitialisation du plateau
def reset_board():
    global current_player
    current_player = "X"
    for i in range(3):
        for j in range(3):
            buttons[i][j].configure(text="")

# Mise à jour du score
def update_score_label():
    score_label.config(text=f"X: {scores['X']} | O: {scores['O']}")

# Interface graphique
score_label = ttk.Label(root, text="X: 0 | O: 0")
score_label.pack(pady=10)

frame = ttk.Frame(root)
frame.pack()

for i in range(3):
    for j in range(3):
        buttons[i][j] = ttk.Button(frame, text="", bootstyle=SECONDARY, width=5, 
                                   command=lambda i=i, j=j: handle_click(i, j))
        buttons[i][j].grid(row=i, column=j, padx=5, pady=5)

reset_button = ttk.Button(root, text="Réinitialiser", bootstyle=SUCCESS, command=reset_board)
reset_button.pack(pady=10)

# Lancement de l'application
root.mainloop()
