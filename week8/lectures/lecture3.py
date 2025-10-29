# PyGame Tutorial: Music and Sound Effects

# The sound and music API's are fairly simple. I feel funny basically going through the documentation and re-iterating it. However, I'll show you some non straightforward tricks as well, like playing a set of songs on shuffle.
# But first, the basics...
# 
# 1. Playing a song once:
pygame.mixer.music.load('foo.mp3')
pygame.mixer.music.play(0)
# 
# 2. Playing a song infinitely:
pygame.mixer.music.load('foo.mp3')
pygame.mixer.music.play(-1)
# 
# The number being passed in is the number of times to repeat the song. 0 will play it once.
# Calling play without a number is like calling it with 0.
pygame.mixer.music.play() # play once
# 
# 3. Queuing a Song:
# If you want a song to start playing immediately after a song is finished, then you can use there's a queue method.
pygame.mixer.music.queue('next_song.mp3')
# 
# 4. Stopping a Song:
pygame.mixer.music.stop()
# 
# The stop function will also nullify any entries in the queue.
# 
# 5. Doing Something When a Song Ends:
# The times that you really need a queue are rare. Typically you'll just want to play the same song over again until you change it. But suppose you want to play a selection of 4 or 5 songs in sequence over and over again. Or even play randomly from a list of songs forever. At this point it's better to implement your own logic and use the handy set_endevent function.
# In part 1, I showed you how to pump the event queue. When going through the events, you check the event.type field and see if it's pygame.QUIT or pygame.KEYDOWN, etc. These type values are just integers. When you call the set_endevent function, it expects a number as input. Its value will be used in the event.type field when the song nautrally ends. Confused? Here's some code...
...
SONG_END = pygame.USEREVENT + 1

pygame.mixer.music.set_endevent(SONG_END)
pygame.mixer.music.load('song.mp3')
pygame.mixer.music.play()
...

while True:
    ...
    for event in pygame.event.get():
        ...
        if event.type == SONG_END:
            print("the song ended!")
    ...
# The USEREVENT + 1 is to ensure that the number assigned to SONG_END isn't inadvertently equal to any other predefined event. Like pygame.VIDEORESIZE or something. USEREVENT has the highest value in the enum.
# 
# 6. Shuffle and Repeat:
# If, for example, you wanted to play randomly from a list of 5 songs, one could create a list of the songs as a global:
_songs = ['song_1.mp3', 'song_2.mp3', 'song_3.mp3', 'song_4.mp3', 'song_5.mp3']
# 
# Add a flag indicating which song is currently playing:
_currently_playing_song = None
# 
# And write a function that chooses a different song randomly that gets called each time the SONG_END event is fired:

import random
def play_a_different_song():
    global _currently_playing_song, _songs
    next_song = random.choice(_songs)
    while next_song == _currently_playing_song:
        next_song = random.choice(_songs)
    _currently_playing_song = next_song
    pygame.mixer.music.load(next_song)
    pygame.mixer.music.play()

Or if you want them to play in the same sequence each time:

def play_next_song():
    global _songs
    _songs = _songs[1:] + [_songs[0]] # move current song to the back of the list
    pygame.mixer.music.load(_songs[0])
    pygame.mixer.music.play()

# 7. Sounds
# The music API is very centralized. However sounds require the creation of sound objects that you have to hold on to. Much like images. Sounds have a simple .play() method that will start playing the sound.
effect = pygame.mixer.Sound('beep.wav')
effect.play()
# 
# Because you can make the mistake of storing sound instances redundantly, I suggest creating a sound library much like the image library from part 2.
_sound_library = {}
def play_sound(path):
  global _sound_library
  sound = _sound_library.get(path)
  if sound == None:
    canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
    sound = pygame.mixer.Sound(canonicalized_path)
    _sound_library[path] = sound
  sound.play()
# There are many more features but this is really all you need to do 95% of what most games will require of you.