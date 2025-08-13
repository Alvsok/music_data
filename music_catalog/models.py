from django.db import models
from django.core.validators import MinValueValidator


class Artist(models.Model):
    """Модель исполнителя"""
    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name="Название исполнителя",
        help_text="Уникальное название исполнителя"
    )


    class Meta:
        verbose_name = "Исполнитель"
        verbose_name_plural = "Исполнители"



    def __str__(self):
        return self.name


class Album(models.Model):
    """Модель альбома"""
    artist = models.ForeignKey(
        Artist,
        on_delete=models.CASCADE,
        related_name='albums',
        verbose_name="Исполнитель"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название альбома"
    )
    release_year = models.PositiveIntegerField(
        validators=[MinValueValidator(1900)],
        verbose_name="Год выпуска",
        help_text="Год выпуска альбома"
    )


    class Meta:
        verbose_name = "Альбом"
        verbose_name_plural = "Альбомы"
        unique_together = ('title', 'release_year')
	
        

    def __str__(self):
        return f"{self.artist.name} - {self.title} ({self.release_year})"


class Song(models.Model):
    """Модель песни"""
    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        related_name='songs',
        verbose_name="Альбом"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название песни"
    )
    track_number = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        verbose_name="Порядковый номер в альбоме",
        help_text="Номер трека в альбоме"
    )


    class Meta:
        verbose_name = "Песня"
        verbose_name_plural = "Песни"


  

    def __str__(self):
        return f"{self.album.artist.name} - {self.title}"

