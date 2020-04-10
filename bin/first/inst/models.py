from django.db import models

# Create your models here.

class Position(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Inst(models.Model):
    name = models.CharField(verbose_name=u'Instructor Name', max_length=65, help_text='This is name')
    surname = models.CharField(max_length=64)
    courses = models.ManyToManyField(Course)
    date_bith = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True, null=True)
    is_active = models.BooleanField(default=True)
    position = models.ForeignKey(Position, null=True)

    def __str__(self):
        return self.name + ' ' + self.surname

