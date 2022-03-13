# Generated by Django 3.2.9 on 2022-03-13 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20220313_2306'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bolge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bolge_adi', models.CharField(max_length=300)),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
        migrations.AddField(
            model_name='musteri',
            name='bolge',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.bolge'),
        ),
    ]
