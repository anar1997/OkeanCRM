# Generated by Django 3.2.12 on 2022-04-19 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mehsullar', '0007_auto_20220419_1344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servis',
            name='servis_qiymeti',
        ),
    ]
