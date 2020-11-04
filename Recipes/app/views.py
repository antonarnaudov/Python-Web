from django.shortcuts import render, redirect

from app.forms import RecipeForm, RecipeFormDisabled
from app.models import Recipe


def index(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, 'index.html', context)


def create_or_edit(request, recipes, template):
    if request.method == 'GET':
        context = {
            'form': RecipeForm(instance=recipes),
            'recipes': recipes
        }
        return render(request, template, context)
    else:
        form = RecipeForm(request.POST, instance=recipes)
        if form.is_valid():
            form.save()
            return redirect('home page')

        context = {
            'form': RecipeForm(instance=recipes),
            'recipes': recipes
        }
        return render(request, template, context)


def create(request):
    return create_or_edit(request, Recipe(), 'create.html')


def edit(request, pk):
    recipes = Recipe.objects.get(pk=pk)
    return create_or_edit(request, recipes, 'edit.html')


def delete(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'form': RecipeFormDisabled(instance=recipe),
            'recipe': recipe
        }
        return render(request, 'delete.html', context)
    else:
        recipe.delete()
        return redirect('home page')


def details(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    recipe.separated_ingredients = recipe.ingredients.split(',')
    context = {
        'recipe': recipe
    }
    return render(request, 'details.html', context)
