# Generated by Django 3.2.12 on 2022-04-01 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maas', '0014_maasode'),
    ]

    operations = [
        migrations.CreateModel(
            name='KreditorPrim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prim_faizi', models.PositiveBigIntegerField(blank=True, default=0)),
            ],
        ),
    ]