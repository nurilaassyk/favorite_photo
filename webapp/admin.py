from django.contrib import admin
from webapp.models import Photo, Favorite


class PhotoAdmin(admin.ModelAdmin):
    list_display = ['photo', 'text', 'author']
    fields = ['photo', 'text', 'author']


class FavoriteAdmin(admin.ModelAdmin):
    list_display = ['user', 'photo']
    fields = ['user', 'photo']


admin.site.register(Photo, PhotoAdmin)
admin.site.register(Favorite, FavoriteAdmin)
