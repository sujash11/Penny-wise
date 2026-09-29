def show_expenses(expense_ledger):
    print('---my expenses---')
    if len(expense_ledger) == 0:
        print('you havent added anything yet')
    else:
        for record in expense_ledger:
            print(record['item'], ':', record['cost'])
            