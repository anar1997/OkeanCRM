# Generated by Django 3.2.12 on 2022-04-08 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_user_maas'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='maas_uslubu',
            field=models.CharField(choices=[('PRİM', 'PRİM'), ('FİX', 'FİX'), ('FİX+PRİM', 'FİX+PRİM')], default='FİX', max_length=50),
        ),
    ]