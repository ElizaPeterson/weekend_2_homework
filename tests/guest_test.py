import unittest
from classes.guest import Guest
from classes.song import Song
from classes.room import Room

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Rupert")
        self.guest_2 = Guest("Winnie")
        self.guest_3 = Guest("Earl")

    def test_guest_has_name(self):
        self.assertEqual("Rupert", self.guest.name)

