TITLE = "LavaRun"
WIDTH = 480
HEIGHT = 600
FPS = 60
FONT_NAME = 'arial'
HS_FILE = "highscore.txt"

# Player properties
PLAYER_ACC = 0.7
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.8
PLAYER_JUMP = 20

# Starting platforms
PLATFORM_LIST = [(WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20),
                 (125, HEIGHT - 350, 100, 20),
                 (350, 200, 100, 20),
                 (175, 100, 50, 20)]

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHTBLUE = (0, 155, 155)
BGCOLOR = BLACK

OBJECT_HEIGHT = 20

LAVA_HARD = 150
LAVA_MEDIUM_HIGH = 120
LAVA_MEDIUM_LOW = 90
LAVA_EASY = 60

PL_LVL0 = (30,80,130,150)
PL_LVL1 = (150,30,130,80)
PL_LVL2 = (150,130, 80,30)