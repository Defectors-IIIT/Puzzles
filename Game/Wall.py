import pygame


class Wall:
    def __init__(self, screen, a, b, color=(255, 255, 255), width=2):
        self.screen = screen
        self.a = a
        self.b = b
        self.color = color
        self.width = width

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

    def draw(self):
        pygame.draw.line(self.screen, self.color, self.a, self.b, self.width)
