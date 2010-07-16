from django.contrib import admin
from tunes.models import Song

class SongAdmin(admin.ModelAdmin):
    list_display = ['name', 'time', 'artist', 'album', 'track', 'total_tracks']
    special_ordering = {'artist': ('artist', 'album', 'track'), 'album': ('album', 'track')}

    def apply_special_ordering(self, request, queryset):
        order_type, order_by = [request.POST.get(param, None) for param in ('ot', 'o')]
        if self.special_ordering and order_type and order_by:
            try:
                order_field = list_display[int(order_by) - 1]
                ordering = self.special_ordering[order_field]
                if order_type == 'desc':
                    ordering = ['-' + field for field in ordering]
                queryset = queryset.orderby()
            except IndexError, KeyError:
                return queryset
        return queryset

    def queryset(self, request):
        queryset = super(SongAdmin, self).queryset(request)
        queryset = self.apply_special_ordering(request, queryset)
        return queryset

admin.site.register(Song, SongAdmin)
