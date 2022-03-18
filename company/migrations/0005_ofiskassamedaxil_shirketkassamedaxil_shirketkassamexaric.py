# Generated by Django 3.2.9 on 2022-03-15 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_auto_20220315_1604'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShirketKassaMexaric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mebleg', models.FloatField(default=0)),
                ('qebzin_resmi', models.FileField(blank=True, null=True, upload_to='media/%Y/%m/%d/')),
                ('qeyd', models.TextField(blank=True, null=True)),
                ('mexaric_tarixi', models.DateField(default=None)),
                ('ofis_kassa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ofis_kassa_mexaric', to='company.ofiskassa')),
            ],
        ),
        migrations.CreateModel(
            name='ShirketKassaMedaxil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mebleg', models.FloatField(default=0)),
                ('qeyd', models.TextField(blank=True, null=True)),
                ('medaxil_tarixi', models.DateField(default=None)),
                ('shirket_kassa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shirket_kassa_medaxil', to='company.shirketkassa')),
            ],
        ),
        migrations.CreateModel(
            name='OfisKassaMedaxil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mebleg', models.FloatField(default=0)),
                ('qeyd', models.TextField(blank=True, null=True)),
                ('medaxil_tarixi', models.DateField(default=None)),
                ('ofis_kassa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ofis_kassa_medaxil', to='company.ofiskassa')),
            ],
        ),
    ]