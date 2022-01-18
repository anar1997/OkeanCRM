# Generated by Django 3.2.9 on 2022-01-18 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mehsullar', '0006_auto_20220117_1651'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='muqavile',
            name='hediyye',
        ),
        migrations.AddField(
            model_name='muqavile',
            name='hediyye1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='muqavile_hediyye1', to='mehsullar.hediyye'),
        ),
        migrations.AlterField(
            model_name='muqavile',
            name='hediyye2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='muqavile_hediyye2', to='mehsullar.hediyye'),
        ),
        migrations.AlterField(
            model_name='muqavile',
            name='hediyye3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='muqavile_hediyye3', to='mehsullar.hediyye'),
        ),
        migrations.DeleteModel(
            name='Hediyye2',
        ),
        migrations.DeleteModel(
            name='Hediyye3',
        ),
    ]
