from django.db import models


class Artist(models.Model):

    name = models.TextField()
    dead = models.BooleanField()
    year_of_birth = models.IntegerField()

    def __str__(self):
        return self.name


class Album(models.Model):

    name = models.TextField()
    release_date = models.DateField()
    number_of_songs = models.IntegerField()
    indiziert = models.BooleanField()

    def __str__(self):
        return self.title


class Song(models.Model):

    CHOICES = (
        ('u', 'Unknown'),
        ('p', 'Pop'),
        ('j', 'Jazz'),
        ('r', 'Rock'),
        ('h', 'Hip-Hop'),
        ('v', 'Volksmusic')
    )

    title = models.TextField()
    artist = models.ManyToManyField('Artist')
    genre = models.CharField(max_length=1, choices=CHOICES, null=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True)
    length = models.PositiveIntegerField(help_text='in Minutes')

    def __str__(self):
        return self.title


class Concert(models.Model):

    name = models.TextField()
    begin_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    artist = models.ManyToManyField('Artist')
    over_18 = models.BooleanField(null=True)

    def __str__(self):
        return self.name
