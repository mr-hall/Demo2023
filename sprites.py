import pygame.sprite

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Images/player.png").convert()
        self.rect = self.image.get_rect()
        self.image.set_colorkey((0,0,0))


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Images/enemyShip.png").convert()
        self.rect = self.image.get_rect()
        self.image.set_colorkey((0,0,0))

    def update(self):
        self.rect.y = self.rect.y + 1
