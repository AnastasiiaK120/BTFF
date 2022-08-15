from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=10)
    points = models.IntegerField(default=0)
    image = models.ImageField(upload_to='', null=True)

    def __str__(self):
        return str(self.name)


class Roster(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return str(self.name)