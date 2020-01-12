from rest_framework import serializers
from .models import Song, Album, Artist, Concert


class ArtistOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name']


class AlbumOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'name']


class SongListSerializer(serializers.ModelSerializer):
    album_name = serializers.SerializerMethodField()
    artist_name = serializers.SerializerMethodField()

    class Meta:
        model = Song
        fields = ['id', 'title', 'artist_name', 'album_name', 'genre']

    def get_album_name(self, obj):
        return obj.album.name if obj.album else ''

    def get_artist_name(self, obj):
        all_artists = "";
        num = 0;
        if obj.artist.all():
            for x in obj.artist.all():
                all_artists = all_artists + obj.artist.all()[num].name + ", "
                num = num+1
            return all_artists
        else: ''


class SongFormSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = '__all__'


class ConcertListSerializer(serializers.ModelSerializer):
    artist_name = serializers.SerializerMethodField()

    class Meta:
        model = Concert
        fields = ['id', 'name', 'begin_date', 'end_date', 'artist_name']

    def get_artist_name(self, obj):
        all_artists = "";
        num = 0;
        if obj.artist.all():
            for x in obj.artist.all():
                all_artists = all_artists + obj.artist.all()[num].name + ", "
                num = num+1
            return all_artists
        else: ''


class ConcertFormSerializer(serializers.ModelSerializer):

    class Meta:
        model = Concert
        fields = '__all__'
