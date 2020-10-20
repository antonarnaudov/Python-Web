from django import forms


class TodoForm(forms.Form):
    title = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Do the chores'
            },
        ),
        # placeholder='Do the chores',
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
    )


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
