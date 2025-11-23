Personal Expense Tracker (Tkinter GUI)

A clean, elegant, and fully functional Personal Expense Tracker built using Python Tkinter.
This application allows users to add income and expenses, track their current balance, and view detailed transaction history — all stored persistently using a JSON file.

🚀 Features
✔ Modern Dark-Themed GUI

A classy matte-black interface with clean buttons, cards, and spacing.

✔ Add Income & Expenses

Popup windows allow users to add:

Amount

Note/description

Timestamp (auto-generated)

✔ Live Balance Calculation

Real-time updates to your current balance after each transaction.

✔ Transaction History

Scrollable list showing:

Date & Time

Note

Income (+) or Expense (–)

Clean formatted entries

✔ Persistent Storage (JSON)

All transactions are stored in transactions.json, and loaded automatically every time the app starts.

📂 Project Structure
Personal-Expense-Tracker/
│
├── main.py                 # Main Tkinter GUI Application
├── transactions.json       # Auto-generated JSON storage
└── README.md               # Project documentation

🧠 How It Works (Flow)

1️⃣ Load Data
Reads all previous transactions from transactions.json.

2️⃣ Show Dashboard
Displays:

Current balance

Scrollable transaction list

3️⃣ Add Income/Expense
User enters amount + note in popup form.

4️⃣ Save to JSON
Every transaction is appended and stored permanently.

5️⃣ Update UI
Balance and transaction list refresh instantly.

🛠️ Technologies Used
Component	Purpose
Python	Core language
Tkinter	GUI framework
JSON	Persistent storage
datetime	Automatic timestamps
▶️ How to Run the Project
Step 1 — Install Python

Requires Python 3.8+

Step 2 — Run the Program
python main.py

Step 3 — Start Tracking!

The GUI opens instantly with:

Title

Balance card

Add buttons

Transaction list

🔄 Reset JSON Data (Optional)

If you want to clear all transactions only once, delete or empty transactions.json.

Empty version:

[]


Or programmatically:

open("transactions.json", "w").write("[]")



📌 Future Improvements (Optional)

Category-wise spending charts

Monthly summary

Export to CSV/Excel

Login/Password screen

Rounded-corner UI

Mobile-like responsive layout