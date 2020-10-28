from django.shortcuts import render, redirect

from common.budget_calculation import budget_left
from expenses_tracker.forms import ExpensesForm, DeleteExpensesForm
from expenses_tracker.models import Expenses
from profile.forms import ProfileForm
from profile.models import Profile


def home_page(request):
    # if Profile.objects.exists():
    profile = Profile.objects.first()
    if profile:
        expenses = Expenses.objects.all()

        profile.budget_left = budget_left(profile, expenses)

        context = {
            'profile': profile,
            'expenses': expenses,
        }
        return render(request, 'home-with-profile.html', context)
    context = {
        'form': ProfileForm(),
    }
    return render(request, 'home-no-profile.html', context)


def create_or_edit(request, expense, template_name):
    if request.method == 'GET':
        context = {
            'form': ExpensesForm(instance=expense),
            'expense': expense,
        }
        return render(request, template_name, context)
    else:
        form = ExpensesForm(request.POST, instance=expense)

        if form.is_valid():
            form.save()
            return redirect('home page')
        context = {
            'form': ExpensesForm(instance=expense),
            'expense': expense,
        }
        return render(request, template_name, context)


def expense_create(request):
    return create_or_edit(request, Expenses(), 'expense-create.html')


def expense_edit(request, pk):
    expense = Expenses.objects.get(pk=pk)
    return create_or_edit(request, expense, 'expense-edit.html')


def expense_delete(request, pk):
    expense = Expenses.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'expense': expense,
            'form': DeleteExpensesForm(instance=expense),
        }
        return render(request, 'expense-delete.html', context)
    else:
        expense.delete()
        return redirect('home page')


'''EXPENSE CREATE WRITTEN SEPARATELY'''
# def expense_create(request):
#     if request.method == 'GET':
#         context = {
#             'form': ExpensesForm()
#         }
#         return render(request, 'expense-create.html', context)
#     else:
#         form = ExpensesForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#             return redirect('home page')
#
#         context = {
#             'form': form,
#         }
#         return render(request, 'expense-create.html', context)

'''EXPENSE EDT WRITTEN SEPARATELY'''
# def expense_edit(request, pk):
#     expense = Expenses.objects.get(pk=pk)
#
#     if request.method == 'GET':
#         context = {
#             'form': ExpensesForm(instance=expense),
#             'expense': expense,
#         }
#         return render(request, 'expense-edit.html', context)
#     else:
#         form = ExpensesForm(request.POST, instance=expense)
#
#         if form.is_valid():
#             form.save()
#             return redirect('home page')
#
#         context = {
#             'form': form,
#             'expense': expense,
#         }
#         return render(request, 'expense-edit.html', context)
