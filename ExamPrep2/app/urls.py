from django.urls import path

from app.views.expense_views import expenses_create, expenses_edit, expenses_delete
from app.views.home_views import home_page
from app.views.profile_views import profile_create, profile_view, profile_edit, profile_delete

urlpatterns = [
    # Home
    path('', home_page, name='home page'),

    # Expenses
    path('expenses/create/', expenses_create, name='expenses create'),
    path('expenses/edit/<int:pk>/', expenses_edit, name='expenses edit'),
    path('expenses/delete/<int:pk>/', expenses_delete, name='expenses delete'),

    # Profile
    path('profile', profile_view, name='profile view'),
    path('profile/create/', profile_create, name='profile create'),
    path('profile/edit/', profile_edit, name='profile edit'),
    path('profile/delete', profile_delete, name='profile delete')
]
