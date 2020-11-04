from django.urls import path

from app.views.expenses_view import expenses_create, expenses_edit, expenses_delete
from app.views.home_view import home_page
from app.views.profile_view import profile_create, profile_view, profile_delete, profile_edit

urlpatterns = [
    # Home
    path('', home_page, name='home page'),

    # Profile
    path('profile', profile_view, name='profile'),
    path('profile/create/', profile_create, name='profile create'),
    path('profile/edit/', profile_edit, name='profile edit'),
    path('profile/delete/', profile_delete, name='profile delete'),

    # Expenses
    path('create/', expenses_create, name='expenses create'),
    path('edit/<int:pk>', expenses_edit, name='expenses edit'),
    path('delete/<int:pk>', expenses_delete, name='expenses delete')
]
