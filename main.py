import os
import sys
import pygame
from gamemap import GameMap
from player import Player

# Initialize pygame instance, which initializes display surface, among other things.
pygame.init()

# Set variables as half the width and height of the first (highest resolution) display mode available.
g_screen_w = int((pygame.display.list_modes()[0][0])/2)
g_screen_h = int((pygame.display.list_modes()[0][1])/2)

# Set display mode screen size to size of background image.
display_surface = pygame.display.set_mode((512, 512))

# Create framerate clock. Set default framerate to 24 fps. Can be changed on load up by gamer.
FPSClock = pygame.time.Clock()
FPS = 24

# Load images and convert pixel format for low latency
background = pygame.image.load("background .png").convert()

# Blit background onto display surface once
display_surface.blit(background, (0, 0))
pygame.display.update()

# Make map object from map json data
level_01 = GameMap("map01.json")
level_01.show_map_data()

# Map sprite class and group

# Create level map sprites and display on screen
for row in level_01.map_data['rows']:
    for index, tile in enumerate(row['tiles']):
        if tile['type'] != 'blank':
            x = 64 * index
            print(f"row height is {row['height']} tile index is {index} so x is {x}")
            y = 512 - (64 * row['height'])
            map_tile = pygame.Surface((64, 64))
            map_tile.fill(pygame.Color(210, 250, 210))
            display_surface.blit(map_tile, (x, y))

# Create and display player character
player_01 = Player("player 1")
display_surface.blit(player_01.image, player_01.position)

pygame.display.update()


# Begin game loop. Run until and unless a Quit Event is triggered or the window is closed.
running = True
while running:

    # Pygame Clock tick to control framerate
    FPSClock.tick(FPS)
    print(f'framerate is currently {FPS} frames per second')

    # If quit event is triggered, quit all pygame modules, then set running to 'False' to exit loop.
    for event in pygame.event.get():
        # Print events so we can see what's going on.
        print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
            print('Game successfully quit!')
        elif event.type == pygame.WINDOWCLOSE:
            pygame.display.quit()
            running = False
            print('window should be quiting now')



if __name__ == '__main__':
    pass
