def make_album(singer, album):
    album_about = {'singer': singer, 'album': album}
    return  album_about

while True:
    print("\nPlease tell me a singer's name and one of his/her album:")
    print("(enter 'q' at any time to quit)")

    singer_name = input("Singer name: ")
    if singer_name == 'q':
        break

    album = input("Album: ")
    if album == 'q':
        break

    album_ms = make_album(singer_name, album)
    print (album_ms)