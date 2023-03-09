from django.contrib.auth.models import User
from django.db import models


class Photo(models.Model):
    photo = models.ImageField(null=False, blank=False, upload_to='photo', verbose_name='Картинка')
    text = models.TextField(max_length=500, null=False, blank=False, verbose_name='Подпись')
    author = models.ForeignKey(
        to=User,
        verbose_name='Автор',
        related_name='photo',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(verbose_name='Дата создания',
                                      auto_now_add=True)


class Favorite(models.Model):
    user = models.ForeignKey(
        to=User,
        related_name='favorite_photo',
        verbose_name='Пользователь',
        null=False,
        on_delete=models.CASCADE
    )
    photo = models.ForeignKey(
        to=Photo,
        related_name='favorite_users',
        verbose_name='Фото',
        null=False,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(verbose_name='Дата создания',
                                      auto_now_add=True)

    class Meta:
        verbose_name = 'Избранная фото'
        verbose_name_plural = 'Избранные фото'



