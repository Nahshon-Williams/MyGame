import pygame
from pygame.sprite import AbstractGroup


class Player(pygame.sprite.Sprite):
    def __init__(self, name, *groups: AbstractGroup):
        super().__init__(*groups)
        self.name = name
        self.position = (1, 1)
        self.image = pygame.Surface((64, 64))
        self.image.fill((210, 210, 250))
        self.rect = self.image.get_rect()

