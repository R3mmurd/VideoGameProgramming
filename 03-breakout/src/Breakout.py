"""
ISPPV1 2023
Study Case: Breakout

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class Breakout as a specialization of gale.Game
"""

import pygame

from gale.game import Game
from gale.state import StateMachine
from gale.input_handler import InputData

import settings

from src import states


class Breakout(Game):
    def init(self) -> None:
        self.state_machine = StateMachine(
            {
                "start": states.StartState,
                "high_score": states.HighScoreState,
                "enter_high_score": states.EnterHighScoreState,
                "game_over": states.GameOverState,
                "paddle_select": states.PaddleSelectState,
                "serve": states.ServeState,
                "play": states.PlayState,
                "victory": states.VictoryState,
                "pause": states.PauseState,
            }
        )
        self.state_machine.change("start")
        pygame.mixer_music.load(settings.BASE_DIR / "assets" / "sounds" / "music.ogg")
        pygame.mixer_music.play(loops=-1)

    def update(self, dt: float) -> None:
        self.state_machine.update(dt)

    def render(self, surface: pygame.Surface) -> None:
        surface.blit(settings.TEXTURES["background"], (0, 0))
        self.state_machine.render(surface)

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == "quit" and input_data.pressed:
            self.quit()
        else:
            self.state_machine.on_input(input_id, input_data)
