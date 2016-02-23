from django.db import models

# Create your models here.

class Stat(models.Model):
    name = models.CharField(max_length=50)
    receptions = models.IntegerField()
    receiving_yards = models.IntegerField()
    touchdowns = models.IntegerField()
    position = models.CharField(max_length=4)

    def __str__(self):
        return self.name
