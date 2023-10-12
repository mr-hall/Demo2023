import pygame

class Button():
    def __init__(self, text):
        self.x = 0
        self.y = 0
        self.text = text
        self.backgroundcolour = (255,255,255)
        self.textcolour = (0, 0, 0)
        self.width = 200
        self.height = 50

    def draw(self, screen):
        pygame.draw.rect(screen, self.backgroundcolour, [self.x, self.y, self.width, self.height], 0)
        font = pygame.font.SysFont('Calibri', 25, True, False)
        text = font.render(self.text, True, self.textcolour)
        screen.blit(text, [self.x, self.y])


    def check_if_hover(self):
        rect = pygame.rect.Rect(self.x, self.y,self.width, self.height)
        if rect.collidepoint(pygame.mouse.get_pos()):
            self.backgroundcolour = (0,0,255)
        else:
            self.backgroundcolour = (255,255,255)