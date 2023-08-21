import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint
from time import sleep
import serial
import sys
import time

arduino = serial.Serial('COM3', 9600, timeout=0)
sleep(1)


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="",
                                                           client_secret="",
                                                           redirect_uri="",
                                                           scope="user-read-playback-state,user-modify-playback-state"))

res = sp.current_user_playing_track()
song_name = res['item']['name'] + "\n"
album_name= res['item']['album']['name']
old_song = song_name
current_song = song_name

while (current_song == old_song):
    sleep(1)
    res = sp.current_user_playing_track()
    if (res['item'] is not None):
        current_song = res['item']['name']
        artist_name = "by " + res['item']['album']['artists'][0]['name']
        if (current_song != old_song):
            old_song = current_song
            try:
                arduino.write(current_song.encode())
                sleep(1.1)
                arduino.write(artist_name.encode())

            except OSError:
                print("Write failed!")
    
arduino.close()
