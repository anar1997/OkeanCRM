# Generated by Django 3.2.12 on 2022-04-06 09:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('company', '0001_initial'),
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
                ('mexaric_eden', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_shirket_mexaric', to=settings.AUTH_USER_MODEL)),
                ('shirket_kassa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shirket_kassa_mexaric', to='company.shirketkassa')),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='ShirketKassaMedaxil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mebleg', models.FloatField(default=0)),
                ('qeyd', models.TextField(blank=True, null=True)),
                ('medaxil_tarixi', models.DateField(default=None)),
                ('medaxil_eden', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_shirket_medaxil', to=settings.AUTH_USER_MODEL)),
                ('shirket_kassa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shirket_kassa_medaxil', to='company.shirketkassa')),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='ShirketdenOfislereTransfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transfer_meblegi', models.FloatField(default=0)),
                ('transfer_tarixi', models.DateField(auto_now=True)),
                ('transfer_qeydi', models.TextField(blank=True, null=True)),
                ('ofis_kassa', models.ManyToManyField(related_name='shirketden_ofise_transfer', to='company.OfisKassa')),
                ('shirket_kassa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shirketden_ofise_transfer', to='company.shirketkassa')),
                ('transfer_eden', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_shirket_ofis_transfer', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='ShirketdenHoldingeTransfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transfer_meblegi', models.FloatField(default=0)),
                ('transfer_tarixi', models.DateField(auto_now=True)),
                ('transfer_qeydi', models.TextField(blank=True, null=True)),
                ('holding_kassa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shirketden_holdinge_transfer', to='company.holdingkassa')),
                ('shirket_kassa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shirketden_holdinge_transfer', to='company.shirketkassa')),
                ('transfer_eden', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_shirket_holding_transfer', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='OfisKassaMexaric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mebleg', models.FloatField(default=0)),
                ('qebzin_resmi', models.FileField(blank=True, null=True, upload_to='media/%Y/%m/%d/')),
                ('qeyd', models.TextField(blank=True, null=True)),
                ('mexaric_tarixi', models.DateField(default=None)),
                ('mexaric_eden', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_ofis_mexaric', to=settings.AUTH_USER_MODEL)),
                ('ofis_kassa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ofis_kassa_mexaric', to='company.ofiskassa')),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='OfisKassaMedaxil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mebleg', models.FloatField(default=0)),
                ('qeyd', models.TextField(blank=True, null=True)),
                ('medaxil_tarixi', models.DateField(default=None)),
                ('medaxil_eden', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_ofis_medaxil', to=settings.AUTH_USER_MODEL)),
                ('ofis_kassa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ofis_kassa_medaxil', to='company.ofiskassa')),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='OfisdenShirketeTransfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transfer_meblegi', models.FloatField(default=0)),
                ('transfer_tarixi', models.DateField(auto_now=True)),
                ('transfer_qeydi', models.TextField(blank=True, null=True)),
                ('ofis_kassa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ofisden_shirkete_transfer', to='company.ofiskassa')),
                ('shirket_kassa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ofisden_shirkete_transfer', to='company.shirketkassa')),
                ('transfer_eden', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_ofis_shirket_transfer', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='HoldingKassaMexaric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mebleg', models.FloatField(default=0)),
                ('qebzin_resmi', models.FileField(blank=True, null=True, upload_to='media/%Y/%m/%d/')),
                ('qeyd', models.TextField(blank=True, null=True)),
                ('mexaric_tarixi', models.DateField(default=None)),
                ('holding_kassa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='holding_kassa_mexaric', to='company.holdingkassa')),
                ('mexaric_eden', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_holding_mexaric', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='HoldingKassaMedaxil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mebleg', models.FloatField(default=0)),
                ('qeyd', models.TextField(blank=True, null=True)),
                ('medaxil_tarixi', models.DateField(default=None)),
                ('holding_kassa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='holding_kassa_medaxil', to='company.holdingkassa')),
                ('medaxil_eden', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_holding_medaxil', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='HoldingdenShirketlereTransfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transfer_meblegi', models.FloatField(default=0)),
                ('transfer_tarixi', models.DateField(auto_now=True)),
                ('transfer_qeydi', models.TextField(blank=True, null=True)),
                ('holding_kassa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='holdingden_shirkete_transfer', to='company.holdingkassa')),
                ('shirket_kassa', models.ManyToManyField(related_name='holdingden_shirkete_transfer', to='company.ShirketKassa')),
                ('transfer_eden', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_holding_shirket_transfer', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
    ]
