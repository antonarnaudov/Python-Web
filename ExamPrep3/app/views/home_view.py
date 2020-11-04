from django.shortcuts import render

# Create your views here.
from app.common.calculate_budget import budget_left
from app.common.get_model import get_profile, get_all_expenses
from app.forms import ProfileForm


def home_page(request):
    profile = get_profile()
    if profile:
        expenses = get_all_expenses()
        profile.budget_left = budget_left(profile.budget, expenses)

        context = {
            'expenses': expenses,
            'profile': profile,
        }
        return render(request, 'home/home-with-profile.html', context)

    context = {
        'form': ProfileForm,
    }
    return render(request, 'home/home-no-profile.html', context)
