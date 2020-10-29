from django.shortcuts import render

from app.common.budget_calculation import budget_left
from app.forms import ProfileForm
from app.models import Profile, Expenses


def home_page(request):
    profile = Profile.objects.first()
    if profile:
        expenses = Expenses.objects.all()

        profile.budget_left = budget_left(profile, expenses)

        context = {
            'profile': profile,
            'expenses': expenses,
        }
        return render(request, 'home/home-with-profile.html', context)

    context = {
        'form': ProfileForm,
    }
    return render(request, 'home/home-no-profile.html', context)
