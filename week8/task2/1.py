from msvcrt import getch
import pygame

songs = ['Blinding_Light.mp3', 'Daddy_Issues.mp3', 'Karma_Police.mp3', 'Love_Like_This.mp3']
pygame.mixer.init()

pygame.mixer.music.load(songs[0])
pygame.mixer.music.play()

while True:
    key = ord(getch())
    if key == 27: #ESC
        break
    if key == 13: #Enter
        pygame.mixer.music.unpause()
    if key == 32: #Space
        pygame.mixer.music.pause()
    if key == 8: #Backspace
        pygame.mixer.music.stop()
    if key == 80: #Down arrow - Next
        songs = songs[1:] + [songs[0]]
        pygame.mixer.music.load(songs[0])
        pygame.mixer.music.play()
    if key == 72: #Up arrow - Previous  
        songs = [songs[-1]] + songs[:-1]
        pygame.mixer.music.load(songs[0])
        pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(100)