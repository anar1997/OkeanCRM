# Generated by Django 3.2.9 on 2022-02-09 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mehsullar', '0005_alter_emeliyyat_emeliyyat_tarixi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emeliyyat',
            name='qeyd',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
