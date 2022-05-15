# Generated by Django 3.2.12 on 2022-04-12 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maas', '0011_canvasserprim_satis0'),
    ]

    operations = [
        migrations.AlterField(
            model_name='canvasserprim',
            name='fix_maas',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='canvasserprim',
            name='komandaya_gore_prim',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='canvasserprim',
            name='ofise_gore_prim',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='canvasserprim',
            name='satis0',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='canvasserprim',
            name='satis15p',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='canvasserprim',
            name='satis1_8',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='canvasserprim',
            name='satis20p',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='canvasserprim',
            name='satis9_14',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='dealerprim',
            name='fix_maas',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='dealerprim',
            name='komandaya_gore_prim',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='officeleaderprim',
            name='fix_maas',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='officeleaderprim',
            name='ofise_gore_prim',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='vanleaderprim',
            name='fix_maas',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='vanleaderprim',
            name='komandaya_gore_prim',
            field=models.FloatField(blank=True, default=0),
        ),
    ]
