import pygame

from Actor import Actor
from InputHandler import InputHandler

if __name__ == '__main__':
    pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Bird')
    actor = Actor("Player")
    while True:
        action = InputHandler.handle_input()
        if action is not None:
            action.execute(actor)
