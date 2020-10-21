from django import forms


def min_validator(value):
    if not value or len(value) < 10:
        raise forms.ValidationError(f'Value should be more than 10 characters, now it is {len(value)}')
