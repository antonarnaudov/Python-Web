# Create your views here.
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from profile.forms import ProfileForm
from profile.models import Profile


def profile(request):
    return render(request, 'profile.html')


def profile_edit(request):
    return render(request, 'profile-edit.html')


def profile_delete(request):
    return render(request, 'profile-delete.html')


@require_POST
def profile_create(request):
    form = ProfileForm(request.POST)
    if form.is_valid():
        new_profile = Profile(
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            budget=form.cleaned_data['budget'],
        )
        new_profile.save()
        return redirect('home page')
