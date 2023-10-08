from django.db import models


class Emp(models.Model):
    id = models.BigAutoField(primary_key=True)  # Specify primary_key=True for id field
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    address = models.TextField()


def __str__(self):
    return self.name
