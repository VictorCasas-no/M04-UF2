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

def menu_opciones():
    while True:
        print("-----Menú-----")
        print("1. Albums")
        print("2. Artists")
        print("3. Songs")
        print("4. Genres")
        print("0. Exit")

        eleccion_menu = input("Elige una opción (entre o y 4)")


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
