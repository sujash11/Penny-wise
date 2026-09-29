import create
import display
import total

expense_ledger = []

while True:
    print('=== Personal Expense Tracker ===')
    print('1. Record New Expense')
    print('2. Display Expense History')
    print('3. Calculate Total Spending')
    print('4. Exit Application')
    
    user_selection = input('Please select an option (1-4): ')
    
    if user_selection == '1':
        create.add_expense(expense_ledger)
    elif user_selection == '2':
        display.show_expenses(expense_ledger)
    elif user_selection == '3':
        total.show_total(expense_ledger)
    elif user_selection == '4':
        print('Shutting down the tracker...')
        print('Goodbye! Tracker session ended successfully.')
        break
    else:
        print('Invalid selection. Please choose a number between 1 and 4.')