# Generated by Django 3.2.12 on 2022-04-20 12:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mehsullar', '0015_alter_muqavile_muqavile_tarixi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='muqavile',
            name='ilkin_odenis',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='muqavile',
            name='ilkin_odenis_qaliq',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='muqavile',
            name='kredit_muddeti',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='muqavile',
            name='mehsul_sayi',
            field=models.PositiveIntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='muqavile',
            name='muqavile_tarixi',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='muqavile',
            name='muqavile_umumi_mebleg',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='muqavile',
            name='negd_odenis_1',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='muqavile',
            name='negd_odenis_2',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='muqavile',
            name='yeni_qrafik_mebleg',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
