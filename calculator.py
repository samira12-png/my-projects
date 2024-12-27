import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import math

def calculate(text):
    try:
        if text == "=":
            return str(eval(entry.get()))
        elif text == "C":
            return ""
        elif text == "<-":
            return entry.get()[:-1]
        elif text == "x^2":
            return str(float(entry.get()) ** 2)
        elif text == "Pi":
            return entry.get() + str(math.pi)
        elif text == "Exp":
            return entry.get() + "e"
        else:
            return entry.get() + text
    except:
        return "Error"

def on_button_click(btn_text):
    entry.delete(0, ttk.END)
    entry.insert(0, calculate(btn_text))

root = ttk.Window(themename="cosmo")
root.title("Calculator")

entry = ttk.Entry(root, justify='right', bootstyle=INFO)
entry.pack(fill=BOTH, ipadx=8, padx=10, pady=10)

buttons = [
    ["%", "x^2", "C", "<-"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "Pi", "/"],
    ["(", ")", "Exp", "="]
]

for row in buttons:
    frame = ttk.Frame(root)
    frame.pack(expand=True, fill=BOTH)
    for btn in row:
        ttk.Button(
            frame,
            text=btn,
            bootstyle=SUCCESS if btn == "=" else PRIMARY if btn in {"+", "-", "*", "/"} else SECONDARY,
            command=lambda b=btn: on_button_click(b)
        ).pack(side="left", expand=True, fill=BOTH)

root.mainloop()
