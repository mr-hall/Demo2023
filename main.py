import pygame
import states

class Main():
    def __init__(self):
        self.WIDTH = 600
        self.HEIGHT = 400
        self.currentScreen = states.Menu()


    def gameloop(self):
        pygame.init()
        size = [self.WIDTH, self.HEIGHT]
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Example code for the draw module")
        done = False
        clock = pygame.time.Clock()
        while not done:
            clock.tick(60)
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    done = True  # Flag that we are done so we exit this loop
                self.currentScreen.handle_input(event)
            self.currentScreen.update()
            self.currentScreen.draw(screen)
            pygame.display.flip()
            if self.currentScreen.next_state:
                self.currentScreen = self.currentScreen.next_state()
        pygame.quit()



main = Main()
main.gameloop()
