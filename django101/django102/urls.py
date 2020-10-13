from django.urls import path

from django102.views import index, UsersListView, GamesListView, something, inheritance

urlpatterns = [
    path('', index, name='index'),
    path('2/', UsersListView.as_view()),
    path('games/', GamesListView.as_view()),
    path('smth/', something),
    path('inheritance/', inheritance),
]
