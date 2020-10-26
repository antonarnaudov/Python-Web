from django.shortcuts import render

from profile.models import Profile


# Create your views here.


def home_page(request):
    profile = Profile.objects.all()
    if profile:
        context = {
            'profile': profile
        }
        return render(request, 'home-with-profile.html', context)
    return render(request, 'home-no-profile.html')


def expense_create(request):
    return render(request, 'expense-create.html')


def expense_edit(request, pk):
    return render(request, 'expense-edit.html')


def expense_delete(request, pk):
    return render(request, 'expense-delete.html')
