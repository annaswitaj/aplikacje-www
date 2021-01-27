from rest_framework import serializers
from .models import Osoba, Samochod


class OsobaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Osoba
        fields = ['id', 'imie', 'nazwisko', 'data_urodzenia', 'zarobki']

class SamochodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Samochod
        fields = ['id', 'marka', 'model', 'pojemnosc', 'rok_produkcji', 'wlasciciel']