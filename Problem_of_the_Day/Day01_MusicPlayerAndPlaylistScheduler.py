class Track:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist

        m, s = map(int, duration.split(":"))
        self.seconds = m * 60 + s
    def formatted_duration(self):
        return f"{self.seconds // 60}:{self.seconds % 60:02d}"

    def __str__(self):
        return f"{self.title} by {self.artist} [{self.formatted_duration()}]"

class Playlist:
    def __init__(self, name):
        self.name = name
        self.tracks = []

    def add(self, track):
        self.tracks.append(track)

    def remove(self, track):
        self.tracks.remove(track)

    def _format_time(self, seconds):
        return f"{seconds // 60}:{seconds % 60:02d}"

    def total_duration(self):
        total = sum(t.seconds for t in self.tracks)
        return self._format_time(total)

    def longest_track(self):
        return max(self.tracks, key=lambda t: t.seconds)

    def shortest_track(self):
        return min(self.tracks, key=lambda t: t.seconds)

    def average_duration(self):
        total = sum(t.seconds for t in self.tracks)
        avg = total // len(self.tracks)
        return self._format_time(avg)

    def tracks_under(self, seconds):
        return [t.title for t in self.tracks if t.seconds < seconds]

    def summary(self):
        print(f"{self.name} | {len(self.tracks)} tracks | Total: {self.total_duration()} | Avg: {self.average_duration()}")


def main():
    tracks = [
  Track("Blinding Lights", "The Weeknd",     "3:20"),
  Track("Levitating",      "Dua Lipa",       "3:23"),
  Track("Stay",            "Kid LAROI",      "2:21"),
  Track("Peaches",         "Justin Bieber",  "3:18"),
  Track("Good 4 U",        "Olivia Rodrigo", "2:58"),
    ]

    playlist = Playlist("Evening Vibes")

    for t in tracks:
        playlist.add(t)
    
    print(tracks[0])
    print(tracks[0].seconds)

    print(playlist.total_duration())
    print(playlist.longest_track())
    print(playlist.shortest_track())
    print(playlist.average_duration())
    print(playlist.tracks_under(200))
    playlist.summary()

if __name__=='__main__':
    main()