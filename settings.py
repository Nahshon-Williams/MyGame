import pygame

# Set variables as half the width and height of the first (highest resolution) display mode available.
screenW = int((pygame.display.list_modes()[0][0])/2)
screenH = int((pygame.display.list_modes()[0][1])/2)

tileSize = (64, 64)

# Create framerate clock. Set default framerate to 24 fps. Can be changed on load up by gamer.
FPSClock = pygame.time.Clock()
FPS = 24
