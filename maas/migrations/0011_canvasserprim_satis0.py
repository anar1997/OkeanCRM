# Generated by Django 3.2.12 on 2022-04-11 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maas', '0010_auto_20220411_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='canvasserprim',
            name='satis0',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
