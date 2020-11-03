import pygame
from pygame.locals import *


class Player:
    def __init__(self, screen, start_position, width, color=(255, 255, 0), speed=1):
        self.x, self.y = start_position
        self.screen = screen
        self.color = color
        self.speed = speed
        self.rect = Rect(self.x - (width / 2), self.y - (width / 2), width, width)

    def move_up(self, walls):
        wall_rects = [wall.rect for wall in walls]
        step = self.rect.copy()

        step.center = (self.x, self.y - self.speed)
        if step.collidelist(wall_rects) == -1:
            self.y -= self.speed

        self.rect.center = (self.x, self.y)

    def move_down(self, walls):
        wall_rects = [wall.rect for wall in walls]
        step = self.rect.copy()

        step.center = (self.x, self.y + self.speed)
        if step.collidelist(wall_rects) == -1:
            self.y += self.speed

        self.rect.center = (self.x, self.y)

    def move_left(self, walls):
        wall_rects = [wall.rect for wall in walls]
        step = self.rect.copy()

        step.center = (self.x - self.speed, self.y)
        if step.collidelist(wall_rects) == -1:
            self.x -= self.speed

        self.rect.center = (self.x, self.y)

    def move_right(self, walls):
        wall_rects = [wall.rect for wall in walls]
        step = self.rect.copy()

        step.center = (self.x + self.speed, self.y)
        if step.collidelist(wall_rects) == -1:
            self.x += self.speed

        self.rect.center = (self.x, self.y)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
