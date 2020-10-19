from django.urls import path

from Petstagram.views import pets_list, like_pet, show_pet_details

urlpatterns = [
    path('', pets_list, name='pets_list'),
    path('details/<int:pk>/', show_pet_details, name='details'),
    path('like/<int:pk>/', like_pet, name='like'),
]
