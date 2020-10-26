from django.urls import path

from expenses_tracker.views import home_page, expense_create, expense_delete, expense_edit

urlpatterns = [
    path('', home_page, name='home page'),
    path('create/', expense_create, name='expense create'),
    path('edit/<int:pk>', expense_edit, name='expense edit'),
    path('delete/<int:pk>', expense_delete, name='expense delete'),
]
