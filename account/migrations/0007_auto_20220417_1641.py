# Generated by Django 3.2.12 on 2022-04-17 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_musteri_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='elektron_imza',
            field=models.ImageField(blank=True, null=True, upload_to='media/account'),
        ),
        migrations.AddField(
            model_name='user',
            name='qeyd',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='sv_image',
            field=models.ImageField(blank=True, null=True, upload_to='media/account/%Y/%m/%d/'),
        ),
    ]
