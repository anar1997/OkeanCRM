# Generated by Django 3.2.9 on 2022-03-15 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_holdingkassamexaric'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holdingdenshirketleretransfer',
            name='transfer_meblegi',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='holdingkassa',
            name='balans',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='holdingkassamedaxil',
            name='mebleg',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='holdingkassamexaric',
            name='mebleg',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='ofisdenshirketetransfer',
            name='transfer_meblegi',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='ofiskassa',
            name='balans',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='shirketdenholdingetransfer',
            name='transfer_meblegi',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='shirketdenofisleretransfer',
            name='transfer_meblegi',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='shirketkassa',
            name='balans',
            field=models.FloatField(default=0),
        ),
    ]
