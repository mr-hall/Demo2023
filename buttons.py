import pygame

class Button():
    def __init__(self, text, x, y, action):
        self.x = x
        self.y = y
        self.text = text
        self.backgroundcolour = (255,255,255)
        self.textcolour = (0, 0, 0)
        self.width = 200
        self.height = 50
        pygame.font.init()
        font = pygame.font.SysFont('Calibri', 25, True, False)
        self.bitmap_of_text = font.render(self.text, True, self.textcolour)
        self.action = action

    def draw(self, screen):
        pygame.draw.rect(screen, self.backgroundcolour, [self.x, self.y, self.width, self.height], 0)

        screen.blit(self.bitmap_of_text, [self.x, self.y])


    def check_if_hover(self):
        rect = pygame.rect.Rect(self.x, self.y,self.width, self.height)
        if rect.collidepoint(pygame.mouse.get_pos()):
            self.backgroundcolour = (0,0,255)
            return True
        else:
            self.backgroundcolour = (255,255,255)
            return False