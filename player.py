from typing import Any

import pygame
from pygame.sprite import AbstractGroup
import settings


class Player(pygame.sprite.Sprite):
    def __init__(self, name, *groups: AbstractGroup):
        super().__init__(*groups)
        self.name = name
        self.start = (1, 1)
        self.image = pygame.Surface((64, 64))
        self.image.fill((210, 210, 250))
        self.positionRect = self.image.get_rect(topleft=self.start)
        self.velocity = (0, 0)

    def update(self) -> None:
        if self.velocity[1] < settings.terminalVelocity:
            self.velocity = (self.velocity[0] + settings.gravity[0], self.velocity[1] + settings.gravity[1])
            print(f"new velocity is {self.velocity}")
        else:
            print("terminal velocity reached")
        if self.positionRect.bottom < settings.offscreenLimit:
            self.positionRect = self.positionRect.move(self.velocity)
            print(f"new position rect is {self.positionRect}")
        else:
            print("already offscreen")
