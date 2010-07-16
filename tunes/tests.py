"""
Tests for tunes app.
"""

from django.test import TestCase
from tunes.models import Song

class SongDeserializeTest(TestCase):
    def _test_deserialize(self, line, fields):
        """
        Runs a serialization test.
        """
        song = Song()
        song.deserialize_itunes_tsv(line)
        song_fields = dict([(field.name, getattr(song, field.name)) for field in song._meta.fields if field.name != 'id'])
        self.assertEquals(song_fields, fields)

    def test_with_total_tracks(self):
        """
        Tests that a row copied from iTunes with a track and the total number of tracks deserializes.
        """
        line = 'On the Beatiful Blue Danube, Walz, Op. 314\t10:05\tJohann Strauss II\tClassical Masterpiece of Music\t1 of 9\tClassical\t\t11\n'
        fields = {'album': u'Classical Masterpiece of Music', 'name': u'On the Beatiful Blue Danube, Walz, Op. 314', 'artist': u'Johann Strauss II', 'track': 1, 'total_tracks': 9, 'time': 605}
        self._test_deserialize(line, fields)

    def test_with_track(self):
        """
        Tests that a row copied from iTunes with a track deserializes.
        """
        line = '08 08 08 08 08 - Act I, Tableau 1, The Nutcracker battles against the Army of the Mouse King, etc.\t3:20\tKirov Orchestra, Valery Gergiev\tTchaikovsky: The Nutcracker, Op. 71 (Complete Ballet)\t8\tClassical\t\t3\n'
        fields = {'album': 'Tchaikovsky: The Nutcracker, Op. 71 (Complete Ballet)', 'name': '08 08 08 08 08 - Act I, Tableau 1, The Nutcracker battles against the Army of the Mouse King, etc.', 'artist': 'Kirov Orchestra, Valery Gergiev', 'track': 8, 'total_tracks': None, 'time': 200}
        self._test_deserialize(line, fields)

    def test_without_track(self):
        """
        Tests that a row copied from iTunes with a track deserializes.
        """
        line = '01 Maple Leaf Rag (1899)\t3:19\tScott Joplin\t\t\tClassical\t\t6\n'
        fields = {'album': '', 'name': '01 Maple Leaf Rag (1899)', 'artist': 'Scott Joplin', 'track': None, 'total_tracks': None, 'time': 199}
        self._test_deserialize(line, fields)

