from django import forms

from expenses_tracker.models import Expenses


class DisabledFormMixin:
    def __init__(self):
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = True
            field.widget.attrs['readonly'] = True


class ExpensesForm(forms.ModelForm):
    class Meta:
        model = Expenses
        fields = '__all__'


class DeleteExpensesForm(ExpensesForm, DisabledFormMixin):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        DisabledFormMixin.__init__(self)
