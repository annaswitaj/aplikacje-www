from django.urls import path
from . import views

urlpatterns = [
    path('osoby', views.OsobaList.as_view(), name=views.OsobaList.name),
    path('osoby/<int:pk>', views.OsobaDetail.as_view(), name=views.OsobaDetail.name),
    path('samochody', views.SamochodList.as_view(), name=views.SamochodList.name),
    path('samochody/<int:pk>', views.SamochodDetail.as_view(), name=views.SamochodDetail.name),
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name)
    ]

