from dataclasses import dataclass

from pygame.color import THECOLORS

# system settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
RESOLUTION = (800, 600)
FPS = 6000


@dataclass()
class Colors:
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    MAGENTA = (255, 0, 255)
    CYAN = (0, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (100, 100, 100)


# ultra colsil'
all_colors = list({color if isinstance(color, tuple) else (0, 0, 0) for color in Colors.__dict__.values()})
# background color
BG_COLOR = THECOLORS['white']

# acceleration of gravity
GRAVITY = 1000
# if object speed <= CRITICAL_SPEED object's speed set to zero
CRITICAL_SPEED = 5
# if distance between objects <= CRITICAL_DISTANCE object move to point with distance = zero
CRITICAL_DISTANCE = min(SCREEN_WIDTH // 100, SCREEN_HEIGHT // 100)
