from django.shortcuts import render, redirect


# Create your views here.
from pets.models import Pet, Like


def pets_list(request):
    context = {
        'pets': Pet.objects.all(),
    }
    return render(request, 'pets/pets_list.html', context)


def show_pet_details(request, pk):
    context = {
        'pet': Pet.objects.get(pk=pk)
    }
    return render(request, 'pets/pet_details.html', context)


def like_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    like = Like()
    like.pet = pet
    like.save()

    return redirect('details', pk)
