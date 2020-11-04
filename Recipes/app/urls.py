from django.urls import path

from app.views import index, create, edit, delete, details

urlpatterns = [
    path('', index, name='home page'),
    path('create/', create, name='create'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('details/<int:pk>/', details, name='details')
]
