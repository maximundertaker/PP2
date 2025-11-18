import pygame, sys
from pygame.locals import *
from math import sqrt, cos, sin, radians

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
    "eraser": Tool(),
    "square": Tool(),
    "right_triangle": Tool(),
    "equilateral_triangle": Tool(),
    "rhombus": Tool()
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
            elif event.key == K_5: 
                current_tool = "square"
                pygame.display.set_caption("Paint - Square")
            elif event.key == K_6: 
                current_tool = "right_triangle"
                pygame.display.set_caption("Paint - Right Triangle")
            elif event.key == K_7: 
                current_tool = "equilateral_triangle"
                pygame.display.set_caption("Paint - Equilateral Triangle")
            elif event.key == K_8: 
                current_tool = "rhombus"
                pygame.display.set_caption("Paint - Rhombus")
            elif event.key == K_q:
                for tool in tools.values(): tool.color = RED
            elif event.key == K_r:
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
            pygame.draw.rect(screen, tool.color, pygame.Rect(rect), 1) #min coordinates and width/height differences
            
        elif current_tool == "circle":
            screen.blit(base_layer, (0, 0))
            x1, y1 = tool.start_pos
            x2, y2 = tool.current_pos
            center = (abs(x1 - x2) / 2 + min(x1, x2), abs(y1 - y2) / 2 + min(y1, y2))
            radius = sqrt(((abs(x1 - x2) / 2) ** 2 + (abs(y1 - y2) / 2) ** 2)) #center as midpoint, radius using pythagorean theorem
            pygame.draw.circle(screen, tool.color, (int(center[0]), int(center[1])), int(radius), 1)
            
        elif current_tool == "eraser":
            pygame.draw.line(screen, BLACK, tool.start_pos, tool.current_pos, 30) #simple line as the pencil
            tool.start_pos = tool.current_pos
            
        elif current_tool == "square":
            screen.blit(base_layer, (0, 0))
            x1, y1 = tool.start_pos
            x2, y2 = tool.current_pos
            size = min(abs(x1 - x2), abs(y1 - y2))
            rect = (min(x1, x2), min(y1, y2), size, size)
            pygame.draw.rect(screen, tool.color, pygame.Rect(rect), 1) #using smallest side for both dimensions
            
        elif current_tool == "right_triangle":
            screen.blit(base_layer, (0, 0))
            x1, y1 = tool.start_pos
            x2, y2 = tool.current_pos
            points = [
                (x1, y1),
                (x1, y2),
                (x2, y2)
            ]
            pygame.draw.polygon(screen, tool.color, points, 1) #three points forming 90-degree angle
            
        elif current_tool == "equilateral_triangle":
            screen.blit(base_layer, (0, 0))
            x1, y1 = tool.start_pos
            x2, y2 = tool.current_pos
            side_length = sqrt((x2 - x1)**2 + (y2 - y1)**2)
            height = (sqrt(3) / 2) * side_length 

            points = [
                (x1, y1),
                (x1 + side_length, y1),
                (x1 + side_length / 2, y1 - height)
            ]
            pygame.draw.polygon(screen, tool.color, points, 1)
            
        elif current_tool == "rhombus":
            screen.blit(base_layer, (0, 0))
            x1, y1 = tool.start_pos
            x2, y2 = tool.current_pos
            center_x = (x1 + x2) / 2
            center_y = (y1 + y2) / 2
            width = abs(x2 - x1) / 2
            height = abs(y2 - y1) / 2
            
            points = [
                (center_x, center_y - height),
                (center_x + width, center_y), 
                (center_x, center_y + height),
                (center_x - width, center_y)  
            ]
            pygame.draw.polygon(screen, tool.color, points, 1) #four points around center along axes

    pygame.display.update()
    clock.tick(60)