# Generated by Django 3.2.9 on 2022-03-13 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20220313_2316'),
        ('mehsullar', '0003_rename_muqvilehediyye_muqavilehediyye'),
    ]

    operations = [
        migrations.AddField(
            model_name='mehsullar',
            name='shirket',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shirket_mehsul', to='account.shirket'),
        ),
    ]