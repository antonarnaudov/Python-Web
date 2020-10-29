def budget_left(profile, expenses):
    expenses_cost = sum(e.price for e in expenses)
    return profile.budget - expenses_cost
