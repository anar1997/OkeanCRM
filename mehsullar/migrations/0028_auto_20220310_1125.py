# Generated by Django 3.2.9 on 2022-03-10 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mehsullar', '0027_alter_muqavile_mehsul_sayi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='muqavile',
            name='mehsul_sayi',
            field=models.PositiveIntegerField(blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='muqavile',
            name='negd_odenis_1',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='muqavile',
            name='negd_odenis_2',
            field=models.FloatField(blank=True, default=0),
        ),
    ]
