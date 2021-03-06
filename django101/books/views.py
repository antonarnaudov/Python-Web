# Create your views here.
from django.shortcuts import render, redirect

from books.forms import BookForm
from books.models import Book


def index(request):
    context = {
        'books': Book.objects.all(),

    }
    return render(request, 'books_app/index.html', context)


def persist(request, book, template_name):
    if request.method == 'GET':
        context = {
            'form': BookForm(instance=book),
        }

        return render(request, f'books_app/{template_name}.html', context)
    else:
        form = BookForm(request.POST, instance=book)

        if form.is_valid():
            form.save()
            return redirect('books index')

        context = {
            'form': form,
        }

        return render(request, f'books_app/{template_name}.html', context)


def create(request):
    return persist(request, Book(), 'create')


def edit(request, pk):
    return persist(request, Book.objects.get(pk=pk), 'edit')

# def create(request):
#     if request.method == 'GET':
#         context = {
#             'form': BookForm(),
#         }
#
#         return render(request, 'books_app/create.html', context)
#     else:
#         form = BookForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('books index')
#         context = {
#             'form': form,
#         }
#         return render(request, 'books_app/create.html', context)
#
#
# def edit(request, pk):
#     book = Book.objects.get(pk=pk)
#
#     if request.method == 'GET':
#         form = BookForm(instance=book)
#         context = {
#             'form': form,
#         }
#
#         return render(request, 'books_app/edit.html', context)
#     else:
#         form = BookForm(request.POST, instance=book)
#
#         if form.is_valid():
#             form.save()
#             return redirect('books index')
#
#         context = {
#             'form': form,
#         }
#
#         return render(request, 'books_app/edit.html', context)
