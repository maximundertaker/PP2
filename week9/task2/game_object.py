import pygame

class Point:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

class GameObject:
    def __init__(self, points, color, tile_width):
        self.points = points
        self.color = color
        self.tile_width = tile_width

    def draw(self, screen):
        for point in self.points:
            pygame.draw.rect(screen, self.color, (point.X, point.Y, self.tile_width, self.tile_width))