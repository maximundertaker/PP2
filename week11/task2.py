import pygame, sys
import random, time

pygame.init()
FramePerSec = pygame.time.Clock()

WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
SCREEN_WIDTH = 400 
SCREEN_HEIGHT = 300
GRID_SIZE = 20
SPEED = 5
SCORE = 0
LEVEL = 1

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

class Snake:
    def __init__(self):
        self.head = [10, 8]
        self.body = [[10, 8], [9, 8], [8, 8]]
        self.direction = 'RIGHT'
        
    def move(self):
        if self.direction == 'RIGHT': self.head[0] += 1
        elif self.direction == 'LEFT': self.head[0] -= 1
        elif self.direction == 'UP': self.head[1] -= 1
        elif self.direction == 'DOWN': self.head[1] += 1

        self.body.insert(0, list(self.head))
        self.body.pop()

    def grow(self):
        self.body.insert(0, list(self.head))

    def check_collision(self):
        if (self.head[0] < 0 or self.head[0] >= 20 or self.head[1] < 0 or self.head[1] >= 15):
            return True
        return self.head in self.body[1:]

class Food:
    def __init__(self):
        self.position = [random.randint(1,18), random.randint(1,13)]
        self.type = random.choice(["normal", "premium", "special"]) #randomly choose food type with different weights
        
        if self.type == "normal":
            self.weight = 1
            self.color = RED
            self.lifetime = 10 #seconds
        elif self.type == "premium":
            self.weight = 2
            self.color = BLUE
            self.lifetime = 7 #seconds
        else:
            self.weight = 3
            self.color = YELLOW
            self.lifetime = 5 #seconds
        self.spawn_time = time.time()
    
    def respawn(self):
        self.position = [random.randint(1,18), random.randint(1,13)]
        self.type = random.choice(["normal", "premium", "special"])
        
        if self.type == "normal":
            self.weight = 1
            self.color = RED
            self.lifetime = 10
        elif self.type == "premium":
            self.weight = 2
            self.color = BLUE
            self.lifetime = 7
        else:
            self.weight = 3
            self.color = YELLOW
            self.lifetime = 5
        self.spawn_time = time.time()
    
    def check_collision(self, head): #situations where snake get collisions with food
        return head[0] == self.position[0] and head[1] == self.position[1]
    
    def disappear(self): #situations where time is out
        return time.time() - self.spawn_time > self.lifetime
    
    def remaining_time(self): #situations where how much time we have while playing
        return max(0, self.lifetime - (time.time() - self.spawn_time))

snake = Snake()
food = Food()
foods_eaten = 0

while True:  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction != 'DOWN':
                snake.direction = 'UP'
            elif event.key == pygame.K_DOWN and snake.direction != 'UP':
                snake.direction = 'DOWN'
            elif event.key == pygame.K_LEFT and snake.direction != 'RIGHT':
                snake.direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and snake.direction != 'LEFT':
                snake.direction = 'RIGHT'

    snake.move()
    
    if snake.check_collision():#check collisions
        pygame.quit()
        sys.exit()

    if food.disappear():#check if food should disappear
        food.respawn()

    if food.check_collision(snake.head):#check food collision
        snake.grow()
        SCORE += food.weight #add food weight instead of just 1
        foods_eaten += food.weight
        
        if foods_eaten >= 3:
            LEVEL += 1
            foods_eaten = 0
            SPEED += 2
        food.respawn()
    
    DISPLAYSURF.fill(BLACK) #draw everything
    pygame.draw.rect(DISPLAYSURF, food.color, (food.position[0]*GRID_SIZE, food.position[1]*GRID_SIZE, GRID_SIZE, GRID_SIZE)) #draw food with its specific color
    
    for segment in snake.body: #draw snake
        pygame.draw.rect(DISPLAYSURF, GREEN, (segment[0]*GRID_SIZE, segment[1]*GRID_SIZE, GRID_SIZE, GRID_SIZE))
    
    font = pygame.font.SysFont("Verdana", 20) #display score and level
    score_text = font.render(f"Score: {SCORE}", True, WHITE)
    level_text = font.render(f"Level: {LEVEL}", True, WHITE)
    food_info = font.render(f"Food: {food.weight}pt", True, WHITE)
    time_left = font.render(f"Time: {int(food.remaining_time())}s", True, WHITE)
    
    DISPLAYSURF.blit(score_text, (10, 10))
    DISPLAYSURF.blit(level_text, (300, 10))
    DISPLAYSURF.blit(food_info, (10, 270))
    DISPLAYSURF.blit(time_left, (300, 270))
                   
    pygame.display.update()
    FramePerSec.tick(SPEED)