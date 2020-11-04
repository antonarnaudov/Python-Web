from django.shortcuts import render, redirect

# Create your views here.
from app.common.get_model import get_expense_by_pk, get_empty_expense
from app.forms import ExpensesForm, ExpensesFormDisabled


def create_or_edit(request, expenses, template):
    if request.method == 'GET':
        context = {
            'form': ExpensesForm(instance=expenses),
            'expenses': expenses
        }
        return render(request, template, context)
    else:
        form = ExpensesForm(request.POST, instance=expenses)
        if form.is_valid():
            form.save()
            return redirect('home page')

        context = {
            'form': ExpensesForm(instance=expenses),
            'expenses': expenses
        }
        return render(request, template, context)


def expenses_create(request):
    return create_or_edit(request, get_empty_expense(), 'expense/expense-create.html')


def expenses_edit(request, pk):
    return create_or_edit(request, get_expense_by_pk(pk), 'expense/expense-edit.html')


def expenses_delete(request, pk):
    expenses = get_expense_by_pk(pk)
    if request.method == 'GET':
        context = {
            'form': ExpensesFormDisabled(instance=expenses),
            'expenses': expenses
        }
        return render(request, 'expense/expense-delete.html', context)
    else:
        expenses.delete()
        return redirect('home page')
