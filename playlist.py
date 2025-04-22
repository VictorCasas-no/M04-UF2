#!/usr/bin/python3

from bs4 import BeautifulSoup

version = 0.5

app_title = "Playlist v" + str(version)

print(app_title)
print("-" * len(app_title))


ALBUMS_PATH = "albums/"
ARTISTS_PATH = "artists/"
GENRES_PATH = "genres/"
SONGS_PATH = "songs/"
COVERS_PATH = "songs/covers/

albums = []
artists = []
genres = []
songs = []
covers = []



def menu_opciones():
    while True:
        print("-----Menú-----")
        print("1. Albums")
        print("2. Artists")
        print("3. Songs")
        print("4. Genres")
        print("0. Exit")

        eleccion_menu = input("Elige una opción (entre o y 4)")

        if eleccion_menu < 0 or eleccion menu > 4:
            print("Please, introduce a number between 0 and 4")

        elif eleccion_menu == 0:
            break

        else:


def show_menu_albums():
    print("-----Albums Menu-----")
    print("1. List all albums")
    print("2. Search album by title")
    print("0. Return")

def show_menu_artists():
    print("-----Artists Menu-----")
    print("1. List all artists")
    print("2. Search artist by name")
    print("0. Return")

def show_menu_songs():
    print("-----Songs Menu-----")
    print("1. List all songs")
    print("2. Search song by title")
    print("0. Return")

def show_menu_genres():
    print("-----Genres Menu-----")
    print("1. List all genres")
    print("2. Search genre by title")
    print("0. Return")


def open_xml (file_path):
    file_xml = open(file_path, "r").read()

    return BeautifulSoup(file_xml, 'xml')

def load_album (album_num):
    global ALBUMS_PATH

    file_name = "album_"+str(album_num)+".xml"

    file_path = ALBUMS_PATH+file_name

    album_xml = open_xml(file_path)
    
    album = {
            "id": album_xml.album['id'],
            "title": album_xml.title.text,
    }

    album = {
            "id": 1,
            "title": "TITULO!!!",
            "cover": "IMAGEN",
            "artists": [
                {
                    "id": 1,
                    "name": "....."
                },
                {
                    "id": 2,
                    "name": "....."
                }
            ],
            "songs": [
                {
                    "id": 1,
                    "title": "....."
                },
                {
                    "id": 2,
                    "title": "....."
                }
            ]

        }

    return album_xml

print(load_album(1))

sys.exit()











#xml_ejemplo = '<personaje><nombre>Jacinto</nombre><edad valor="33" /></personaje>'

#print(xml_ejemplo)

#personaje = BeautifulSoup(xml_ejemplo, 'xml')

#print(personaje.prettify())

#nombre = personaje.nombre

#print(nombre.contents)
#print(nombre.text)


#song_xml = open("templates/song.xml", "r").read()

#print(song_xm)


#song = BeautifulSoup(song_xml, 'xml')

#print(song.title.text)
#print(song.duration.seconds)
