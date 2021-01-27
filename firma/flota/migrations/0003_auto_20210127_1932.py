# Generated by Django 3.1.5 on 2021-01-27 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flota', '0002_samochod'),
    ]

    operations = [
        migrations.AddField(
            model_name='osoba',
            name='email',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='samochod',
            name='wlasciciel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='samochody', to='flota.osoba'),
        ),
    ]