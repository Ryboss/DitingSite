from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Extending User Model Using a One-To-One Link
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField("Фото", default='default.jpg', upload_to='profile_images')
    bio = models.CharField('О себе', max_length=300)
    country = models.CharField('Город', max_length=100, default='Город')
    sex = (
        ('мужчина', 'm'),
        ('женщина', 'w')
    )
    gender = models.CharField('Пол', max_length=7, choices=sex, default='')
    lastname = models.CharField('Lastname', max_length=100, default='NoLastName')
    firstname = models.CharField('Имя', max_length=100, default='NoName')
    age = models.CharField('Возраст',max_length=3,default='Возраст')
    longitude = models.FloatField('Долгота', max_length=20, null=True)
    latitude=models.FloatField('Широта', max_length=20, null=True)


    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('profiles', kwargs={'profile_id': self.pk})

    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)




class Like(models.Model):
    user = models.CharField(max_length=6, null=True)
    who_likes = models.CharField(max_length=50, null=True)
    profile_likes = models.CharField(max_length=50, null=True)