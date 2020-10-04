from django.db import models


# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    password = models.CharField(max_length=40)

    class Meta:
        db_table = 'registered_users'
