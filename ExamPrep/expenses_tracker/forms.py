from django import forms

from expenses_tracker.models import Expenses


class ExpensesForm(forms.ModelForm):
    class Meta:
        model = Expenses
        fields = '__all__'
