# Generated by Django 3.2.9 on 2022-03-10 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mehsullar', '0026_muqavile_mehsul_sayi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='muqavile',
            name='mehsul_sayi',
            field=models.PositiveIntegerField(blank=True, default=1, null=True),
        ),
    ]
