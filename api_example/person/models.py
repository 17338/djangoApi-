from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50)
    birthday = models.CharField(max_length=50)
    adress = models.CharField(max_length=50)

    def __str__(self):
        return self.name