from django import forms
# Create your views here.
from django.shortcuts import render

from books.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

        widgets = {
            # 'title': forms.CharField(
            #     required=True,
            #     attrs={
            #         'class': 'form-control',
            #         'placeholder': 'My title',
            #     }
            # ),
            # 'description': forms.TextInput(attrs={
            #     'class': 'form-control',
            #     'placeholder': 'Enter description',
            # })
        }


def index(request):
    context = {
        'books': Book.objects.all(),

    }
    return render(request, 'books_app/index.html', context)


def create(request):
    if request.method == 'GET':
        context = {
            'form': BookForm()
        }
        return render(request, 'books_app/create.html', context)
    else:
        pass


def edit(request, pk):
    return render(request, 'books_app/edit.html')
