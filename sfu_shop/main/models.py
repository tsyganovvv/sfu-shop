from django.db import models

# Create your models here.
class User(models.Model):
    username = models .CharField(max_length=128, unique=True)
    password = models .CharField(max_length=128, unique=False)
    
    def __str__(self):
        return f'username: {self.username} | password: {self.password}'