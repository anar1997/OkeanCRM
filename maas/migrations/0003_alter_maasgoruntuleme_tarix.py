# Generated by Django 3.2.12 on 2022-04-07 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maas', '0002_bonus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maasgoruntuleme',
            name='tarix',
            field=models.DateField(null=True),
        ),
    ]
