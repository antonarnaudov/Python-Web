from django.contrib import admin

# Register your models here.
from app.models import Profile, Expenses

admin.site.register(Profile)
admin.site.register(Expenses)