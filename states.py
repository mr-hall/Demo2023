import buttons

class State():
    def __init__(self):
        return

    def draw(self):
        pass

    def update(self):
        pass

    def handle_input(self, event):
        pass

class Game(State):
    def __init__(self):
        return

    def draw(self, screen):
        screen.fill((255,0,0))

class Menu(State):
    def __init__(self):
        button1 = buttons.Button("Start Game")
        self.list_of_buttons = [button1]

    def draw(self, screen):
        screen.fill((0,255,0))
        for button in self.list_of_buttons:
            button.draw(screen)

    def update(self):
        for button in self.list_of_buttons:
            button.check_if_hover()
