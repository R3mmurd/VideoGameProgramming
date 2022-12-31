"""
ISPPJ1 2023
Study Case: Breakout

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class Breakout as a specialization of gale.Game
"""
import pygame

from gale.game import Game
from gale.state_machine import StateMachine

from src import states


class Breakout(Game):
    def init(self) -> None:
        self.state_machine = StateMachine({
            'start': states.StartState,
            'high_score': states.HighScoreState,
            'enter_high_score': states.EnterHighScoreState,
            'game_over': states.GameOverState,
            'paddle_select': states.PaddleSelectState,
            'serve': states.ServeState,
            'play': states.PlayState,
            'victory': states.VictoryState
        })
        self.state_machine.change("start")

    def update(self, dt: float) -> None:
        self.state_machine.update(dt)

    def render(self, surface: pygame.Surface) -> None:
        self.state_machine.render(surface)
