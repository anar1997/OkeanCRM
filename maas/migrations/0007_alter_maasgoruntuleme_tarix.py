# Generated by Django 3.2.12 on 2022-04-15 12:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('maas', '0006_alter_maasgoruntuleme_tarix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maasgoruntuleme',
            name='tarix',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
