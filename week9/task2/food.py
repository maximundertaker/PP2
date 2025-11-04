import random
from game_object import GameObject, Point

class Food(GameObject):
    def __init__(self, tile_width):
        self.tile_width = tile_width
        points = [self.generate_position()]
        super().__init__(points, (0,255,0), tile_width)
    
    def generate_position(self):
        x = random.randint(1, 19) * 20 # Generate random position within play area
        y = random.randint(1, 14) * 20
        return Point(x, y)
    
    def check_collision(self, head):
        for point in self.points: # Check if snake eats food
            if point.X == head.X and point.Y == head.Y:
                return point
        return None
    
    def respawn(self):
        self.points[0] = self.generate_position() # Move food to new position