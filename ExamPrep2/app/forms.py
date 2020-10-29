from django import forms

from app.common.disabled_form_mixin import DisabledFormMixin
from app.models import Profile, Expenses


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ExpensesForm(forms.ModelForm):
    class Meta:
        model = Expenses
        fields = '__all__'


class DeleteExpensesForm(ExpensesForm, DisabledFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        DisabledFormMixin.__init__(self)
