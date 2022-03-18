# Generated by Django 3.2.9 on 2022-03-14 07:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20220313_2316'),
    ]

    operations = [
        migrations.CreateModel(
            name='IsciSatisSayi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarix', models.DateField()),
                ('satis_sayi', models.PositiveIntegerField(default=0, null=True)),
                ('isci', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='isci_satis_sayi', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]