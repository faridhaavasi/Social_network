# Generated by Django 4.2.3 on 2023-07-14 15:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_name', models.CharField(max_length=50, unique=True, verbose_name='id')),
                ('avatar', models.ImageField(upload_to='media/profile/avatar')),
                ('bio', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='User', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'profile',
                'verbose_name_plural': 'profiles',
                'ordering': ('user',),
            },
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_uuid', models.UUIDField(null=True, verbose_name='device UUID')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login datetime')),
                ('device_type', models.CharField(choices=[(1, 'web'), (2, 'android'), (3, 'ios'), (4, 'pc')], default=1, max_length=50)),
                ('device_os', models.CharField(blank=True, max_length=20, verbose_name='os device')),
                ('app_version', models.CharField(blank=True, max_length=10, verbose_name='version_app')),
                ('device_model', models.CharField(blank=True, max_length=10, verbose_name='device model')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'device',
                'verbose_name_plural': 'devices',
                'ordering': ('user', 'last_login'),
            },
        ),
    ]
