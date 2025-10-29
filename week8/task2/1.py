from msvcrt import getch
import pygame

songs = ['Blinding_Light.mp3', 'Daddy_Issues.mp3', 'Karma_Police.mp3', 'Love_Like_This.mp3']
pygame.mixer.init()

pygame.mixer.music.load(songs[0])
pygame.mixer.music.play()

while True:
    key = ord(getch())
    if key == 27: #esc
        break
    if key == 13: #enter
        pygame.mixer.music.unpause()
    if key == 32: #space
        pygame.mixer.music.pause()
    if key == 8: #backspace
        pygame.mixer.music.stop()
    if key == 80: #down arrow - next
        songs = songs[1:] + [songs[0]]
        pygame.mixer.music.load(songs[0])
        pygame.mixer.music.play()
    if key == 72: #up arrow - previous  
        songs = [songs[-1]] + songs[:-1]
        pygame.mixer.music.load(songs[0])
        pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(100)