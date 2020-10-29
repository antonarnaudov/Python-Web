from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST

from app.common.budget_calculation import budget_left
from app.forms import ProfileForm
from app.models import Profile, Expenses


def profile_view(request):
    profile = Profile.objects.all()[0]
    expenses = Expenses.objects.all()

    profile.budget_left = budget_left(profile, expenses)

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
    profile = Profile.objects.all()[0]
    if request.method == 'GET':

        context = {
            'form': ProfileForm(instance=profile)
        }
        return render(request, 'profile/profile-edit.html', context)

    else:
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile view')

        context = {
            'form': ProfileForm(instance=profile)
        }
        return render(request, 'profile/profile-edit.html', context)


def profile_delete(request):
    if request.method == 'GET':
        return render(request, 'profile/profile-delete.html')
    else:
        profile = Profile.objects.all()[0]
        expenses = Expenses.objects.all()

        profile.delete()
        expenses.delete()
        return redirect('home page')
