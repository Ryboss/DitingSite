# Generated by Django 3.2.6 on 2022-01-28 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_profile_watermark_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Watermark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('watermark_image', models.ImageField(default='default.jpg', upload_to='watermark_images')),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='watermark_image',
        ),
    ]