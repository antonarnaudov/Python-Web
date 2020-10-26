from django.contrib import admin

# Register your models here.
from expenses_tracker.models import Expenses

admin.site.register(Expenses)
