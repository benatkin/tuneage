from django.contrib import admin
from django.contrib.admin.views.main import ChangeList
from tunes.models import Song

class SpecialOrderingChangeList(ChangeList):
    def apply_special_ordering(self, queryset):
        order_type, order_by = [self.params.get(param, None) for param in ('ot', 'o')]
        special_ordering = self.model_admin.special_ordering
        if special_ordering and order_type and order_by:
            try:
                order_field = self.list_display[int(order_by)]
                ordering = special_ordering[order_field]
                if order_type == 'desc':
                    ordering = ['-' + field for field in ordering]
                queryset = queryset.order_by(*ordering)
            except IndexError:
                return queryset
            except KeyError:
                return queryset
        return queryset

    def get_query_set(self):
        queryset = super(SpecialOrderingChangeList, self).get_query_set()
        queryset = self.apply_special_ordering(queryset)
        return queryset

class SongAdmin(admin.ModelAdmin):
    list_display = ['name', 'time', 'artist', 'album', 'track', 'total_tracks']
    special_ordering = {'artist': ('artist', 'album', 'track'), 'album': ('album', 'track')}

    def get_changelist(self, request, **kwargs):
        return SpecialOrderingChangeList

admin.site.register(Song, SongAdmin)
