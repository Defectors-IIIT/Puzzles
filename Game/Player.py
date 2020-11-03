import pygame
from pygame.locals import *


class Player:
    def __init__(self, screen, start_position, width, color=(255, 255, 0), speed=1):
        self.screen = screen
        self.position = list(start_position)
        self.color = color
        self.speed = speed
        self.rect = Rect(self.position[0], self.position[1], width, width)

    def move_up(self, walls):
        wall_rects = [wall.rect for wall in walls]
        if self.rect.move(0, -self.speed).collidelist(wall_rects) == -1:
            self.rect.move_ip(0, -self.speed)

    def move_down(self, walls):
        wall_rects = [wall.rect for wall in walls]
        if self.rect.move(0, self.speed).collidelist(wall_rects) == -1:
            self.rect.move_ip(0, self.speed)

    def move_left(self, walls):
        wall_rects = [wall.rect for wall in walls]
        if self.rect.move(-self.speed, 0).collidelist(wall_rects) == -1:
            self.rect.move_ip(-self.speed, 0)

    def move_right(self, walls):
        wall_rects = [wall.rect for wall in walls]
        if self.rect.move(self.speed, 0).collidelist(wall_rects) == -1:
            self.rect.move_ip(self.speed, 0)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
