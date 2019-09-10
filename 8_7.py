def make_album(singer, album, number=''):
    album_about = {'singer': singer, 'album': album}
    if number:
        album_about['number'] = number
    return  album_about

album_1 = make_album('singer_1', 'album_1')
print (album_1)

album_2 = make_album('singer_2', 'album_2', number=21)
print(album_2)

album_3 = make_album('singer_3', 'album_3', 11)
print(album_3)