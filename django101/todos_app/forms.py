from django import forms

from todos_app.validators import min_validator


class TodoForm(forms.Form):
    title = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Do the chores'
            },
        ),
    )

    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Make your bed\nWash the dishes',
            },
        ),
        required=False,
        label='The Desc',
        validators=[
            min_validator,
        ]
    )

    bot_catcher = forms.CharField(
        widget=forms.HiddenInput,
        required=False,
    )

    def clean_bot_catcher(self):
        if len(self.cleaned_data['bot_catcher']):
            raise forms.ValidationError('This is a bot')

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for (_, field) in self.fields.items():
    #         if 'class' in field.widget.attrs:
    #             value = field.widget.attrs['class'] + ' form-control'
    #         else:
    #             value = ' form-control'
    #         field.widget.attrs['class'] = value

# class TodoFormFull(forms.Form):
#     title = forms.CharField(
#         max_length=30,
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'form-control'
#             }
#         )
#     )
#
#     description = forms.CharField(
#         widget=forms.Textarea(
#             attrs={
#                 'class': 'form-control'
#             }
#         ),
#         required=False,
#         label='The Desc',
#     )
#     my_password = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={
#                 'class': 'form-control'
#             }
#         ),
#     )
#     age = forms.IntegerField(
#         widget=forms.NumberInput(
#             attrs={
#                 'class': 'form-control'
#             }
#         ),
#     )
#     size = forms.IntegerField(
#         widget=(forms.TextInput(
#             attrs={
#                 'type': 'range',
#                 'class': 'form-control',
#             }
#         )
#         )
#     )
