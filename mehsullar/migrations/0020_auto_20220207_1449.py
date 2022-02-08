# Generated by Django 3.2.9 on 2022-02-07 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mehsullar', '0019_auto_20220207_1133'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock',
            old_name='warehouse',
            new_name='anbar',
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='quantity',
            new_name='say',
        ),
        migrations.AddField(
            model_name='stock',
            name='mehsul',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mehsullar.mehsullar'),
        ),
        migrations.AlterUniqueTogether(
            name='stock',
            unique_together=set(),
        ),
    ]