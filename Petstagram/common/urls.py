from django.urls import path

from common.views import landing_page, login_form, register_form

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('register/', register_form, name='register'),
    path('login/', login_form, name='login'),
]
