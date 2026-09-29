# Personal Expense Tracker

## Overview
The Personal Expense Tracker is a modular Command Line Interface (CLI) application built in Python. It allows users to easily log their daily expenditures, view their transaction history, and calculate their total spending in a single session. 

## Features
* **Record New Expense:** Securely input item names and costs with built-in error handling for invalid data entries.
* **Display Expense History:** View a complete, itemized ledger of all recorded expenses in the current session.
* **Calculate Total Spending:** Instantly aggregate and display the total sum of all financial transactions.
* **Modular Design:** The application logic is separated into distinct, manageable files (`create.py`, `display.py`, `total.py`, and the main script) for high maintainability.

## Technologies Used
* **Language:** Python 3.x
* **Interface:** Command Line Interface (CLI)

## Steps to Install & Run
1. Clone or download the repository to your local machine.
2. Ensure you have Python 3.x installed.
3. Verify that all Python files (`create.py`, `display.py`, `total.py`, and your main execution file) are in the same directory.
4. Open your terminal or command prompt.
5. Navigate to the project directory.
6. Run the main application file using the command:
   `python main.py` (replace `main.py` with your main file's name).

## Instructions for Testing
1. Launch the application.
2. Select option `1` and enter a valid item (e.g., "Lunch") and a numeric cost (e.g., "15.50"). Verify the success message.
3. Select option `1` again and enter an invalid cost (e.g., "fifteen"). Verify that the system catches the `ValueError` and prompts you for a valid number.
4. Select option `2` to ensure the ledger displays the previously entered items accurately.
5. Select option `3` to verify the total sum calculates correctly.
6. Select option `4` to successfully terminate the application loop.

## Screenshots
*(Optional: Add screenshots of the CLI menu and output here prior to final submission)*
