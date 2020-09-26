from django.contrib.auth.models import User
from django.shortcuts import render


# Create your views here.

def routelcom(request):
    context = {
        'title': 'Routelcom',
        'users': User.objects.all(),
    }

    return render(request, 'routelcom.html', context)
