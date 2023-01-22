class Song:
    def __init__(self, name):
        self.name = name

    def find_song_by_name(self, name):
        if self.name == name:
            return name


