# Generated by Django 3.2.6 on 2022-01-27 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20220127_1226'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='age',
            field=models.CharField(default='Возраст', max_length=3, verbose_name='Возраст'),
        ),
    ]
