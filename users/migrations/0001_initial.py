# Generated by Django 5.0.6 on 2024-06-11 07:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=6)),
                ('who_likes', models.CharField(max_length=50)),
                ('profile_likes', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(default='default.jpg', upload_to='profile_images', verbose_name='Фото')),
                ('bio', models.CharField(max_length=300, verbose_name='О себе')),
                ('country', models.CharField(default='Город', max_length=100, verbose_name='Город')),
                ('gender', models.CharField(choices=[('man', 'Мучжина'), ('woman', 'Жежина')], verbose_name='Пол')),
                ('lastname', models.CharField(blank=True, max_length=100, verbose_name='Lastname')),
                ('firstname', models.CharField(blank=True, max_length=100, verbose_name='Имя')),
                ('age', models.IntegerField(blank=True, verbose_name='Возраст')),
                ('longitude', models.FloatField(blank=True, max_length=20, verbose_name='Долгота')),
                ('latitude', models.FloatField(blank=True, max_length=20, verbose_name='Широта')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
