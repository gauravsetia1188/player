from django.contrib import admin
from .models import Album,Song
# Register your models here.

class Albumcustomisation(admin.ModelAdmin):
    list_display = ['artist','album_title']
    list_filter = ['artist']
    class Meta:
        model = Album

class Songcustomisation(admin.ModelAdmin):

    search_fields = ['song_title']
    list_display = ['song_title','album']

    class Meta:
        model = Song

admin.site.register(Album,Albumcustomisation)
admin.site.register(Song,Songcustomisation)