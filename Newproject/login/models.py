from django.db import models

# Create your models here.
class register(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=50)
    phone = models.IntegerField()
    password = models.CharField(max_length=60)
