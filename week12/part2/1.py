import pygame
import random
import psycopg2
from config import load_config

WIDTH, HEIGHT = 400, 300
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

def setup_database():
    conn = None
    try:
        config = load_config()
        conn = psycopg2.connect(**config)
        conn.autocommit = True
        cur = conn.cursor()
        
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                username VARCHAR(50) PRIMARY KEY,
                level INTEGER DEFAULT 1,
                score INTEGER DEFAULT 0
            )
        """)
        print("Table created successfully")
        cur.close()
    except Exception as e:
        print("DB setup error:", e)
    finally:
        if conn: conn.close()

def get_user_level(username):
    conn = None
    try:
        config = load_config()
        conn = psycopg2.connect(**config)
        cur = conn.cursor()
        
        cur.execute("SELECT level, score FROM users WHERE username = %s", (username,))
        result = cur.fetchone()
        
        if result:
            level, score = result
            print(f"Welcome back {username}! Level: {level}, Score: {score}")
            return level
        else:
            cur.execute("INSERT INTO users (username, level, score) VALUES (%s, 1, 0)", (username,))
            conn.commit()
            print(f"New user {username} created! Starting at level 1")
            return 1
    except Exception as e:
        print("DB error:", e)
        return 1
    finally:
        if conn: conn.close()

def save_score(username, level, score):
    conn = None
    try:
        config = load_config()
        conn = psycopg2.connect(**config)
        cur = conn.cursor()
        
        cur.execute("SELECT 1 FROM users WHERE username = %s", (username,))
        if cur.fetchone():
            cur.execute("UPDATE users SET level = %s, score = %s WHERE username = %s", 
                       (level, score, username))
        else:
            cur.execute("INSERT INTO users (username, level, score) VALUES (%s, %s, %s)", 
                       (username, level, score))
        
        conn.commit()
        print(f"Score saved! Level: {level}, Score: {score}")
        cur.close()
    except Exception as e:
        print("DB error:", e)
    finally:
        if conn: conn.close()

class Snake:
    def __init__(self):
        self.head = [GRID_WIDTH//2, GRID_HEIGHT//2]
        self.body = [[self.head[0], self.head[1]], [self.head[0]-1, self.head[1]], [self.head[0]-2, self.head[1]]]
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
        if self.head[0] < 0 or self.head[0] >= GRID_WIDTH or self.head[1] < 0 or self.head[1] >= GRID_HEIGHT:
            return True
        return self.head in self.body[1:]

class Food:
    def __init__(self):
        self.position = [random.randint(1, GRID_WIDTH-2), random.randint(1, GRID_HEIGHT-2)]
    
    def respawn(self):
        self.position = [random.randint(1, GRID_WIDTH-2), random.randint(1, GRID_HEIGHT-2)]

def main():
    username = input("Enter your username: ").strip()
    if not username:
        print("Username required!")
        return
    
    setup_database()
    level = get_user_level(username)
    
    speeds = {1: 5, 2: 7, 3: 10}
    speed = speeds.get(level, 5)
    
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(f"Snake Game - Level {level}")
    clock = pygame.time.Clock()
    
    snake = Snake()
    food = Food()
    score = 0
    foods_eaten = 0
    
    print(f"Level: {level}, Speed: {speed}")
    print("Controls: Arrow keys, P to save and quit")
    
    done = True
    while done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != 'DOWN':
                    snake.direction = 'UP'
                elif event.key == pygame.K_DOWN and snake.direction != 'UP':
                    snake.direction = 'DOWN'
                elif event.key == pygame.K_LEFT and snake.direction != 'RIGHT':
                    snake.direction = 'LEFT'
                elif event.key == pygame.K_RIGHT and snake.direction != 'LEFT':
                    snake.direction = 'RIGHT'
                elif event.key == pygame.K_p:
                    save_score(username, level, score)
                    done = False
        
        snake.move()
        
        if snake.check_collision():
            save_score(username, level, score)
            print("Game Over!")
            done = False
            continue
        
        if snake.head == food.position:
            snake.grow()
            score += 1
            foods_eaten += 1
            food.respawn()
            
            if foods_eaten >= 3 and level < 3:
                level += 1
                speed = speeds[level]
                foods_eaten = 0
                pygame.display.set_caption(f"Snake Game - Level {level}")
                print(f"Level up! Now level {level}")
        
        screen.fill(BLACK)
        pygame.draw.rect(screen, RED, (food.position[0]*GRID_SIZE, food.position[1]*GRID_SIZE, GRID_SIZE, GRID_SIZE))
        
        for segment in snake.body:
            pygame.draw.rect(screen, GREEN, (segment[0]*GRID_SIZE, segment[1]*GRID_SIZE, GRID_SIZE, GRID_SIZE))
        
        font = pygame.font.SysFont("Arial", 20)
        score_text = font.render(f"Score: {score}", True, WHITE)
        level_text = font.render(f"Level: {level}", True, WHITE)
        screen.blit(score_text, (10, 10))
        screen.blit(level_text, (300, 10))
        
        pygame.display.update()
        clock.tick(speed)
    
    pygame.quit()

if __name__ == "__main__":
    main()