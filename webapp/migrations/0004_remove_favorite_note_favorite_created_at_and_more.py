# Generated by Django 4.1.3 on 2022-11-21 14:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0003_rename_article_favorite_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorite',
            name='note',
        ),
        migrations.AddField(
            model_name='favorite',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата создания'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='favorite',
            name='photo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_users', to='webapp.photo', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_photo', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
