import pygame
import os
from pygame.locals import *
import time
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("PyStocks")  # Window title
icon = pygame.image.load("data/sprites/money.png")  # Icon next to window title
pygame.display.set_icon(icon)
background = pygame.Surface(screen.get_size())
font = pygame.font.SysFont("arial", 16)
os.environ['SDL_VIDEO_CENTERED'] = "1"
stockPrice = [["AMC", 15], ["GME", 182], ["BBIG", 3], ["MSFT", 270]]  # List of stocks

userData = {"Suit": '', "Type of trader": '', "Name": '', "Stock Chosen": ''}  # Userdata

# Constants for class InputBox
COLOR_INACTIVE = pygame.Color('yellow')
COLOR_ACTIVE = pygame.Color('black')
FONT = pygame.font.SysFont("arial", 25)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (53, 198, 188)
PURPLE = (230, 0, 255)
YELLOW = (255, 247, 0)
muted = False

# Sprite Groups
exchanges = pygame.sprite.Group(())
player = pygame.sprite.Group(())
score = pygame.sprite.Group(())
bouncer = pygame.sprite.Group(())
objects = pygame.sprite.Group(())
BG = pygame.sprite.Group(())
boss = pygame.sprite.Group(())
tv = pygame.sprite.Group(())


# Used for loading standalone audio
def load_sound(name):
    class NoneSound:
        def play(self): pass

    if not pygame.mixer or not pygame.mixer.get_init():
        return NoneSound()
    fullname = os.path.join('data', name)
    try:
        sound = pygame.mixer.Sound(fullname)
        return sound
    except pygame.error as message:
        print('Cannot load sound:', fullname)
        raise (SystemExit, message)


# Used for loading standalone images
def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
        # image.set_colorkey(image.get_at((0, 0)))
    except pygame.error as message:
        print('Cannot load image:', fullname)
        raise (SystemExit, message)

    image = image.convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()


sound1 = pygame.mixer.Sound('data/sounds/coins.wav')
sound2 = pygame.mixer.Sound('data/sounds/celebrate.wav')
sound3 = pygame.mixer.Sound('data/sounds/trumpets.wav')
sound4 = pygame.mixer.Sound('data/sounds/winLevel.wav')
sound5 = pygame.mixer.Sound('data/sounds/restart.wav')
sound6 = pygame.mixer.Sound('data/sounds/piano.wav')
if not muted:
    # pygame.mixer.music.load("data/music/stockmus.mp3")
    pygame.mixer.music.load("data/music/toward.mp3")
    # music = pygame.mixer.music
    # music = pygame.mixer.music.load("data/music/stockmus.mp3") #lost.ogg
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.Sound.set_volume(sound1, 0.5)
    pygame.mixer.Sound.set_volume(sound2, 0.5)
    pygame.mixer.Sound.set_volume(sound3, 0.5)
    pygame.mixer.Sound.set_volume(sound4, 0.5)
    pygame.mixer.Sound.set_volume(sound5, 0.5)
    pygame.mixer.music.play(-1)


elif muted:
    pygame.mixer.music.set_volume(0.0)
    pygame.mixer.Sound.set_volume(sound1, 0.0)
    pygame.mixer.Sound.set_volume(sound2, 0.0)

# class New_Game_Button(Button):
#     def __init__(self, parent, position=(300, 300)):
#         Button.__init__(self, parent, 'Continue',
#                         pygame.image.load('data/sprites/new_game_btn.png').convert(), position)
#
#     def on_click(self):
#         print("clicked")


# Sprite for userData
class Score(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.scoreFont = pygame.font.Font("data/fonts/ls.ttf", 25)
        self.font = pygame.font.Font("data/fonts/arial.ttf", 18)
        self.text = ("   [Type of Trader]-   " + userData["Type of trader"] +
                     "   [Suit Color]-   " + userData["Suit"] +
                     "   [Name]-   " + userData["Name"])
        self.image = self.font.render(self.text, True, (0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.center = (400, 8)


# user() and user2() game loop background animation sprite
class Arena(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load("data/menu/3.png"))
        self.sprites.append(pygame.image.load("data/menu/4.png"))
        self.sprites.append(pygame.image.load("data/menu/5.png"))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()

        self.image.set_colorkey(self.image.get_at((0, 0)))

    def update(self):
        self.current_sprite += 0.09

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[int(self.current_sprite)]


# saveScore() game loop background animation sprite
class nameBg(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load("data/menu/saveScore/3.png"))
        self.sprites.append(pygame.image.load("data/menu/saveScore/4.png"))
        self.sprites.append(pygame.image.load("data/menu/saveScore/5.png"))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()

        self.image.set_colorkey(self.image.get_at((0, 0)))

    def update(self):
        self.current_sprite += 0.09
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[int(self.current_sprite)]


# missionMenu() game loop background animation sprite
class howToPlay(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load("data/menu/howTo/9.png"))
        self.sprites.append(pygame.image.load("data/menu/howTo/10.png"))
        self.sprites.append(pygame.image.load("data/menu/howTo/11.png"))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()

        self.image.set_colorkey(self.image.get_at((0, 0)))

    def update(self):
        self.current_sprite += 0.09
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[int(self.current_sprite)]


# game() game loop background animation sprite
class backGround(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # self.image, self.rect = load_image("menu/out.png", -1)
        self.sprites = []
        self.sprites.append(pygame.image.load("data/menu/outside/17.png"))
        self.sprites.append(pygame.image.load("data/menu/outside/18.png"))
        self.sprites.append(pygame.image.load("data/menu/outside/19.png"))
        self.sprites.append(pygame.image.load("data/menu/outside/20.png"))
        self.sprites.append(pygame.image.load("data/menu/outside/21.png"))
        self.sprites.append(pygame.image.load("data/menu/outside/22.png"))
        self.sprites.append(pygame.image.load("data/menu/outside/23.png"))
        self.sprites.append(pygame.image.load("data/menu/outside/24.png"))
        self.sprites.append(pygame.image.load("data/menu/outside/25.png"))
        self.sprites.append(pygame.image.load("data/menu/outside/26.png"))
        self.sprites.append(pygame.image.load("data/menu/outside/27.png"))
        self.sprites.append(pygame.image.load("data/menu/outside/28.png"))
        self.sprites.append(pygame.image.load("data/menu/outside/29.png"))
        self.sprites.append(pygame.image.load("data/menu/outside/30.png"))
        self.sprites.append(pygame.image.load("data/menu/outside/31.png"))
        self.sprites.append(pygame.image.load("data/menu/outside/32.png"))
        self.sprites.append(pygame.image.load("data/menu/outside/33.png"))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()

        self.image.set_colorkey(self.image.get_at((0, 0)))

    def update(self):
        self.current_sprite += 0.3
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[int(self.current_sprite)]


# game2() game loop background animation sprite
class bossBG(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load("data/menu/outside2/1.png"))
        self.sprites.append(pygame.image.load("data/menu/outside2/2.png"))
        self.sprites.append(pygame.image.load("data/menu/outside2/3.png"))
        self.sprites.append(pygame.image.load("data/menu/outside2/4.png"))
        self.sprites.append(pygame.image.load("data/menu/outside2/5.png"))
        self.sprites.append(pygame.image.load("data/menu/outside2/6.png"))
        self.sprites.append(pygame.image.load("data/menu/outside2/7.png"))
        self.sprites.append(pygame.image.load("data/menu/outside2/8.png"))
        self.sprites.append(pygame.image.load("data/menu/outside2/9.png"))
        self.sprites.append(pygame.image.load("data/menu/outside2/11.png"))
        self.sprites.append(pygame.image.load("data/menu/outside2/12.png"))
        self.sprites.append(pygame.image.load("data/menu/outside2/13.png"))
        self.sprites.append(pygame.image.load("data/menu/outside2/14.png"))
        self.sprites.append(pygame.image.load("data/menu/outside2/15.png"))
        self.sprites.append(pygame.image.load("data/menu/outside2/16.png"))
        self.sprites.append(pygame.image.load("data/menu/outside2/17.png"))
        self.sprites.append(pygame.image.load("data/menu/outside2/18.png"))
        self.sprites.append(pygame.image.load("data/menu/outside2/19.png"))
        self.sprites.append(pygame.image.load("data/menu/outside2/20.png"))
        self.sprites.append(pygame.image.load("data/menu/outside2/21.png"))
        self.sprites.append(pygame.image.load("data/menu/outside2/22.png"))
        self.sprites.append(pygame.image.load("data/menu/outside2/23.png"))
        self.sprites.append(pygame.image.load("data/menu/outside2/24.png"))
        self.sprites.append(pygame.image.load("data/menu/outside2/25.png"))
        self.sprites.append(pygame.image.load("data/menu/outside2/26.png"))
        self.sprites.append(pygame.image.load("data/menu/outside2/27.png"))
        self.sprites.append(pygame.image.load("data/menu/outside2/28.png"))
        self.sprites.append(pygame.image.load("data/menu/outside2/29.png"))
        self.sprites.append(pygame.image.load("data/menu/outside2/30.png"))
        self.sprites.append(pygame.image.load("data/menu/outside2/31.png"))
        self.sprites.append(pygame.image.load("data/menu/outside2/32.png"))
        self.sprites.append(pygame.image.load("data/menu/outside2/33.png"))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()

        self.image.set_colorkey(self.image.get_at((0, 0)))

    def update(self):
        self.current_sprite += .7
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[int(self.current_sprite)]


# game3() game loop background animation sprite
class tradeBG(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load("data/menu/inside/1.png"))
        self.sprites.append(pygame.image.load("data/menu/inside/2.png"))
        self.sprites.append(pygame.image.load("data/menu/inside/3.png"))
        self.sprites.append(pygame.image.load("data/menu/inside/4.png"))
        self.sprites.append(pygame.image.load("data/menu/inside/5.png"))
        self.sprites.append(pygame.image.load("data/menu/inside/6.png"))
        self.sprites.append(pygame.image.load("data/menu/inside/7.png"))
        self.sprites.append(pygame.image.load("data/menu/inside/8.png"))
        self.sprites.append(pygame.image.load("data/menu/inside/9.png"))
        self.sprites.append(pygame.image.load("data/menu/inside/11.png"))
        self.sprites.append(pygame.image.load("data/menu/inside/12.png"))
        self.sprites.append(pygame.image.load("data/menu/inside/13.png"))
        self.sprites.append(pygame.image.load("data/menu/inside/14.png"))
        self.sprites.append(pygame.image.load("data/menu/inside/15.png"))
        self.sprites.append(pygame.image.load("data/menu/inside/16.png"))
        self.sprites.append(pygame.image.load("data/menu/inside/17.png"))
        self.sprites.append(pygame.image.load("data/menu/inside/18.png"))
        self.sprites.append(pygame.image.load("data/menu/inside/19.png"))
        self.sprites.append(pygame.image.load("data/menu/inside/20.png"))
        self.sprites.append(pygame.image.load("data/menu/inside/21.png"))
        self.sprites.append(pygame.image.load("data/menu/inside/22.png"))
        self.sprites.append(pygame.image.load("data/menu/inside/23.png"))
        self.sprites.append(pygame.image.load("data/menu/inside/24.png"))
        self.sprites.append(pygame.image.load("data/menu/inside/25.png"))
        self.sprites.append(pygame.image.load("data/menu/inside/26.png"))
        self.sprites.append(pygame.image.load("data/menu/inside/27.png"))
        self.sprites.append(pygame.image.load("data/menu/inside/28.png"))
        self.sprites.append(pygame.image.load("data/menu/inside/29.png"))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()

        self.image.set_colorkey(self.image.get_at((0, 0)))

    def update(self):
        self.current_sprite += .1
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[int(self.current_sprite)]


# standalone sprite used for background in game loop winGameMSFT(), winGameBBIG(), winGameAMC(), and winGameGME()
class wonG(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load("data/menu/winGame/2.png"))
        self.sprites.append(pygame.image.load("data/menu/winGame/3.png"))
        self.sprites.append(pygame.image.load("data/menu/winGame/4.png"))
        self.sprites.append(pygame.image.load("data/menu/winGame/5.png"))
        self.sprites.append(pygame.image.load("data/menu/winGame/6.png"))
        self.sprites.append(pygame.image.load("data/menu/winGame/7.png"))
        self.sprites.append(pygame.image.load("data/menu/winGame/8.png"))
        self.sprites.append(pygame.image.load("data/menu/winGame/9.png"))
        self.sprites.append(pygame.image.load("data/menu/winGame/11.png"))
        self.sprites.append(pygame.image.load("data/menu/winGame/12.png"))
        self.sprites.append(pygame.image.load("data/menu/winGame/13.png"))
        self.sprites.append(pygame.image.load("data/menu/winGame/14.png"))
        self.sprites.append(pygame.image.load("data/menu/winGame/15.png"))
        self.sprites.append(pygame.image.load("data/menu/winGame/16.png"))
        self.sprites.append(pygame.image.load("data/menu/winGame/17.png"))
        self.sprites.append(pygame.image.load("data/menu/winGame/18.png"))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()

        self.image.set_colorkey(self.image.get_at((0, 0)))

    def update(self):
        if self.current_sprite < 15:
            self.current_sprite += .3
        elif self.current_sprite > 15:
            self.current_sprite = 15
        elif self.current_sprite == 15:
            self.current_sprite = 15
        self.image = self.sprites[int(self.current_sprite)]


# Sprite added to boss sprite group, used in game loop game5()
class BossKenG(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("sprites/kg3.png")
        self.rect = self.image.get_rect()
        self.image.set_colorkey(self.image.get_at((0, 1)))
        self.rect.x = x
        self.rect.y = y
        self.is_collidable = False


# animation sprite of sprite group tv, used in game loop game3()
class Tv(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load("data/sprites/tv3/11.png"))
        self.sprites.append(pygame.image.load("data/sprites/tv3/12.png"))
        self.sprites.append(pygame.image.load("data/sprites/tv3/13.png"))
        self.sprites.append(pygame.image.load("data/sprites/tv3/14.png"))
        self.sprites.append(pygame.image.load("data/sprites/tv3/15.png"))
        self.sprites.append(pygame.image.load("data/sprites/tv3/16.png"))
        self.sprites.append(pygame.image.load("data/sprites/tv3/17.png"))
        self.sprites.append(pygame.image.load("data/sprites/tv3/18.png"))
        self.sprites.append(pygame.image.load("data/sprites/tv3/19.png"))
        self.sprites.append(pygame.image.load("data/sprites/tv3/20.png"))
        self.sprites.append(pygame.image.load("data/sprites/tv3/21.png"))
        self.sprites.append(pygame.image.load("data/sprites/tv3/22.png"))
        self.sprites.append(pygame.image.load("data/sprites/tv3/23.png"))
        self.sprites.append(pygame.image.load("data/sprites/tv3/24.png"))
        self.sprites.append(pygame.image.load("data/sprites/tv3/25.png"))
        self.sprites.append(pygame.image.load("data/sprites/tv3/26.png"))
        self.sprites.append(pygame.image.load("data/sprites/tv3/27.png"))
        self.sprites.append(pygame.image.load("data/sprites/tv3/28.png"))
        self.sprites.append(pygame.image.load("data/sprites/tv3/29.png"))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.is_collidable = False

    def update(self):
        self.current_sprite += 0.7

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[int(self.current_sprite)]


# animation sprite of sprite group tv, used in game loop game3()
class Tv2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # self.image, self.rect = load_image("sprites/Trade.png")
        # self.rect = self.image.get_rect()
        # self.image.set_colorkey(self.image.get_at((0, 0)))

        self.sprites = []
        self.sprites.append(pygame.image.load("data/sprites/tv/12.png"))
        self.sprites.append(pygame.image.load("data/sprites/tv/13.png"))
        self.sprites.append(pygame.image.load("data/sprites/tv/14.png"))
        self.sprites.append(pygame.image.load("data/sprites/tv/15.png"))
        self.sprites.append(pygame.image.load("data/sprites/tv/16.png"))
        self.sprites.append(pygame.image.load("data/sprites/tv/17.png"))
        self.sprites.append(pygame.image.load("data/sprites/tv/18.png"))
        self.sprites.append(pygame.image.load("data/sprites/tv/19.png"))
        self.sprites.append(pygame.image.load("data/sprites/tv/20.png"))
        self.sprites.append(pygame.image.load("data/sprites/tv/21.png"))
        self.sprites.append(pygame.image.load("data/sprites/tv/22.png"))
        self.sprites.append(pygame.image.load("data/sprites/tv/23.png"))
        self.sprites.append(pygame.image.load("data/sprites/tv/24.png"))
        self.sprites.append(pygame.image.load("data/sprites/tv/25.png"))
        self.sprites.append(pygame.image.load("data/sprites/tv/26.png"))
        self.sprites.append(pygame.image.load("data/sprites/tv/27.png"))
        self.sprites.append(pygame.image.load("data/sprites/tv/28.png"))
        self.sprites.append(pygame.image.load("data/sprites/tv/29.png"))
        self.sprites.append(pygame.image.load("data/sprites/tv/30.png"))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.is_collidable = False

    def update(self):
        self.current_sprite += 0.1

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[int(self.current_sprite)]


# animation sprite of sprite group tv, used in game loop game3()
class Tv3(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load("data/sprites/tv2/12.png"))
        self.sprites.append(pygame.image.load("data/sprites/tv2/13.png"))
        self.sprites.append(pygame.image.load("data/sprites/tv2/14.png"))
        self.sprites.append(pygame.image.load("data/sprites/tv2/15.png"))
        self.sprites.append(pygame.image.load("data/sprites/tv2/16.png"))
        self.sprites.append(pygame.image.load("data/sprites/tv2/17.png"))
        self.sprites.append(pygame.image.load("data/sprites/tv2/18.png"))
        self.sprites.append(pygame.image.load("data/sprites/tv2/19.png"))
        self.sprites.append(pygame.image.load("data/sprites/tv2/20.png"))
        self.sprites.append(pygame.image.load("data/sprites/tv2/21.png"))
        self.sprites.append(pygame.image.load("data/sprites/tv2/22.png"))
        self.sprites.append(pygame.image.load("data/sprites/tv2/23.png"))
        self.sprites.append(pygame.image.load("data/sprites/tv2/24.png"))
        self.sprites.append(pygame.image.load("data/sprites/tv2/25.png"))
        self.sprites.append(pygame.image.load("data/sprites/tv2/26.png"))
        self.sprites.append(pygame.image.load("data/sprites/tv2/27.png"))
        self.sprites.append(pygame.image.load("data/sprites/tv2/28.png"))
        self.sprites.append(pygame.image.load("data/sprites/tv2/29.png"))
        self.sprites.append(pygame.image.load("data/sprites/tv2/30.png"))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.is_collidable = False

    def update(self):
        self.current_sprite += 0.3

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[int(self.current_sprite)]


# standalone sprite used for the stock exchange in game loop game()
class Exchange(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("sprites/exchange2.png")
        self.rect = self.image.get_rect()
        # self.image.set_colorkey(self.image.get_at((0, 0)))
        self.rect.x = x
        self.rect.y = y
        self.is_collidable = False


# standalone sprite used for computer window in game loop game4()
class window(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("menu/window.png", -1)


# standalone sprite used for background in game loop highScore()
class shine(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("menu/shine.png", -1)


# standalone sprite used for background in game loop game5()
class desktop(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("menu/desktop.png", -1)


# standalone sprite used for background in game loop optionMSFT()
class MSFTbg(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("menu/MSFT.png", -1)


# standalone sprite used for background in game loop optionBBIG()
class BBIGbg(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("menu/BBIG.png", -1)


# standalone sprite used for background in game loop optionAMC()
class AMCbg(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("menu/AMC.png", -1)


# standalone sprite used for background in game loop optionGME()
class GMEbg(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("menu/GME.png", -1)


# standalone sprite used for background in game loop endGameMSFT(), endGameBBIG(), endGameAMC(), and endGameGME()
class endG(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("menu/gameover.png", -1)


# standalone sprite used for background in game loop optionCredits()
class stonksBg(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("menu/stonks.png", -1)


class TextScroll:

    def __init__(self, area, font2, fg_color, bk_color, text, ms_per_line=800):
        """object to display lines of text scrolled in with a delay between each line
        in font and fg_color with background o fk_color with in the area rect"""
        super().__init__()
        self.rect = area.copy()
        self.fg_color = fg_color
        self.bk_color = bk_color
        self.size = area.size
        self.surface = pygame.Surface(self.size, flags=pygame.SRCALPHA)
        self.surface.fill(bk_color)
        self.font = font2
        self.lines = text.split('\n')
        self.ms_per_line = ms_per_line
        self.y = 0
        self.y_delta = self.font.size("M")[1]
        self.next_time = None
        self.dirty = False

    def _update_line(self, line):  # render next line if it's time

        if self.y + self.y_delta > self.size[1]:  # line does not fit in remaining space
            self.surface.blit(self.surface, (0, -self.y_delta))  # scroll up
            self.y += -self.y_delta  # backup a line
            pygame.draw.rect(self.surface, self.bk_color,
                             (0, self.y, self.size[0], self.size[1] - self.y))

        text = self.font.render(line, True, self.fg_color)
        # pygame.draw.rect(text, GREY, text.get_rect(), 1)  # for demo show render area
        self.surface.blit(text, (0, self.y))

        self.y += self.y_delta

    # call update from pygame main loop
    def update(self):
        time_now = time.time()
        if (self.next_time is None or self.next_time < time_now) and self.lines:
            self.next_time = time_now + self.ms_per_line / 1000
            line = self.lines.pop(0)
            self._update_line(line)
            self.dirty = True
            self.update()  # do it again to catch more than one event per tick

    # call draw from pygam main loop after update
    def draw(self, screen2):
        if self.dirty:
            screen2.blit(self.surface, self.rect)
            self.dirty = False


class InputBox(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, text='', text_size=0.5):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text

        self.text_size = text_size
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
        self.pos = (w * h)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    userData['Name'] = self.text
                    return userData['Name']  # User entered string
                    # return userInput
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        # width = max(200, self.txt_surface.get_width() + 10)

        width = 200
        if self.txt_surface.get_width() > width - 18:
            self.text = self.text[:-1]
            self.rect.w = width
        self.rect.w = width

    def draw(self, screen2):
        # Blit the text.
        screen2.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        # Blit the rect.
        pygame.draw.rect(screen2, self.color, self.rect, 2)
