from django import forms

from app.models import Profile, Expenses


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ExpensesForm(forms.ModelForm):
    class Meta:
        model = Expenses
        fields = '__all__'


class ExpensesFormDisabled(ExpensesForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = True
            field.widget.attrs['readonly'] = True
