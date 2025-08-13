from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Artist, Album, Song
from .serializers import ArtistSerializer, AlbumSerializer, SongSerializer


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [AllowAny]


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [AllowAny]


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [AllowAny]
