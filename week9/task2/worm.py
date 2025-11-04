import pygame
from game_object import GameObject, Point

class Worm(GameObject):
    def __init__(self, tile_width): # Start with 2 segments
        super().__init__([Point(60, 60), Point(40, 60)], (0,0,255), tile_width)
        self.DX = 1
        self.DY = 0

    def move(self): # Move body segments
        for i in range(len(self.points)-1, 0, -1):
            self.points[i].X = self.points[i-1].X
            self.points[i].Y = self.points[i-1].Y
        self.points[0].X += self.DX * self.tile_width # Move head
        self.points[0].Y += self.DY * self.tile_width

    def grow(self):
        self.points.append(Point(self.points[-1].X, self.points[-1].Y)) # Add new segment
    
    def check_self_collision(self):
        head = self.points[0] # Check if head hits body
        for segment in self.points[1:]:
            if head.X == segment.X and head.Y == segment.Y:
                return True
        return False

    def process_input(self, events):
        for event in events: # Handle arrow keys
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.DY != 1:
                    self.DX, self.DY = 0, -1
                elif event.key == pygame.K_DOWN and self.DY != -1:
                    self.DX, self.DY = 0, 1
                elif event.key == pygame.K_RIGHT and self.DX != -1:
                    self.DX, self.DY = 1, 0
                elif event.key == pygame.K_LEFT and self.DX != 1:
                    self.DX, self.DY = -1, 0