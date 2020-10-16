from django.db import models


# Create your models here.

class Pet(models.Model):
    DOG = 'Dog'
    CAT = 'Cat'
    PARROT = 'Parrot'
    UNKNOWN = 'Unknown'

    PET_TYPES = (
        (DOG, 'Dog'),
        (CAT, 'Cat'),
        (PARROT, 'Parrot'),
        (UNKNOWN, 'Unknown')
    )

    type = models.CharField(max_length=7, choices=PET_TYPES, default=UNKNOWN)
    name = models.CharField(max_length=7, blank=False)
    age = models.IntegerField(blank=False)
    description = models.TextField(blank=False)
    image_url = models.URLField(blank=False)

    def __str__(self):
        return f'Id {self.id}: {self.type} {self.name}'


class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
