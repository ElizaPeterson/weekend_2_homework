class Room:
    def __init__(self, rooms):
        self.rooms = rooms
                
    def add_song_to_room(self, song, room):
        if self.rooms == room:
            self.rooms.append(song)

    def add_guest_to_room(self, guest, room):
        if self.rooms == room:
                self.rooms.append(guest)
                