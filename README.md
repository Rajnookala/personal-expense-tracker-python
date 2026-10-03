# Personal Expense Tracker

A beginner-friendly command-line application built with Python to record, manage, and analyze personal expenses.

## Features

- Add new expenses
- View all expenses
- Calculate total spending
- View spending by category
- View monthly spending summary
- Store expense data permanently in a CSV file
- Validate dates and expense amounts
- Simple command-line interface

## Technologies Used

- Python 3
- CSV module
- File handling
- Functions
- Exception handling
- Date and time handling

## Project Structure

```text
expense-tracker/
├── expense_tracker.py
├── expenses.csv
├── requirements.txt
└── README.md
```

## How to Run

### 1. Install Python

Download Python from:

https://www.python.org/downloads/

Make sure Python is added to PATH during installation.

### 2. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 3. Open the project

```bash
cd expense-tracker
```

### 4. Run the application

Windows:

```bash
python expense_tracker.py
```

If `python` does not work, try:

```bash
py expense_tracker.py
```

## Example

```text
========================================
       PERSONAL EXPENSE TRACKER
========================================
1. Add Expense
2. View All Expenses
3. Show Total Spending
4. Category Summary
5. Monthly Summary
6. Exit

Enter your choice (1-6): 1

--- Add Expense ---
Date (YYYY-MM-DD, press Enter for today): 2026-10-03
Category (Food/Travel/Shopping/Bills/Other): Food
Description: Dinner
Amount: 350

Expense added successfully!
```

## Future Improvements

- Add a graphical user interface using Tkinter
- Add charts using Matplotlib
- Add SQLite database support
- Add login/user authentication
- Export monthly reports to Excel

## Resume Description

**Personal Expense Tracker | Python**

Developed a command-line expense management application using Python to record, categorize, search, and analyze personal expenses. Implemented CSV-based data persistence, input validation, expense summaries, and monthly spending calculations.

## Skills Demonstrated

Python, File Handling, CSV, Functions, Exception Handling, Data Processing, Input Validation, CLI Application Development
