# Generated by Django 3.2.9 on 2022-03-13 04:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mehsullar', '0001_initial'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bonus',
            name='stok',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stok_bonus', to='mehsullar.stok'),
        ),
    ]
