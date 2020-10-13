from django.urls import path, include

from todos_app.views import index

urlpatterns = [
    path('', index)
]