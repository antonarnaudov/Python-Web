from django.urls import path

from profile.views import profile_view, profile_edit, profile_delete, profile_create

urlpatterns = [
    path('', profile_view, name='profile'),
    path('create/', profile_create, name='profile create'),
    path('edit/', profile_edit, name='profile edit'),
    path('delete/', profile_delete, name='profile delete'),
]
