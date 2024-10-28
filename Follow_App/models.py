from django.db import models

# Create your models here.
class Utilisateur(models.Model):
    mail = models.CharField(max_length = 30)
    login = models.CharField(max_length = 30)
