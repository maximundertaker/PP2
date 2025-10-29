# PyGame Tutorial: Getting Started

# The Anatomy of a PyGame Game
# The following is the simplest barebones app that can be made using the PyGame pipeline:

# import pygame
# 
# pygame.init()
# screen = pygame.display.set_mode((400,300))
# 
# done = False
# is_blue = True
# 
# while not done:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True
#         if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
#             is_blue = not is_blue
#     
#     if is_blue: color = (0, 128, 255)
#     else: color = (255, 100, 0)
#     
#     pygame.draw.rect(screen, color, pygame.Rect(30, 30, 60, 60))
#     pygame.display.flip()

# import pygame - this is of course needed to access the PyGame framework.
# pygame.init() - This kicks things off. It initializes all the modules required for PyGame.
# pygame.display.set_mode((width, height)) - This will launch a window of the desired size. The return value is a Surface object which is the object you will perform graphical operations on. This will be discussed later.
# pygame.event.get() - this empties the event queue. If you do not call this, the windows messages will start to pile up and your game will become unresponsive in the opinion of the operating system.
# pygame.QUIT - This is the event type that is fired when you click on the close button in the corner of the window.
# pygame.display.flip() - PyGame is double-buffered. This swaps the buffers. All you need to know is that this call is required in order for any updates that you make to the game screen to become visible.

# Drawing Something
# pygame.draw.rect - As you can imagine, this will draw a rectangle. I takes in a few arguments, including the surface to draw on (I'll be drawing on the screen instance), the color, and the coordinates/dimensions of the rectangle.

# The first argument is the surface instance to draw the rectangle to.
# The second argument is the (red, green, blue) tuple that represents the color to draw with.
# The third argument is a pygame.Rect instance. The arguments for this constructor are the x and y coordintaes of the top left corner, the width, and the height.

# Adventuring around
# Our box is bored of switching from aquamarine to orangish red. He wants to move around.
# There is an additional way to access key events. You can get the depression status of any key by calling pygame.key.get_pressed(). This returns a huge array filled with 1's and 0's. Mostly 0's.
# When you check the integer value of any of the pygame.K_%%%%% constants, you'll notice it's a number.
# >>> pygame.K_LEFTBRACKET
# 91
# >>> 
# This value is not-so-coincidentally the index of the get_pressed() array that corresponds to that key. So if you want to see if the Up Arrow is pressed, the way to do that is:
# *** up_pressed = pygame.get_pressed()[pygame.K_UP] ***
# Simple as that.
# This is useful for the sort of events that you want to do when the user holds down a button. For example, moving around a sprite when the user holds down any arrow keys.
# Applying this concept to our current box game, this is what the code looks like now:

import pygame
pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
is_blue = True
x = 30
y = 30

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= 3
    if pressed[pygame.K_DOWN]: y += 3
    if pressed[pygame.K_LEFT]: x -= 3
    if pressed[pygame.K_RIGHT]: x += 3

    screen.fill((0,0,0))
    if is_blue: 
        color = (0, 128, 255)
    else:
        color = (255, 100, 0)
    pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))
    pygame.display.flip()
    clock.tick(60)

# For the first, you simply need to reset the screen to black before you draw the rectangle. There is a simple method on Surface called fill that does this. It takes in an rgb tuple.
# screen.fill((0, 0, 0))

# Secondly, the duration of each frame is as short as your super fancy computer can make it. The framerate needs to be throttled at a sane number such as 60 frames per second. Luckily, there is a simple class in pygame.time called Clock that does this for us. It has a method called tick which takes in a desired fps rate.
# clock = pygame.time.Clock()
# ...
# while not done:
# 
#     ...
# 
#     # will block execution until 1/60 seconds have passed
#     # since the previous time clock.tick was called.
#     clock.tick(60)