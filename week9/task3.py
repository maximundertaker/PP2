import pygame, sys
from pygame.locals import *
from math import sqrt

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

class Tool:
    def __init__(self):
        self.start_pos = (-1, -1)
        self.current_pos = (-1, -1)
        self.color = WHITE
        self.active = False

tools = {
    "pencil": Tool(),
    "rectangle": Tool(), 
    "circle": Tool(),
    "eraser": Tool()
}

current_tool = "pencil"
base_layer = pygame.Surface((640, 480))
base_layer.fill(BLACK)
screen.fill(BLACK)

pygame.display.set_caption("Paint - Pencil")

while True:  
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            tools[current_tool].start_pos = event.pos
            tools[current_tool].current_pos = event.pos
            tools[current_tool].active = True
                    
        if event.type == MOUSEBUTTONUP and event.button == 1:
            tools[current_tool].active = False
            base_layer.blit(screen, (0, 0))
                
        if event.type == MOUSEMOTION:
            tools[current_tool].current_pos = event.pos
            
        if event.type == KEYDOWN:
            if event.key == K_1: 
                current_tool = "pencil"
                pygame.display.set_caption("Paint - Pencil")
            elif event.key == K_2: 
                current_tool = "rectangle"
                pygame.display.set_caption("Paint - Rectangle")
            elif event.key == K_3: 
                current_tool = "circle"
                pygame.display.set_caption("Paint - Circle")
            elif event.key == K_4: 
                current_tool = "eraser"
                pygame.display.set_caption("Paint - Eraser")
            elif event.key == K_q:
                for tool in tools.values(): tool.color = RED
            elif event.key == K_g:
                for tool in tools.values(): tool.color = GREEN
            elif event.key == K_e:
                for tool in tools.values(): tool.color = BLUE
            elif event.key == K_w:
                for tool in tools.values(): tool.color = WHITE

    tool = tools[current_tool]
    if tool.active:
        if current_tool == "pencil":
            pygame.draw.line(screen, tool.color, tool.start_pos, tool.current_pos)
            tool.start_pos = tool.current_pos
            
        elif current_tool == "rectangle":
            screen.blit(base_layer, (0, 0))
            x1, y1 = tool.start_pos
            x2, y2 = tool.current_pos
            rect = (min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))
            pygame.draw.rect(screen, tool.color, pygame.Rect(rect), 1)
            
        elif current_tool == "circle":
            screen.blit(base_layer, (0, 0))
            x1, y1 = tool.start_pos
            x2, y2 = tool.current_pos
            center = (abs(x1 - x2) / 2 + min(x1, x2), abs(y1 - y2) / 2 + min(y1, y2))
            radius = sqrt(((abs(x1 - x2) / 2) ** 2 + (abs(y1 - y2) / 2) ** 2))
            pygame.draw.circle(screen, tool.color, (int(center[0]), int(center[1])), int(radius), 1)
            
        elif current_tool == "eraser":
            pygame.draw.line(screen, BLACK, tool.start_pos, tool.current_pos, 30)
            tool.start_pos = tool.current_pos

    pygame.display.update()
    clock.tick(60)