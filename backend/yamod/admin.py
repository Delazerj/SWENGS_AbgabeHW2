from django.contrib import admin
from .models import *


class SongAdmin(admin.ModelAdmin): pass


class AlbumAdmin(admin.ModelAdmin): pass


class ArtistAdmin(admin.ModelAdmin): pass


class ConcertAdmin (admin.ModelAdmin): pass


admin.site.register(Song, SongAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Concert, ConcertAdmin)


