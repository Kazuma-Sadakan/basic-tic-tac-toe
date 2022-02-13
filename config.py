from collections import namedtuple, defaultdict
from enum import Enum

import pygame
#board setting 
CELL_SIZE = 200
LINE_WIDTH = 10
BOARD_SIZE = CELL_SIZE * 3 
PADDING = 30

RED = pygame.Color("Red")
WHITE = pygame.Color("White")
BLACK = pygame.Color("Black")
BACKGROUND_COLOR = (30, 170, 160)
LINE_COLOR = (25, 150, 140)
CROSS_COLOR = (65,65, 65)
CIRCLE_COLOR = (240, 230, 200)

Position = namedtuple("Position", ["x", "y"])

class Letter(Enum):
    CIRCLE = 1
    CROSS = 2