# Generated by Django 3.2.12 on 2022-04-19 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mehsullar', '0008_remove_servis_servis_qiymeti'),
    ]

    operations = [
        migrations.AddField(
            model_name='servis',
            name='servis_qiymeti',
            field=models.FloatField(blank=True, default=0),
        ),
    ]
