
import pygame

from ActionJump import ActionJump
from ActionShoot import ActionShoot

input_binding = {
    "keyboard": {
        pygame.K_SPACE: ActionJump,
    },
    "mouse": {
        1: ActionShoot,
        3: ActionJump
    }
}
