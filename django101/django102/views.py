from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from django102.models.game import Game
from django102.models.person import Person
from django102.models.player import Player


def something(request):
    return HttpResponse('<u>It Works!</u>')


def inheritance(request):
    context = {
        'title': 'Inherited design pattern',
    }
    return render(request, 'inheritance.html', context)


def index(request):
    title = 'SoftUni Django 101'
    users = User.objects.all()
    games = Game.objects.all_with_players_count()

    context = {
        'title': title,
        'users': users,
        'games': games,
    }

    return render(request, 'index.html', context)


class UsersListView(ListView):
    model = User
    template_name = 'index2.html'
    queryset = User.objects.all().order_by('-username')

    def get_context_object_name(self, object_list):
        return 'users'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = 'From class view'
        return context


class GamesListView(ListView):
    model = Game
    template_name = 'games.html'
