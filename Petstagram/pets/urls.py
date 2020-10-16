from django.urls import path

from Petstagram.views import pets_list, pet_details, like_pet

urlpatterns = [
    path('', pets_list, name='pets_list'),
    path('details/', pet_details, name='details'),
    path('like/', like_pet, name='like'),

]
