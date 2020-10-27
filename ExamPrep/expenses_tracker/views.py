from django.shortcuts import render, redirect

from expenses_tracker.forms import ExpensesForm
from expenses_tracker.models import Expenses
from profile.models import Profile


# Create your views here.


def home_page(request):
    profile = Profile.objects.all()
    if profile:

        expenses = Expenses.objects.all()
        if expenses:
            context = {
                'profile': profile,
                'expenses': expenses,
            }
            return render(request, 'home-with-profile.html', context)

        context = {
            'profile': profile,

        }

        return render(request, 'home-with-profile-no-expense.html', context)
    return render(request, 'home-no-profile.html')


def create_or_edit(request, expense, template_name):
    if request.method == 'GET':
        context = {
            'form': ExpensesForm(instance=expense),
        }
        return render(request, f'{template_name}.html', context)
    else:
        form = ExpensesForm(request.POST, instance=expense)

        if form.is_valid():
            form.save()
            return redirect('home page')

        context = {
            'form': form,
        }

        return render(request, f'{template_name}.html', context)


def expense_create(request):
    return create_or_edit(request, Expenses(), 'expense-create')


def expense_edit(request, pk):
    return create_or_edit(request, Expenses(pk=pk), 'expense-edit')


def expense_delete(request, pk):
    return render(request, 'expense-delete.html')
