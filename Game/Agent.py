import pygame
from pygame.locals import *

from Utils import position, coordinates


class Agent:
    def __init__(
        self,
        screen,
        start_position,
        width,
        color=(255, 255, 0),
        speed=1,
        player=False,
        state="ACTIVE",
    ):
        self.color = color
        self.speed = speed
        self.state = state
        self.screen = screen
        self.player = player
        self.x, self.y = start_position
        self.rect = Rect(self.x - (width / 2), self.y - (width / 2), width, width)

    def activate(self):
        self.state = "ACTIVE"

    def deactivate(self):
        self.state = "INACTIVE"

    def walk(self, algorithm, STATE):
        if self.state == "ACTIVE":
            next_direction = algorithm(self, STATE)
            if next_direction == "N":
                self.target = (self.rect.centerx, self.rect.centery - STATE["cell_width"])
            elif next_direction == "S":
                self.target = (self.rect.centerx, self.rect.centery + STATE["cell_width"])
            elif next_direction == "W":
                self.target = (self.rect.centerx - STATE["cell_width"], self.rect.centery)
            elif next_direction == "E":
                self.target = (self.rect.centerx + STATE["cell_width"], self.rect.centery)
            else:
                self.target = None

            if self.target != None:
                self.state = "MOVING"

        if self.state == "MOVING":
            self.move_to_coordinate(self.target, STATE["walls"])

    def move_to_coordinate(self, coordinate, walls):
        xd = self.rect.centerx - coordinate[0]
        yd = self.rect.centery - coordinate[1]
        if xd == 0 and yd == 0:
            self.state = "ACTIVE"
        else:
            self.state = "MOVING"
            if xd < 0:
                self.move_right(walls)
            elif xd > 0:
                self.move_left(walls)
            elif yd < 0:
                self.move_down(walls)
            elif yd > 0:
                self.move_up(walls)

    def move_up(self, walls):
        if self.state in ["ACTIVE", "MOVING"]:
            wall_rects = [wall.rect for wall in walls]
            step = self.rect.copy()
            step.center = (self.x, self.y - self.speed)
            if step.collidelist(wall_rects) == -1 and (self.y - self.speed) > 0:
                self.y -= self.speed

            self.rect.center = (self.x, self.y)

    def move_down(self, walls):
        if self.state in ["ACTIVE", "MOVING"]:
            wall_rects = [wall.rect for wall in walls]
            step = self.rect.copy()
            step.center = (self.x, self.y + self.speed)
            if (
                step.collidelist(wall_rects) == -1
                and (self.y + self.speed) < self.screen.get_height()
            ):
                self.y += self.speed

            self.rect.center = (self.x, self.y)

    def move_left(self, walls):
        if self.state in ["ACTIVE", "MOVING"]:
            wall_rects = [wall.rect for wall in walls]
            step = self.rect.copy()
            step.center = (self.x - self.speed, self.y)
            if step.collidelist(wall_rects) == -1 and (self.x - self.speed) > 0:
                self.x -= self.speed

            self.rect.center = (self.x, self.y)

    def move_right(self, walls):
        if self.state in ["ACTIVE", "MOVING"]:
            wall_rects = [wall.rect for wall in walls]
            step = self.rect.copy()
            step.center = (self.x + self.speed, self.y)
            if (
                step.collidelist(wall_rects) == -1
                and (self.x + self.speed) < self.screen.get_width()
            ):
                self.x += self.speed

            self.rect.center = (self.x, self.y)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
