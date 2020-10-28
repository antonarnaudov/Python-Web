# Create your views here.
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from common.budget_calculation import budget_left
from expenses_tracker.models import Expenses
from profile.forms import ProfileForm
from profile.models import Profile


@require_POST
def profile_create(request):
    form = ProfileForm(request.POST)

    if form.is_valid():
        form.save()
        return redirect('home page')


def profile_view(request):
    (profile, expenses) = (Profile.objects.all()[0], Expenses.objects.all())
    profile.budget_left = budget_left(profile, expenses)

    context = {
        'profile': profile,
    }
    return render(request, 'profile.html', context)


def profile_edit(request):
    profile = Profile.objects.all()[0]

    if request.method == 'GET':
        context = {
            'form': ProfileForm(instance=profile),
        }
        return render(request, 'profile-edit.html', context)

    else:
        form = ProfileForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()
            return redirect('profile')

        context = {
            'form': ProfileForm(instance=profile),
        }
        return render(request, 'profile-edit.html', context)


def profile_delete(request):
    profile = Profile.objects.all()[0]

    if request.method == 'GET':
        context = {
            'form': ProfileForm(instance=profile)
        }

        return render(request, 'profile-delete.html', context)
    else:
        profile.delete()
        [expense.delete() for expense in Expenses.objects.all()]
        return redirect('home page')
