import unittest
from classes.guest import Guest
from classes.song import Song
from classes.room import Room

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room([])
        self.room_2 = Room([])
        self.room_3 = Room([])
        self.song = Song("Dancing Queen, Abba")
        self.song_2 = Song("Back to Black, Amy Winehouse")
        self.song_3 = Song("...Baby One More Time, Britney Spears")
        self.guest = Guest("Rupert")
        self.guest_2 = Guest("Winnie")
        self.guest_3 = Guest("Earl")

    def test_add_song_to_room(self):
        self.room.add_song_to_room(self.song_2.name, self.room.rooms)
        self.assertEqual(["Back to Black, Amy Winehouse"], self.room.rooms)

    def test_add_guest_to_room(self):
        self.room.add_guest_to_room(self.guest.name, self.room.rooms)
        self.assertEqual(["Rupert"], self.room.rooms)
