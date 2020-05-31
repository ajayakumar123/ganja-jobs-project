from django.db import models

# Create your models here.


class Student(models.Model):

    name=models.CharField("Name",max_length=24)
    marks=models.IntegerField("Marks")
    country=models.CharField("Country",max_length=24,default='India')

    def __str__(self):
        return self.name

