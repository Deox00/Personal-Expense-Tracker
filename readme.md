Personal Expense Tracker (Tkinter GUI)

A modern, minimal, and elegant Python Tkinter-based personal finance tracker that allows users to manage daily income and expenses through a smooth, mobile-style interface.
All transactions are stored locally using JSON, making the data persistent across sessions.

📌 Features

Add Expense (money spent)

Add Income (money received)

Auto-calculated Current Balance

Clean Transaction History List

Timestamps for Every Transaction

Persistent Storage using JSON

Modern Matte-Black UI using Tkinter

Popup Windows for Adding Entries

📸 GUI Overview

The interface consists of:

A header displaying the app name

A balance card showing the total balance

Buttons for adding income and expenses

A scrollable list of transactions in reverse chronological order

🧠 How It Works (Flow)

Start Application

Load Data from transactions.json

Display UI

Current balance

Transaction list

User Action: Add Expense or Income

Save Transaction to JSON

Update UI Automatically

End

🛠️ Tech Stack / Libraries Used

Python 3.x

Tkinter – GUI Framework

JSON – Local data storage

datetime – Timestamp generation

(No external libraries required.)

📂 Project Structure
Expense-Tracker/
│
├── transactions.json      # Stores all transactions
├── expense_tracker.py     # Main Tkinter application
└── README.md              # Documentation

▶️ How to Run
1. Install Python

Make sure Python 3.x is installed.

2. Run the script
python expense_tracker.py


The GUI will open instantly.

🔄 Resetting Data (Optional)

If you want to clear all transactions only once, delete the JSON file manually:

del transactions.json


or inside Python:

open("transactions.json", "w").write("[]")

💡 Future Improvements (Optional)

Category tags (Food, Travel, Shopping, etc.)

Monthly statistics

Graphs and charts (Matplotlib)

Export to Excel

PIN-lock start screen

More premium UI themes