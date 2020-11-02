import pygame


class Wall:
    def __init__(self, screen, a, b, color=(255, 255, 255), width=2):
        self.screen = screen
        self.point_a = a
        self.point_b = b
        self.position = (((a[0] + b[0]) / 2), (a[1] + b[1] / 2))
        self.length = abs((a[0] - b[0]) + (a[1] - b[1]))
        self.color = color
        self.width = width

    def draw(self):
        pygame.draw.line(self.screen, self.color, self.point_a, self.point_b, self.width)
