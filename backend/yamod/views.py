from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from yamod.models import Song, Album, Artist, Concert

from yamod.serializers import AlbumOptionSerializer, ArtistOptionSerializer, SongFormSerializer, SongListSerializer, \
    ConcertFormSerializer, ConcertListSerializer


@swagger_auto_schema(method='GET', responses={200: AlbumOptionSerializer(many=True)})
@api_view(['GET'])
def album_option_list(request):
    albums = Album.objects.all()
    serializer = AlbumOptionSerializer(albums, many=True)
    return Response(serializer.data)


@swagger_auto_schema(method='GET', responses={200: ArtistOptionSerializer(many=True)})
@api_view(['GET'])
def artist_option_list(request):
    artists = Artist.objects.all()
    serializer = ArtistOptionSerializer(artists, many=True)
    return Response(serializer.data)


@swagger_auto_schema(method='GET', responses={200: SongListSerializer(many=True)})
@api_view(['GET'])
def songs_list(request):
    songs = Song.objects.all()
    serializer = SongListSerializer(songs, many=True)
    return Response(serializer.data)


@swagger_auto_schema(method='POST', request_body=SongFormSerializer, responses={200: SongFormSerializer()})
@api_view(['POST'])
def song_form_create(request):
    data = JSONParser().parse(request)
    serializer = SongFormSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@swagger_auto_schema(method='PUT', request_body=SongFormSerializer, responses={200: SongFormSerializer()})
@api_view(['PUT'])
def song_form_update(request, pk):
    try:
        song = Song.objects.get(pk=pk)
    except Song.DoesNotExist:
        return Response({'error': 'Song does not exist.'}, status=404)

    data = JSONParser().parse(request)
    serializer = SongFormSerializer(song, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@swagger_auto_schema(method='GET', responses={200: SongFormSerializer()})
@api_view(['GET'])
def song_form_get(request, pk):
    try:
        song = Song.objects.get(pk=pk)
    except Song.DoesNotExist:
        return Response({'error': 'Song does not exist.'}, status=404)

    serializer = SongFormSerializer(song)
    return Response(serializer.data)


@api_view(['DELETE'])
def song_delete(request, pk):
    try:
        song = Song.objects.get(pk=pk)
    except Song.DoesNotExist:
        return Response({'error': 'Song does not exist.'}, status=404)
    song.delete()
    return Response(status=204)

#
@swagger_auto_schema(method='GET', responses={200: ConcertListSerializer(many=True)})
@api_view(['GET'])
def concerts_list(request):
    concerts = Concert.objects.all()
    serializer = ConcertListSerializer(concerts, many=True)
    return Response(serializer.data)


@swagger_auto_schema(method='POST', request_body=ConcertFormSerializer, responses={200: ConcertFormSerializer()})
@api_view(['POST'])
def concert_form_create(request):
    data = JSONParser().parse(request)
    serializer = ConcertFormSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@swagger_auto_schema(method='PUT', request_body=ConcertFormSerializer, responses={200: ConcertFormSerializer()})
@api_view(['PUT'])
def concert_form_update(request, pk):
    try:
        concert = Concert.objects.get(pk=pk)
    except Concert.DoesNotExist:
        return Response({'error': 'Concert does not exist.'}, status=404)

    data = JSONParser().parse(request)
    serializer = ConcertFormSerializer(concert, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@swagger_auto_schema(method='GET', responses={200: ConcertFormSerializer()})
@api_view(['GET'])
def concert_form_get(request, pk):
    try:
        concert = Concert.objects.get(pk=pk)
    except Concert.DoesNotExist:
        return Response({'error': 'Concert does not exist.'}, status=404)

    serializer = ConcertFormSerializer(concert)
    return Response(serializer.data)


@api_view(['DELETE'])
def concert_delete(request, pk):
    try:
        concert = Concert.objects.get(pk=pk)
    except Concert.DoesNotExist:
        return Response({'error': 'Concert does not exist.'}, status=404)
    concert.delete()
    return Response(status=204)

