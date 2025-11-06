import pygame, sys
import random

pygame.init()
FramePerSec = pygame.time.Clock()

WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)
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
        if (self.head[0] < 0 or self.head[0] >= 20 or 
            self.head[1] < 0 or self.head[1] >= 15):
            return True
        return self.head in self.body[1:]

class Food:
    def __init__(self):
        self.position = [random.randint(1,18), random.randint(1,13)]
    
    def respawn(self):
        self.position = [random.randint(1,18), random.randint(1,13)]
    
    def check_collision(self, head):
        return head[0] == self.position[0] and head[1] == self.position[1]

snake = Snake() # Create objects
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
    
    if snake.check_collision(): # Check collisions
        pygame.quit()
        sys.exit()

    if food.check_collision(snake.head): # Check food collision
        snake.grow()
        food.respawn()
        SCORE += 1
        foods_eaten += 1
        
        if foods_eaten >= 3:
            LEVEL += 1
            foods_eaten = 0
            SPEED += 2

    
    DISPLAYSURF.fill(BLACK) # Draw everything
    pygame.draw.rect(DISPLAYSURF, RED, (food.position[0]*GRID_SIZE, food.position[1]*GRID_SIZE, GRID_SIZE, GRID_SIZE)) # Draw food
    
    for segment in snake.body: # Draw snake
        pygame.draw.rect(DISPLAYSURF, GREEN, (segment[0]*GRID_SIZE, segment[1]*GRID_SIZE, GRID_SIZE, GRID_SIZE))
    
    font = pygame.font.SysFont("Arial", 20) # Display score and level
    score_text = font.render(f"Score: {SCORE}", True, WHITE)
    level_text = font.render(f"Level: {LEVEL}", True, WHITE)
    DISPLAYSURF.blit(score_text, (10, 10))
    DISPLAYSURF.blit(level_text, (300, 10))
                   
    pygame.display.update()
    FramePerSec.tick(SPEED)