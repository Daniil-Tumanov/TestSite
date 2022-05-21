from django.db import models


# Create your models here.
class Users(models.Model):
    FullName = models.CharField(max_length=150)
    Login = models.CharField(max_length=150)
    Email = models.EmailField(max_length=150)
    Password = models.CharField(max_length=150)


    def __str__(self):
        return self.FullName
