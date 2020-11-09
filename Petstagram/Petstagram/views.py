from django.shortcuts import render, redirect

# Create your views here.
from pets.forms import CommentForm
from pets.models import Pet, Like, Comment


def pets_list(request):
    context = {
        'pets': Pet.objects.all(),
    }
    return render(request, 'pets/pets_list.html', context)


def details_or_comment_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'pet': pet,
            'form': CommentForm(),
        }
        return render(request, 'pets/pet_details.html', context)
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(text=form.cleaned_data['text'])
            comment.pet = pet
            comment.save()
            # pet.comment_set.all(comment)
            # pet.save()
            redirect('pet details or comment', pk)

        context = {
            'pet': pet,
            'form': CommentForm(),
        }
        return render(request, 'pets/pet_details.html', context)


def like_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    like = Like()
    like.pet = pet
    like.save()

    return redirect('details', pk)


def edit_pet(request, pk):
    return render(request, 'pet_edit.html')


def delete_pet(request, pk):
    return render(request, 'pet_delete.html')
