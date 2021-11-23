from django.db import models

# Create your models here.
class Animal(models.Model):
    name = models.CharField(max_length=100)
    leg = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    height = models.PositiveIntegerField()
    speed = models.PositiveIntegerField()
    family = models.ForeignKey('Family', on_delete=models.CASCADE)

class Family(models.Model):
    name = models.CharField(max_length=200)


