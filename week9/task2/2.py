import pygame
from worm import Worm
from food import Food
from wall import Wall

def create_background(screen):
    colors = [(255,255,255), (212,212,212)]
    for y in range(0,300,20):
        for x in range(0,400,20):
            c = colors[(y//20 + x//20) % 2]
            pygame.draw.rect(screen, c, (x,y,20,20))

pygame.init()
screen = pygame.display.set_mode((400,300))
clock = pygame.time.Clock()

worm = Worm(20)
food = Food(20)
wall = Wall(20)

speed = 5
score = 0
level = 1
foods_in_level = 0

done = False
while not done:
    events = []
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        else:
            events.append(event)

    worm.process_input(events)
    worm.move()
    
    if wall.check_collision(worm.points[0]):
        done = True
    
    if worm.check_self_collision():
        done = True
    
    if food.check_collision(worm.points[0]):
        worm.grow()
        food.respawn()
        score += 1
        foods_in_level += 1
        
        if foods_in_level >= 2:
            level += 1
            foods_in_level = 0
            speed += 1
    
    create_background(screen)
    food.draw(screen)
    wall.draw(screen)
    worm.draw(screen)
    
    font = pygame.font.SysFont("Arial", 20)
    score_text = font.render(f"Foods: {score}", True, (0,0,0))
    level_text = font.render(f"Level: {level}", True, (0,0,0))
    screen.blit(score_text, (10,10))
    screen.blit(level_text, (300,10))
    
    pygame.display.flip()
    clock.tick(speed)
pygame.quit()