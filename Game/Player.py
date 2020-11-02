import pygame

# singular point 'p' and a line defined by points 'a' and 'b'
def collides(a, b, p, offset):
    x1, y1 = a
    x2, y2 = b
    x0, y0 = p
    d_ap = ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5
    d_bp = ((x2 - x0) ** 2 + (y2 - y0) ** 2) ** 0.5
    d_ab = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return not ((d_ap + d_bp) > d_ab)


class Player:
    def __init__(self, screen, start_position, width, color=(255, 255, 255), speed=0.2):
        self.screen = screen
        self.position = list(start_position)
        self.width = width
        self.color = color
        self.speed = speed

    def move_up(self, WALLS):
        x, y = self.position
        for wall in WALLS:
            if collides(wall.a, wall.b, (x, y - self.speed), 1):
                return

        self.position[1] -= self.speed

    def move_down(self, WALLS):
        x, y = self.position
        for wall in WALLS:
            if collides(wall.a, wall.b, (x, y + self.speed), 1):
                return

        self.position[1] += self.speed

    def move_left(self, WALLS):
        x, y = self.position
        for wall in WALLS:
            if collides(wall.a, wall.b, (x - self.speed, y), 1):
                return

        self.position[0] -= self.speed

    def move_right(self, WALLS):
        x, y = self.position
        for wall in WALLS:
            if collides(wall.a, wall.b, (x + self.speed, y), 1):
                return

        self.position[0] += self.speed

    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.position, self.width)
