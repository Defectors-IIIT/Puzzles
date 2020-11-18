import pygame
from pygame.locals import *


class Wall:
    def __init__(self, screen, a, b, color=(255, 255, 255)):
        self.screen = screen
        self.a = a
        self.b = b
        self.color = color

        if a[0] == b[0]:
            self.height = abs(a[1] - b[1])
            self.width = 2
        else:
            self.height = 2
            self.width = abs(a[0] - b[0])

        self.rect = Rect(min(a[0], b[0]), min(a[1], b[1]), self.width, self.height)

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
