import pygame
pygame.init()


class StockMenu:
    # Define the initalize self options
    def __init__(self, *options):
        self.options = options
        self.x = 0
        self.y = 0
        self.font = pygame.font.Font(None, 32)
        self.option = 0
        self.width = 1
        self.color = [0, 0, 0]
        self.hcolor = [0, 0, 0]
        self.height = len(self.options)*self.font.get_height()
        for o in self.options:
            text = o[0]
            ren = self.font.render(text, True, (0, 0, 0))
            if ren.get_width() > self.width:
                self.width = ren.get_width()

# Draw the menu
    def draw(self, surface):
        i = 0
        for o in self.options:
            if i == self.option:
                clr = self.hcolor
            else:
                clr = self.color
            text = o[0]
            ren = self.font.render(text, True, clr)
            if ren.get_width() > self.width:
                self.width = ren.get_width()
            surface.blit(ren, (self.x, self.y + i * self.font.get_height()))
            i += 1

# Menu Input
    def update(self, events):
        for e in events:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_DOWN:
                    self.option += 1
                if e.key == pygame.K_UP:
                    self.option -= 1
                if e.key == pygame.K_RETURN:
                    self.options[self.option][1]()
        if self.option > len(self.options)-1:
            self.option = 0
        if self.option < 0:
            self.option = len(self.options)-1

# Position Menu
    def set_pos(self, x, y):
        self.x = x
        self.y = y

# Font Style
    def set_font(self, font):
        self.font = font

# Highlight Color
    def set_highlight_color(self, color):
        self.hcolor = color

# Font Color
    def set_normal_color(self, color):
        self.color = color

# Font position
    def center_at(self, x, y):
        self.x = x-(self.width/2)
        self.y = y-(self.height/2)
