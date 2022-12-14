import os
from pygame.font import SysFont, init
import pygame
import codecs
from os import path

# Colour
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
GREEN = (0, 255, 0)
PURPLE = (255, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BROWN = (165, 42, 42)
YELLOW = (255,255,0)
ORANGE = (255, 191, 0)

# Button Colours
LIGHT_COLOUR = (170, 170, 170)
DARK_COLOUR = (100, 100, 100)

# Window Sizes
WIDTH, HEIGHT = 1920, 1080
DS_WIDTH, DS_HEIGHT = 720, 405
SF = WIDTH / DS_WIDTH

# FPS
FPS = 120

# debug
debug = True

# files
GAME_FOLDER = path.dirname(__file__)
ASSETS_FOLDER = path.join(GAME_FOLDER, "assets")
BUTTONS_FOLDER = path.join(ASSETS_FOLDER, "buttonImages")
TABLE_FOLDER = path.join(ASSETS_FOLDER, "table")
POCKET_FOLDER = path.join(ASSETS_FOLDER, "pocket")
CUEBALL_FOLDER = path.join(ASSETS_FOLDER, "cueball")
BALL_FOLDER = path.join(ASSETS_FOLDER, "balls")

BUTTONS = {}
TABLE_IMAGE = {}

# Values for balls (number, radius, friction and font)
# Need each colour twice for strips and solids (Excep black)
COLOUR = [YELLOW, BLUE, RED, PURPLE, ORANGE, GREEN, BROWN,
          BLACK, WHITE, YELLOW, BLUE, RED, PURPLE, ORANGE, GREEN, BROWN]
RADIUS = 5
FRICTION = 0
BALL_FONT = ("Agency FB", 10)
balls_potted = []
balls_notpotted = 15


#Values needed for the pool table
RECT_HEIGHT = 600
CUSHIONS = 30
MARGIN = 30

#Cueball
BALL_RADIUS = 5

#Variables for input box
COLOUR_OFF = WHITE
COLOUR_ON = YELLOW

init()
INPUT_FONT = SysFont(None, 32)
#Cushions coords

#Left side
CUSHION1 = (153, 110), (153, 295)
#Top left
CUSHION2 = (167, 101), (350, 101)
#Top Right
CUSHION3 = (369, 101), (552, 101)
#Right side
CUSHION4 = (557, 110), (557, 295)
#Bottom right
CUSHION5 = (369, 299), (552, 299)
#Bottom left
CUSHION6 = (167, 299), (350, 299)

#Backdround box for table friction
BOX_COORDS = (0, 0), (650, 370)

#Slowing balls down
SLOW_BALL = pygame.time.get_ticks() + 1 * 1000

#Red ball coords
RED1 = (483, 207)
RED2 = (492, 193)
RED3 = (501, 217)
RED4 = (501, 197)
RED5 = (511, 183)
RED6 = (511, 202)
RED7 = (511, 212)

#Yellow ball coords
Yellow1 = (474, 202)
Yellow2 = (483, 197)
Yellow3 = (492, 212)
Yellow4 = (502, 207)
Yellow5 = (504, 187)
Yellow6 = (511, 193)
Yellow7 = (511, 222)

#Black ball Coord
Black1 = (492, 202)

#Corner pocket radius, coords
POCKET_RADIUS = 13
pocket_coords = [ 
    (150, 93), #Top left
    (560, 93), #Top right
    (150, 312), #Bottom left
    (560, 312), #Bottom right
    (359, 85), #Top middle
    (359, 321) #Bottom middle
]
CP_TL = (150, 93)
CP_TR = (560, 93)
CP_BL = (150, 312)
CP_BR = (560, 312)
MP_T = (359, 93)
MP_B = (359, 312)