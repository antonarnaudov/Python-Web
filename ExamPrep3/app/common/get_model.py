from app.models import Profile, Expenses


def get_profile():
    return Profile.objects.first()


def get_empty_expense():
    return Expenses()


def get_all_expenses():
    return Expenses.objects.all()


def get_expense_by_pk(pk):
    return Expenses.objects.get(pk=pk)
