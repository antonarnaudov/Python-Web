from django.shortcuts import render, redirect

from app.forms import ExpensesForm, DeleteExpensesForm
from app.models import Expenses


def create_or_edit(request, expenses, template_name):
    if request.method == 'GET':
        context = {
            'expenses': expenses,
            'form': ExpensesForm(instance=expenses),
        }
        return render(request, template_name, context)

    else:
        form = ExpensesForm(request.POST, instance=expenses)
        if form.is_valid():
            form.save()
            return redirect('home page')

        context = {
            'expenses': expenses,
            'form': ExpensesForm(instance=expenses),
        }
        return render(request, template_name, context)


def expenses_create(request):
    return create_or_edit(request, Expenses(), 'expense/expense-create.html')


def expenses_edit(request, pk):
    expenses = Expenses.objects.get(pk=pk)
    return create_or_edit(request, expenses, 'expense/expense-edit.html')


def expenses_delete(request, pk):
    expense = Expenses.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'form': DeleteExpensesForm(instance=expense),
            'expense': expense
        }
        return render(request, 'expense/expense-delete.html', context)
    else:
        expense.delete()
        return redirect('home page')
