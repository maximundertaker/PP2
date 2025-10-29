# PyGame Tutorial: Working with Images

import pygame
import os

_image_library = {}
def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image == None:
        canonicalized_path = path.replace('/', os.sep). replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[path] = image
    return image

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    screen.fill((255, 255, 255))

    screen.blit(get_image('ball.png'), (20, 20))
    pygame.display.flip()
    clock.tick(60)

# Big Scary Warning
# Windows is not case sensitive when it comes to file names. All other major operating 
# systems are. If your file is called ball.png and you use pygame.image.load('BALL.PNG') 
# it will work if you are on windows. However when you give your game to someone running 
# on a mac or linux, it will explode and they won't be very happy with you. So be careful. 
# After a few embarrassing PyWeek hotfixes I had to send out, I now play it safe and make 
# ALL of my image files lowercase. Then in my get_image function, I call .lower() in the 
# canonicalize_path step.

# Setting the alpha of images
# If you have a surface that does not have per-pixel alpha (e.g. a surface you initialized 
# without pygame.SRCALPHA) then you can set the alpha of the whole surface with the set_alpha 
# method. Then, when you blit the image, it will be blitted at the faded opacity. If you would 
# like to blit an image with per-pixel alpha at a faded opacity, that is unfortunately impossible 
# to do directly. However, I did invent a lovely hack to get around this limitation which you can 
# read about here if you are interested.

# If you want to change a 24-bit image to 32-bit or vice versa, use the .convert_alpha() method. 
# For vice-versa, use the .convert() method which will overlay any per-pixel alpha values over black.