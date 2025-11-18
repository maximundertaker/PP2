import pygame, sys
from pygame.locals import *
import random, time

pygame.init()
FramePerSec = pygame.time.Clock()

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COIN_COUNT = 0
COIN_THRESHOLD = 5  #number of coins needed to increase enemy speed
 
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
 
background = pygame.image.load("road.png")

DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")
 
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  
 
    def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
       #if pressed_keys[K_UP]:
           #self.rect.move_ip(0, -5)
       #if pressed_keys[K_DOWN]:
           #self.rect.move_ip(0,5)
         
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        coin_type = random.choice(["small", "medium", "big"])
        
        if coin_type == "small":
            self.image = pygame.image.load("coin.png")
            self.weight = 1
            self.speed = random.randint(3, 5)
        elif coin_type == "medium":
            self.image = pygame.image.load("coin.png")
            self.image = pygame.transform.scale(self.image, (30, 30))
            self.weight = 2
            self.speed = random.randint(4, 6)
        else:
            self.image = pygame.image.load("coin.png")
            self.image = pygame.transform.scale(self.image, (40, 40))
            self.weight = 3
            self.speed = random.randint(5, 7)
            
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

    def move(self):
        self.rect.move_ip(0, self.speed)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
     
P1 = Player()
E1 = Enemy()
C1 = Coin()

enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

while True:  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5     
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
 
    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    coin_count = font_small.render(f"Coins: {COIN_COUNT}", True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
    DISPLAYSURF.blit(coin_count, (10, 40))

    for entity in all_sprites: #moves and re-draws all Sprites
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
 
    if pygame.sprite.spritecollideany(P1, enemies): #collision between player and enemy
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(0.5)
                    
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30,250))
           
        pygame.display.update()
        for entity in all_sprites:
            entity.kill() 
        time.sleep(2)
        pygame.quit()
        sys.exit()     

    coin_collisions = pygame.sprite.spritecollide(P1, coins, True) #collision between player and coin
    for coin in coin_collisions:
        COIN_COUNT += coin.weight  #add coin weight instead of just 1
        
        if COIN_COUNT >= COIN_THRESHOLD: #increase enemy speed when reaching coin threshold
            SPEED += 0.5
            COIN_THRESHOLD += 5  #set next threshold
            
        new_coin = Coin() #create a new coin to replace
        coins.add(new_coin)
        all_sprites.add(new_coin)
                   
    pygame.display.update()
    FramePerSec.tick(60)