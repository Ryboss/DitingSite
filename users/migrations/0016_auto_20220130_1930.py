# Generated by Django 3.2.6 on 2022-01-30 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20220128_1818'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='profile_likes',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='like',
            name='who_likes',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
