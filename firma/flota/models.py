from django.db import models


# Create your models here.
class Osoba(models.Model):
    imie = models.CharField(max_length=60, null=False)
    nazwisko = models.CharField(max_length=60, null=False)
    data_urodzenia = models.DateField()
    zarobki = models.DecimalField(max_digits=10, decimal_places=2, default=4000)
