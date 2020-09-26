from django.urls import path

from Routelcom.views import routelcom

urlpatterns = [
    path('', routelcom)
]
