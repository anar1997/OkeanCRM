# Generated by Django 3.2.12 on 2022-04-18 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_musteriqeydler_tarix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musteriqeydler',
            name='tarix',
            field=models.DateField(auto_now_add=True),
        ),
    ]
