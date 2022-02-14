from django.db import models
from django.db.models.aggregates import Max

# Create your models here.

class Employ(models.Model):
    Name = models.CharField(max_length=150)
    Lastname = models.CharField(max_length=150)

    def __str__(self):
        return self.Lastname


class Account(models.Model):

    GenereChoices = (
        ("Man", "Masculine"),
        ("Woman", "Femenine"),
        ("Indistint", "Indistint"),
    )

    Username = models.CharField(max_length=150)
    Password = models.CharField(max_length=400)
    Email = models.CharField(max_length=150)
    Salt = models.CharField(max_length=400, default='')

    def __str__(self):
        return self.Username
