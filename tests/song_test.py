import unittest
from classes.guest import Guest
from classes.song import Song
from classes.room import Room

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Dancing Queen, Abba")
        self.song_2 = Song("Back to Black, Amy Winehouse")
        self.song_3 = Song("...Baby One More Time, Britney Spears")

    def test_song_has_name(self):
        self.assertEqual("Back to Black, Amy Winehouse", self.song_2.name)

    def test_find_song_by_name(self):
        self.song.find_song_by_name(self.song_2.name)
        self.assertEqual("Back to Black, Amy Winehouse", self.song_2.name)
    

