import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single aline in the fleet"""
    def __init__(self, ai_game):
        super(Alien, self).__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Loads the alien image and sets its attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # starting each alien at the top left of the game window
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # stores the alien exact horizontal position
        self.x = float(self.rect.x)

    def update(self):
        """Move the alien to right or left"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """Return True if alien has hit its edge"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
