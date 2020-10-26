from django.urls import path

from profile.views import profile, profile_edit, profile_delete, profile_create

urlpatterns = [
    path('', profile),
    path('create/', profile_create, name='profile create'),
    path('edit/', profile_edit, name='profile edit'),
    path('delete/', profile_delete, name='profile delete'),
]
