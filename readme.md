# 💰 Personal Expense Tracker (Tkinter GUI)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

A clean, elegant, and fully functional **Personal Expense Tracker** built using Python and Tkinter. This application allows users to add income and expenses, track their current balance, and view detailed transaction history — all stored persistently using a local JSON file.

![App Screenshot]
Screenshot 2025-11-23 191802.png
Screenshot 2025-11-23 192157.png
Screenshot 2025-11-23 191838.png
Screenshot 2025-11-23 192028.png

---

## 🚀 Features

### ✔ Modern Dark-Themed GUI
A classy **matte-black interface** (`#171717`) designed with clean buttons, distinct cards, and comfortable spacing for a premium user experience.

### ✔ Add Income & Expenses
Intuitive popup windows allow users to easily input:
* **Amount** (Validation included)
* **Note/Description**
* **Timestamp** (Auto-generated)

### ✔ Live Balance Calculation
The dashboard updates the **Current Balance** in real-time immediately after every transaction.

### ✔ Transaction History
A scrollable list box displaying:
* 📅 Date & Time
* 📝 Description
* 💵 Income (+) or Expense (–)

### ✔ Persistent Storage (JSON)
No database setup required! All transactions are stored in `transactions.json` and loaded automatically every time the app starts.

---

## 🛠️ Technologies Used

| Component | Purpose |
| :--- | :--- |
| **Python** | Core logic and application flow |
| **Tkinter** | Standard GUI framework for the interface |
| **JSON** | Lightweight persistent data storage |
| **Datetime** | Automatic timestamp generation |

---

## 📂 Project Structure

```text
Personal-Expense-Tracker/
│
├── main.py               # Main Tkinter GUI Application
├── transactions.json     # Auto-generated JSON storage (created on first run)
└── README.md             # Project documentation
🧠 How It Works (Internal Flow)
Load Data: On startup, the app reads existing records from transactions.json.

Show Dashboard: Displays the calculated balance and populates the scrollable history list.

Add Transaction: User clicks "Add Income" or "Add Expense," filling out a popup form.

Save to JSON: The new entry is appended to the list and dumped into the JSON file immediately.

Update UI: The balance label and listbox refresh instantly to reflect changes.

▶️ How to Run the Project
Step 1: Install Python
Ensure you have Python installed (Version 3.8 or higher is recommended).

Step 2: Clone & Run
Navigate to the folder and run the main script:

Bash

python main.py
Step 3: Start Tracking!
The GUI opens instantly. You can start adding transactions right away.

🔄 Resetting Data
If you want to clear your transaction history completely, you have two options:

Option A (Manual): Delete the transactions.json file from the folder. The app will create a fresh one next time it runs.

Option B (Programmatic): Run this simple Python command:

Python

open("transactions.json", "w").write("[]")
📌 Future Improvements
[ ] Category-wise spending charts (Pie charts)

[ ] Monthly summary reports

[ ] Export data to CSV/Excel

[ ] Authentication (Login/Password)

[ ] Responsive layout adjustments