from django.db import models

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=50)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    year = models.IntegerField()

    def __str__(self):
        return self.name