from django.db import models

# Create your models here.
class Curri(models.Model):
    title= models.CharField(max_length=40)

    def __str__(self):
        return f'{self.id}:{self.title}'