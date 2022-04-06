# Generated by Django 3.2.12 on 2022-04-06 08:14

from django.conf import settings
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('company', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('asa', models.CharField(max_length=200)),
                ('dogum_tarixi', models.DateField(blank=True, null=True)),
                ('ishe_baslama_tarixi', models.DateField(auto_now_add=True, null=True)),
                ('last_login', models.DateTimeField(auto_now=True, null=True)),
                ('tel1', models.CharField(max_length=200)),
                ('tel2', models.CharField(max_length=200)),
                ('sv_image', models.ImageField(blank=True, null=True, upload_to='media/%Y/%m/%d/')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
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
        migrations.CreateModel(
            name='IsciStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_adi', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Musteri',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asa', models.CharField(max_length=200)),
                ('sv_image', models.ImageField(blank=True, null=True, upload_to='media/%Y/%m/%d/')),
                ('tel1', models.CharField(max_length=50)),
                ('tel2', models.CharField(blank=True, max_length=50, null=True)),
                ('tel3', models.CharField(blank=True, max_length=50, null=True)),
                ('tel4', models.CharField(blank=True, max_length=50, null=True)),
                ('unvan', models.TextField()),
                ('bolge', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.bolge')),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='MusteriQeydler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qeyd', models.TextField()),
                ('musteri', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='musteri_qeydler', to='account.musteri')),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='IsciSatisSayi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarix', models.DateField()),
                ('satis_sayi', models.PositiveIntegerField(default=0, null=True)),
                ('isci', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='isci_satis_sayi', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
        migrations.AddField(
            model_name='user',
            name='isci_status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.iscistatus'),
        ),
        migrations.AddField(
            model_name='user',
            name='komanda',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_komanda', to='company.komanda'),
        ),
        migrations.AddField(
            model_name='user',
            name='ofis',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ishci', to='company.ofis'),
        ),
        migrations.AddField(
            model_name='user',
            name='shirket',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ishci', to='company.shirket'),
        ),
        migrations.AddField(
            model_name='user',
            name='shobe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ishci', to='company.shobe'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AddField(
            model_name='user',
            name='vezife',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_vezife', to='company.vezifeler'),
        ),
    ]
