from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.http import require_POST

from app.common.calculate_budget import budget_left
from app.common.get_model import get_profile, get_all_expenses
from app.forms import ProfileForm


def profile_view(request):
    profile = get_profile()
    profile.budget_left = budget_left(profile.budget, get_all_expenses())
    context = {
        'profile': profile
    }
    return render(request, 'profile/profile.html', context)


@require_POST
def profile_create(request):
    form = ProfileForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('home page')


def profile_edit(request):
    profile = get_profile()
    if request.method == 'GET':
        context = {
            'form': ProfileForm(instance=profile)
        }
        return render(request, 'profile/profile-edit.html', context)
    else:
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')

        context = {
            'form': ProfileForm(instance=profile)
        }
        return render(request, 'profile/profile-edit.html', context)


def profile_delete(request):
    if request.method == 'GET':
        return render(request, 'profile/profile-delete.html')
    else:
        profile = get_profile()
        expenses = get_all_expenses()

        profile.delete()
        expenses.delete()
        return redirect('home page')
