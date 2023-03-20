from spoopify_project.album import Album
from spoopify_project.song import Song


class Band:

    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        # if album.name not in [x.name for x in self.albums]:
        if album not in self.albums:
            self.albums.append(album)
            return f"Band {self.name} has added their newest album {album.name}."
        return f"Band {self.name} already has {album.name} in their library."

    def remove_album(self, album_name: str):
        if album_name not in [x.name for x in self.albums]:
            return f"Album {album_name} is not found."
        for album in self.albums:
            if album.published:
                return "Album has been published. It cannot be removed."
            elif album.name == album_name:
                self.albums.remove(album)
                return f"Album {album_name} has been removed."

    def details(self):
        result = f"Band {self.name}"
        for album in self.albums:
            result += f"\n{album.details()}"
        return result

song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())
band = Band("Manuel")
print(band.add_album(album))
print(band.remove_album("Initial D"))
print(band.details())