from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from . import views

from . models import Osoba
from rest_framework import status


class OsobaTests(APITestCase):
    def post_osoba(self, nazwisko):
        url = reverse(views.OsobaList.name)
        dane = {'nazwisko': nazwisko}
        response = self.client.post(url, dane, format='json')
        return response

    def test_post_and_get_osoba(self):
        nowe_nazwisko = 'Kowalski'
        response = self.post_osoba(nowe_nazwisko)
        assert response.status_code == status.HTTP_201_CREATED
        assert Osoba.objects.count() == 1
        assert Osoba.objects.get().nazwisko == nowe_nazwisko