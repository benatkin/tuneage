from django.db import models

class Song(models.Model):
    name = models.CharField(max_length=100)
    time = models.IntegerField() # in seconds
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    track = models.IntegerField(null=True)
    total_tracks = models.IntegerField(null=True)

    def deserialize_itunes_tsv(self, line):
        cols = [col.strip() for col in line.split("\t")]
        self.name = cols[0]
        minutes, seconds = [int(s) for s in cols[1].split(':')]
        self.time = minutes * 60 + seconds
        self.artist = cols[2]
        self.album = cols[3]
        track = cols[4]
        if ' of ' in track:
            self.track, self.total_tracks = [int(s) for s in track.split(' of ')]
        elif len(track) > 0:
            self.track = int(track)
