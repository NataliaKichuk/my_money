# My Money — Personal Finance Tracker
The project is in progress.

A lightweight web application built with **Django** and **PostgreSQL** (or SQLite) designed to help users track their daily financial activities. This project allows users to record incomes and expenses, categorize transactions, and monitor their current balance in real-time.

## Key Features
* **Transaction Management:** Add, view, and delete records for incomes and expenses.
* **Category System:** Organize your finances using customizable categories (e.g., Food, Salary, Rent).
* **Real-time Balance:** Automatically calculates the current balance based on all entries.
* **Data Validation:** Ensures no negative amounts or future dates for past transactions.

## Tech Stack
* **Backend:** Python 3.x, Django 6.x
* **Database:** PostgreSQL (Production) / SQLite (Development)
* **Environment:** Virtualenv, Pip

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/NataliaKichuk/my_money.git
   cd my_money
   
2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   
3. **Activate the virtual environment:**
   ```bash
   Windows: venv\Scripts\activate```
   
4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt```

5. **Apply database migrations:**
   ```bash
   python manage.py migrate```

6. **Create a superuser:**
   ```bash
   python manage.py createsuperuser

7. **Run the development server:**
   ```bash
   python manage.py runserver