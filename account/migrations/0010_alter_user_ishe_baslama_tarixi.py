# Generated by Django 3.2.12 on 2022-04-18 08:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_alter_user_vezife'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='ishe_baslama_tarixi',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
