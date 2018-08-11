import pygame


class Ship:
    def __int__(self, screen):
        """Initialize the ship and sets its starting position."""
        self.screen = screen

        # Load the ship image and gets its rect.
        self.image = pygame.image.load('D:/Learning/python project/alien_invasion/images/jet1.bmp')
        self.rect = self.image.get_rect()  # get_rect() method is used to access the surface's rect attributes
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
