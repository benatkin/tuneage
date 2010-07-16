from django.contrib import admin
from tunes.models import Song

class SongAdmin(admin.ModelAdmin):
    list_display = ['name', 'time', 'artist', 'album', 'track', 'total_tracks']

admin.site.register(Song, SongAdmin)
