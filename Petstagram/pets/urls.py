from django.urls import path

from Petstagram.views import pets_list, like_pet, details_or_comment_pet, edit_pet, delete_pet

urlpatterns = [
    path('', pets_list, name='pets_list'),
    path('details/<int:pk>/', details_or_comment_pet, name='pet details or comment'),
    path('like/<int:pk>/', like_pet, name='like'),
    path('comment/<int:pk>/', details_or_comment_pet, name='pet details or comment'),
    path('edit/<int:pk>/', edit_pet, name='edit pet'),
    path('delete/<int:pk>/', delete_pet, name='delete pet'),
]
