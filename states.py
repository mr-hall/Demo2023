import pygame

import buttons
import sprites
import random

class State():
    def __init__(self):
        self.next_state = None
        return

    def draw(self):
        pass

    def update(self):
        pass

    def handle_input(self, event):
        pass

class Game(State):
    def __init__(self):
        super().__init__()
        self.player = sprites.Player()
        self.player.rect.y = 300
        self.player.rect.x = 300
        self.enemies = pygame.sprite.Group()
        for i in range(13):
            enemy = sprites.Enemy()
            enemy.rect.x = random.randint(0, 400)
            self.enemies.add(enemy)
        return

    def draw(self, screen):
        screen.fill((255,0,0))
        self.enemies.draw(screen)
        screen.blit(self.player.image, self.player.rect)

    def update(self):
        self.enemies.update()

class Menu(State):
    def __init__(self):
        super().__init__()
        button1 = buttons.Button("Start Game", 50,50, Game)
        button2 = buttons.Button("Options", 50, 100, None)
        button3 = buttons.Button("Exit", 50, 150, None)
        self.list_of_buttons = [button1, button2, button3]

    def draw(self, screen):
        screen.fill((0,255,0))
        for button in self.list_of_buttons:
            button.draw(screen)

    def update(self):
        for button in self.list_of_buttons:
            button.check_if_hover()

    def handle_input(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for button in self.list_of_buttons:
                if button.check_if_hover():
                    self.next_state = button.action
