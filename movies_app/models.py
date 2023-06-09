from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=50, null=True)
    order = models.IntegerField(null=True)
    description = models.CharField(max_length=1024, null=True)

    def __str__(self) -> str:
        return f'{self.order} - {self.title}'


class Character(models.Model):
    firstname = models.CharField(max_length=50, null=True)
    lastname = models.CharField(max_length=50, null=True)

    def __str__(self) -> str:
        return f'{self.firstname} {self.lastname}'