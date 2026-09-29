def add_expense(expense_ledger):
    item_name = input("what did you buy?")
    while True:
        try:
            item_cost = float(input("what was the cost?"))
            break
        except ValueError:
            print("please enter a valid number")
            
    expense_ledger.append({'item': item_name, 'cost': item_cost})
    print('succesfully added', item_name, 'at', item_cost)