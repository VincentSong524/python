def make_album(singer, album, songs = None):
    song_album = {}
    song_album['singer'] = singer
    song_album['album'] = album
    if songs:
        song_album['songs'] = songs
    return song_album

coldplay = make_album('coldplay', 'yellow', 18)
print(coldplay)