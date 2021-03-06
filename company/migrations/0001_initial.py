# Generated by Django 3.2.12 on 2022-04-06 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Holding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('holding_adi', models.CharField(max_length=200, unique=True)),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='Komanda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('komanda_adi', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='Ofis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ofis_adi', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='Shirket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shirket_adi', models.CharField(max_length=200, unique=True)),
                ('holding', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='holding_shirket', to='company.holding')),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='Shobe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shobe_adi', models.CharField(max_length=200)),
                ('ofis', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shobe', to='company.ofis')),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='Vezifeler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vezife_adi', models.CharField(max_length=50)),
                ('shirket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shirket_vezifeleri', to='company.shirket')),
                ('shobe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shobe_vezife', to='company.shobe')),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='ShirketKassa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balans', models.FloatField(default=0)),
                ('shirket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shirket_kassa', to='company.shirket')),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='OfisKassa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balans', models.FloatField(default=0)),
                ('ofis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ofis_kassa', to='company.ofis')),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
        migrations.AddField(
            model_name='ofis',
            name='shirket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shirket_ofis', to='company.shirket'),
        ),
        migrations.CreateModel(
            name='HoldingKassa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balans', models.FloatField(default=0)),
                ('holding', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='holding_kassa', to='company.holding')),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
    ]
