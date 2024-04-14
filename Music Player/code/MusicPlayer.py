# Importing the pygame in build library
import pygame # type: ignore

print("Hello World")
# Creating the playlist
playlist=[]
pygame.mixer.init()


#  Function for Adding the Song into The Playlist
def add_song(path):
        playlist.append(path)
    
# Function For Playing the Song 
def play():
     for song in playlist:
         pygame.mixer.music.load(song)
         pygame.mixer.music.play()
         while pygame.mixer.music.get_busy():
             continue        
        
#  Adding the Song's into playlist
 
add_song("C:\\Music\\song.mp3")   
add_song("C:\\Music\\Zehra.mp3")  
add_song("C:\\Music\\Randall.mp3")  

# Playing the song 
play()
         
 