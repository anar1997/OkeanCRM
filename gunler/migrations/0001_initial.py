# Generated by Django 3.2.12 on 2022-04-06 09:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0002_holdingdenshirketleretransfer_holdingkassamedaxil_holdingkassamexaric_ofisdenshirketetransfer_ofiska'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HoldingGunler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_gunleri_count', models.PositiveBigIntegerField(default=0)),
                ('qeyri_is_gunu_count', models.PositiveBigIntegerField(default=0)),
                ('tetil_gunleri', models.CharField(blank=True, max_length=500, null=True)),
                ('tarix', models.DateField(editable=False)),
                ('holding', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='is_gunleri', to='company.holding')),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='KomandaGunler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_gunleri_count', models.PositiveBigIntegerField(default=0)),
                ('qeyri_is_gunu_count', models.PositiveBigIntegerField(default=0)),
                ('tetil_gunleri', models.CharField(blank=True, max_length=500, null=True)),
                ('tarix', models.DateField(editable=False)),
                ('komanda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='is_gunleri', to='company.komanda')),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='OfisGunler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_gunleri_count', models.PositiveBigIntegerField(default=0)),
                ('qeyri_is_gunu_count', models.PositiveBigIntegerField(default=0)),
                ('tetil_gunleri', models.CharField(blank=True, max_length=500, null=True)),
                ('tarix', models.DateField(editable=False)),
                ('ofis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='is_gunleri', to='company.ofis')),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='ShirketGunler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_gunleri_count', models.PositiveBigIntegerField(default=0)),
                ('qeyri_is_gunu_count', models.PositiveBigIntegerField(default=0)),
                ('tetil_gunleri', models.CharField(blank=True, max_length=500, null=True)),
                ('tarix', models.DateField(editable=False)),
                ('shirket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='is_gunleri', to='company.shirket')),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='ShobeGunler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_gunleri_count', models.PositiveBigIntegerField(default=0)),
                ('qeyri_is_gunu_count', models.PositiveBigIntegerField(default=0)),
                ('tetil_gunleri', models.CharField(blank=True, max_length=500, null=True)),
                ('tarix', models.DateField(editable=False)),
                ('shobe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='is_gunleri', to='company.shobe')),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='VezifeGunler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_gunleri_count', models.PositiveBigIntegerField(default=0)),
                ('qeyri_is_gunu_count', models.PositiveBigIntegerField(default=0)),
                ('tetil_gunleri', models.CharField(blank=True, max_length=500, null=True)),
                ('tarix', models.DateField(editable=False)),
                ('vezife', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='is_gunleri', to='company.vezifeler')),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='VezifeIstisnaIsci',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tetil_gunleri', models.CharField(blank=True, max_length=500, null=True)),
                ('istisna_isciler', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
                ('vezife_gunler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='istisna_isci', to='gunler.vezifegunler')),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='ShobeIstisnaIsci',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tetil_gunleri', models.CharField(blank=True, max_length=500, null=True)),
                ('istisna_isciler', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
                ('shobe_gunler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='istisna_isci', to='gunler.shobegunler')),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='ShirketIstisnaIsci',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tetil_gunleri', models.CharField(blank=True, max_length=500, null=True)),
                ('istisna_isciler', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
                ('shirket_gunler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='istisna_isci', to='gunler.shirketgunler')),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='OfisIstisnaIsci',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tetil_gunleri', models.CharField(blank=True, max_length=500, null=True)),
                ('istisna_isciler', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
                ('ofis_gunler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='istisna_isci', to='gunler.ofisgunler')),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='KomandaIstisnaIsci',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tetil_gunleri', models.CharField(blank=True, max_length=500, null=True)),
                ('istisna_isciler', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
                ('komanda_gunler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='istisna_isci', to='gunler.komandagunler')),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='IsciGunler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_gunleri_count', models.PositiveBigIntegerField(default=0)),
                ('qeyri_is_gunu_count', models.PositiveBigIntegerField(default=0)),
                ('tetil_gunleri', models.CharField(blank=True, max_length=500, null=True)),
                ('icaze_gunleri_odenisli', models.CharField(blank=True, max_length=500, null=True)),
                ('icaze_gunleri_odenissiz', models.CharField(blank=True, max_length=500, null=True)),
                ('tarix', models.DateField(editable=False)),
                ('isci', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='is_gunleri', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='HoldingIstisnaIsci',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tetil_gunleri', models.CharField(blank=True, max_length=500, null=True)),
                ('holding_gunler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='istisna_isci', to='gunler.holdinggunler')),
                ('istisna_isciler', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
    ]
