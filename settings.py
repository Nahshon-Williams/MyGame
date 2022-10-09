import pygame

# Initialize pygame instance, which initializes display surface, among other things.
pygame.init()

# Set variables as half the width and height of the first (highest resolution) display mode available.
screenW = int((pygame.display.list_modes()[0][0])/2)
screenH = int((pygame.display.list_modes()[0][1])/2)

tileSize = (64, 64)

offscreenLimit = screenH + tileSize[0]

# Create framerate clock. Set default framerate to 24 fps. Can be changed on load up by gamer.
FPSClock = pygame.time.Clock()
FPS = 24

# Acceleration due to gravity
gravity = (0, 3)
terminalVelocity = 45
