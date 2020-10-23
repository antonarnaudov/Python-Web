# Create your views here.
from django.shortcuts import render, redirect

from books.forms import BookForm
from books.models import Book


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
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('books index')
        context = {
            'form': form,
        }
        return render(request, 'books_app/create.html', context)


def edit(request, pk):
    return render(request, 'books_app/edit.html')
