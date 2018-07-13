import sys
import pygame
from settings import Settings

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Alien Invasion")
    #set the background color.
    bg_color = (230,230,230)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            screen.fill(ai_settings.bg_color)
        
        pygame.display.flip()
# Added new comment
run_game()
