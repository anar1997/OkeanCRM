# Generated by Django 3.2.9 on 2021-12-29 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_user_ishe_baslama_tarixi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='ofis',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ishci', to='account.merkezler'),
        ),
        migrations.AlterField(
            model_name='user',
            name='shirket',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ishci', to='account.shirket'),
        ),
    ]