# Generated by Django 3.2.9 on 2022-01-24 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mehsullar', '0012_muqavile_dusen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='muqavile',
            name='elektron_imza',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]