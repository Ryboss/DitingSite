# Generated by Django 3.2.6 on 2022-01-28 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20220128_1258'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='watermark_image',
            field=models.ImageField(null=True, upload_to='profile_images'),
        ),
    ]
