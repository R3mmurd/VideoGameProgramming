import pygame

from gale.input_handler import InputHandler, InputData
from gale.state_machine import BaseState
from gale.text import render_text

import settings


class GameOverState(BaseState):
    def enter(self, player) -> None:
        self.player = player
        InputHandler.register_listener(self)
        InputHandler.unregister_listener(self.player.state_machine.current)
    
    def exit(self) -> None:
        InputHandler.unregister_listener(self)

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == 'enter' and input_data.pressed:
            self.state_machine.change('play')

    def render(self, surface: pygame.Surface) -> None:
        surface.fill((25, 130, 196))

        render_text(
            surface, 'Game Over!', settings.FONTS['medium'],
            settings.VIRTUAL_WIDTH // 2, 20,
            (255, 255, 255), center=True, shadowed=True
        )

        y = 50

        for color, amount in self.player.coins_counter.items():
            surface.blit(
                settings.TEXTURES['tiles'],
                (settings.VIRTUAL_WIDTH // 2 - 32, y),
                settings.FRAMES['tiles'][color]
            )
            render_text(
                surface, 'x', settings.FONTS['small'],
                settings.VIRTUAL_WIDTH // 2, y + 3, (255, 255, 255),
                shadowed=True
            )
            render_text(
                surface, f'{amount}', settings.FONTS['small'],
                settings.VIRTUAL_WIDTH // 2 + 16, y + 3, (255, 255, 255),
                shadowed=True
            )
            y += 20

        render_text(
            surface, f'Score: {self.player.score}', settings.FONTS['small'],
            settings.VIRTUAL_WIDTH // 2, y+10, (255, 255, 255),
            shadowed=True, center=True
        )

        render_text(
            surface, 'Press Enter to play again', settings.FONTS['small'],
            settings.VIRTUAL_WIDTH // 2, settings.VIRTUAL_HEIGHT - 20,
            (255, 255, 255), center=True, shadowed=True
        )
