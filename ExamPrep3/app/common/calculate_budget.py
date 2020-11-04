def budget_left(budget, expenses):
    all_expenses = sum(expense.price for expense in expenses)
    return budget - all_expenses
