# Generated by Django 5.0.6 on 2024-06-11 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.IntegerField(verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='firstname',
            field=models.CharField(default='', max_length=100, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='lastname',
            field=models.CharField(default='', max_length=100, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='latitude',
            field=models.FloatField(max_length=20, null=True, verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='longitude',
            field=models.FloatField(max_length=20, null=True, verbose_name='Долгота'),
        ),
        migrations.RenameField(
            model_name='Profile',
            old_name='firstname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='Profile',
            old_name='lastname',
            new_name='last_name',
        ),
    ]