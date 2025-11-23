import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import json

FILENAME = "transactions.json"

# ---------------- Data Handling ---------------- #

def load_data():
    try:
        with open(FILENAME, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_data(data):
    with open(FILENAME, "w") as f:
        json.dump(data, f, indent=4)

def add_transaction(amount, t_type, note):
    data = load_data()
    entry = {
        "amount": amount,
        "type": t_type,
        "note": note,
        "date": datetime.now().strftime("%Y-%m-%d  %I:%M %p")
    }
    data.append(entry)
    save_data(data)

# ---------------- UI Functions ---------------- #

def update_list():
    listbox.delete(0, tk.END)
    data = load_data()

    for t in reversed(data):
        sign = "+" if t["type"] == "income" else "-"
        entry = f"{t['date']} | {t['note']} | {sign}₹{t['amount']}"
        listbox.insert(tk.END, entry)

def update_balance():
    data = load_data()
    income = sum(t["amount"] for t in data if t["type"] == "income")
    expense = sum(t["amount"] for t in data if t["type"] == "expense")
    balance = income - expense
    balance_label.config(text=f"₹{balance}")

def open_add_screen(t_type):
    win = tk.Toplevel(window)
    win.title(f"Add {t_type.title()}")
    win.geometry("320x280")
    win.configure(bg=BG)

    tk.Label(win, text=f"Add {t_type.title()}",
             bg=BG, fg="white", font=("Arial", 18, "bold")).pack(pady=15)

    tk.Label(win, text="Amount:", bg=BG, fg="white").pack()
    amt_entry = tk.Entry(win)
    amt_entry.pack(pady=5)

    tk.Label(win, text="Note:", bg=BG, fg="white").pack()
    note_entry = tk.Entry(win)
    note_entry.pack(pady=5)

    def save():
        try:
            amount = float(amt_entry.get())
        except:
            messagebox.showerror("Error", "Enter a valid amount.")
            return
        
        note = note_entry.get().strip()
        if not note:
            messagebox.showerror("Error", "Note cannot be empty.")
            return
        
        add_transaction(amount, t_type, note)
        update_list()
        update_balance()
        win.destroy()

    tk.Button(win, text="Save", bg="#3E8E7E", fg="white",
              font=("Arial", 12, "bold"),
              width=15, command=save).pack(pady=20)


# ---------------- Main Window ---------------- #

BG = "#171717"  # Midnight Black Background

window = tk.Tk()
window.title("Personal Expense Tracker")
window.geometry("400x650")
window.configure(bg=BG)
window.resizable(False, False)

# Title
tk.Label(window, text="Personal Expense Tracker",
         bg=BG, fg="white", font=("Arial", 20, "bold")).pack(pady=15)

# Balance Card
balance_frame = tk.Frame(window, bg="#1F1F1F", padx=20, pady=20)
balance_frame.pack(pady=10, padx=20, fill="x")

tk.Label(balance_frame, text="Current Balance",
         bg="#1F1F1F", fg="white",
         font=("Arial", 12)).pack()

balance_label = tk.Label(balance_frame, text="₹0",
                         bg="#1F1F1F", fg="white",
                         font=("Arial", 28, "bold"))
balance_label.pack()

# Buttons Row
btn_frame = tk.Frame(window, bg=BG)
btn_frame.pack(pady=15)

tk.Button(btn_frame, text="Add Expense",
          relief="flat", bd=0,
          bg="#D9534F", fg="white",
          font=("Arial", 12, "bold"),
          width=13, command=lambda: open_add_screen("expense")).grid(row=0, column=0, padx=10)

tk.Button(btn_frame, text="Add Income",
          relief="flat", bd=0,
          bg="#5CB85C", fg="white",
          font=("Arial", 12, "bold"),
          width=13, command=lambda: open_add_screen("income")).grid(row=0, column=1, padx=10)

# Transactions Title
tk.Label(window, text="Transactions",
         bg=BG, fg="white", font=("Arial", 16, "bold")).pack()

# Listbox Frame
list_frame = tk.Frame(window, bg=BG)
list_frame.pack(fill="both", expand=True, padx=20, pady=10)

listbox = tk.Listbox(list_frame, width=40, height=20,
                     bg="#1F1F1F", fg="white",
                     selectbackground="#1F1F1F",
                     font=("Consolas", 11))
listbox.pack(fill="both", expand=True)

# Load initial values
update_list()
update_balance()

window.mainloop()
