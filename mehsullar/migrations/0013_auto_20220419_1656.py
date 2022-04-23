# Generated by Django 3.2.12 on 2022-04-19 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mehsullar', '0012_servisodeme_ilkin_odenis'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servisodeme',
            name='ilkin_odenis',
        ),
        migrations.AddField(
            model_name='servis',
            name='ilkin_odenis',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='servis',
            name='kredit',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]