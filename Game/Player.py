import pygame


class Player:
    def __init__(self, screen, start_position, width, color=(255, 255, 255), speed=0.5):
        self.screen = screen
        self.position = list(start_position)
        self.width = width
        self.color = color
        self.speed = speed

    def move_up(self):
        self.position[1] -= self.speed

    def move_down(self):
        self.position[1] += self.speed

    def move_left(self):
        self.position[0] -= self.speed

    def move_right(self):
        self.position[0] += self.speed

    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.position, self.width)
