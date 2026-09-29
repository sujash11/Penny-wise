def show_total(expense_ledger):
    grand_total = 0
    for record in expense_ledger:
        grand_total += record['cost']
    print("total money spent so far :", grand_total)