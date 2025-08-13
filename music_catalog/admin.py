from django.contrib import admin
from .models import Artist, Album, Song


class AlbumInline(admin.TabularInline):
    """Инлайн для альбомов исполнителя"""
    model = Album
    extra = 0
    fields = ('title', 'release_year')
    show_change_link = True


class SongInline(admin.TabularInline):
    """Инлайн для песен альбома"""
    model = Song
    extra = 0
    fields = ('track_number', 'title')
    ordering = ('track_number',)


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    """Админка для исполнителей"""
    list_display = ('name', 'albums_count', 'songs_count')
    search_fields = ('name',)
    ordering = ('name',)
    inlines = [AlbumInline]

    def albums_count(self, obj):
        """Количество альбомов"""
        return obj.albums.count()
    albums_count.short_description = 'Количество альбомов'

    def songs_count(self, obj):
        """Общее количество песен"""
        return Song.objects.filter(album__artist=obj).count()
    songs_count.short_description = 'Всего песен'


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    """Админка для альбомов"""
    list_display = ('title', 'artist', 'release_year', 'songs_count')
    list_filter = ('release_year', 'artist')
    search_fields = ('title', 'artist__name')
    ordering = ('-release_year', 'title')
    autocomplete_fields = ('artist',)
    inlines = [SongInline]

    fieldsets = (
        ('Основная информация', {
            'fields': ('artist', 'title', 'release_year')
        }),
    )

    def songs_count(self, obj):
        """Количество песен в альбоме"""
        return obj.songs.count()
    songs_count.short_description = 'Количество песен'


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    """Админка для песен"""
    list_display = ('title', 'artist_name', 'album', 'track_number')
    list_filter = ('album__artist', 'album__release_year')
    search_fields = ('title', 'album__title', 'album__artist__name')
    ordering = ('album__artist__name', 'album__title', 'track_number')
    autocomplete_fields = ('album',)

    fieldsets = (
        ('Основная информация', {
            'fields': ('album', 'title', 'track_number')
        }),
    )

    def artist_name(self, obj):
        """Название исполнителя"""
        return obj.album.artist.name
    artist_name.short_description = 'Исполнитель'
    artist_name.admin_order_field = 'album__artist__name'


# Настройка заголовков админки
admin.site.site_header = 'Музыкальная База Данных'
admin.site.site_title = 'Музыкальная БД'
admin.site.index_title = 'Управление музыкальной коллекцией'
