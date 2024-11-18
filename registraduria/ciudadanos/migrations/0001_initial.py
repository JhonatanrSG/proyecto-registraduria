# Generated by Django 3.1.12 on 2024-11-17 20:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudadano',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos/')),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('identificacion', models.CharField(max_length=20)),
                ('fecha_nacimiento', models.DateField()),
                ('lugar_nacimiento', models.CharField(max_length=100)),
                ('fecha_expedicion', models.DateField()),
                ('lugar_expedicion', models.CharField(max_length=100)),
                ('rh', models.CharField(max_length=3)),
                ('grupo_sanguineo', models.CharField(max_length=3)),
                ('estatura', models.FloatField(blank=True, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
