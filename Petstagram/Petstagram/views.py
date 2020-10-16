from django.shortcuts import render, redirect


# Create your views here.
from pets.models import Pet


def pets_list(request):
    context = {
        'pets': Pet.objects.all(),
    }
    return render(request, 'pets/pets_list.html', context)


def pet_details(request):
    context = {

    }
    return render(request, 'pets/pet_details.html', context)


def like_pet(request):
    return redirect('')
