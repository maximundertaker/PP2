from game_object import GameObject, Point

class Wall(GameObject):
    def __init__(self, tile_width): # Create border walls around screen
        points = [] # Top and bottom walls
        for x in range(0, 400, tile_width):
            points.append(Point(x, 0))
            points.append(Point(x, 280))
        
        for y in range(20, 280, tile_width): # Left and right walls
            points.append(Point(0, y))
            points.append(Point(380, y))
        super().__init__(points, (255,0,0), tile_width)
    
    def check_collision(self, head):
        for point in self.points: # Check if head hits wall
            if point.X == head.X and point.Y == head.Y:
                return True
        return False