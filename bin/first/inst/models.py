from django.db import models

# Create your models here.
class Inst(models.Model):
    name = models.CharField(max_length=65)
    surname = models.CharField(max_length=64)
    course = models.CharField(max_length=64)