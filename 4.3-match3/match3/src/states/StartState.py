"""
ISPPV1 2023
Study Case: Match-3

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class StartState.
"""
import random

import pygame

from gale.input_handler import InputData
from gale.state import BaseState, StateMachine
from gale.text import render_text
from gale.timer import Timer

import settings


class StartState(BaseState):
    # colors we'll use to change the title text
    colors = [
        (217, 87, 99),
        (95, 205, 228),
        (251, 242, 54),
        (118, 66, 138),
        (153, 229, 80),
        (223, 113, 38),
    ]

    # letters of MATCH 3 and their spacing relative to the center
    LETTER_TABLE = {"M": -108, "A": -64, "T": -28, "C": 2, "H": 40, "3": 112}

    # A list of frames just for display.
    frames = []

    def __init__(self, state_machine: StateMachine, game) -> None:
        super().__init__(state_machine)
        self.game = game

    def enter(self) -> None:
        self.current_menu_item = 1

        def shift_colors():
            last = self.colors[5]

            for i in range(5, 0, -1):
                self.colors[i] = self.colors[i - 1]

            self.colors[0] = last

        self.color_timer = Timer.every(0.075, shift_colors)

        self.alpha_transition = 0

        # Generate the full tile list for display
        for _ in range(settings.BOARD_WIDTH * settings.BOARD_HEIGHT):
            color = random.randint(0, settings.NUM_COLORS - 1)
            variety = random.randint(0, settings.NUM_VARIETIES - 1)
            self.frames.append(settings.FRAMES["tiles"][color][variety])

        # A surface that supports alpha for the screen
        self.screen_alpha_surface = pygame.Surface(
            (settings.VIRTUAL_WIDTH, settings.VIRTUAL_HEIGHT), pygame.SRCALPHA
        )

        # A surface that supports alpha for each tile to draw
        self.tile_alpha_surface = pygame.Surface(
            (settings.TILE_SIZE, settings.TILE_SIZE), pygame.SRCALPHA
        )
        pygame.draw.rect(
            self.tile_alpha_surface,
            (0, 0, 0, 255),
            pygame.Rect(0, 0, settings.TILE_SIZE, settings.TILE_SIZE),
            border_radius=7,
        )

        # A surface that supports alpha for the title and the menu
        self.text_alpha_surface = pygame.Surface((300, 58), pygame.SRCALPHA)
        pygame.draw.rect(
            self.text_alpha_surface, (255, 255, 255, 128), pygame.Rect(0, 0, 300, 58)
        )

        # If we have selected an option, we need to deactivate inputs while we
        # animate out.
        self.active = True

    def render(self, surface: pygame.Surface) -> None:
        # Render all the tiles and their shadows
        for i in range(settings.BOARD_HEIGHT):
            for j in range(settings.BOARD_HEIGHT):
                x = j * settings.TILE_SIZE + 128
                y = i * settings.TILE_SIZE + 16

                # Frame position in the list
                f = i * settings.BOARD_HEIGHT + j

                surface.blit(settings.TEXTURES["tiles"], (x + 2, y + 2), self.frames[f])
                surface.blit(self.tile_alpha_surface, (x + 2, y + 2))
                surface.blit(
                    settings.TEXTURES["tiles"],
                    (x, y),
                    self.frames[i * settings.BOARD_HEIGHT + j],
                )

        # keep the background and tiles a little darker than normal
        pygame.draw.rect(
            self.screen_alpha_surface,
            (0, 0, 0, 128),
            pygame.Rect(0, 0, settings.VIRTUAL_WIDTH, settings.VIRTUAL_HEIGHT),
        )
        surface.blit(self.screen_alpha_surface, (0, 0))
        self.__draw_match3_text(surface, -60)
        self.__draw_options(surface, 12)

        # draw our transition rect; is normally fully transparent, unless we're
        # moving to a new state
        pygame.draw.rect(
            self.screen_alpha_surface,
            (255, 255, 255, self.alpha_transition),
            pygame.Rect(0, 0, settings.VIRTUAL_WIDTH, settings.VIRTUAL_HEIGHT),
        )
        surface.blit(self.screen_alpha_surface, (0, 0))

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if not self.active:
            return

        if input_id in ("up", "down") and input_data.pressed:
            self.current_menu_item = 1 if self.current_menu_item == 2 else 2
            settings.SOUNDS["select"].play()
        elif input_id == "enter" and input_data.pressed:
            if self.current_menu_item == 1:
                self.active = False
                Timer.tween(
                    1,
                    [(self, {"alpha_transition": 255})],
                    on_finish=lambda: self.state_machine.change("begin"),
                )
            else:
                self.game.quit()

    def __draw_match3_text(self, surface: pygame.Surface, y: int) -> None:
        # draw semi-transparent rect behind MATCH 3
        surface.blit(
            self.text_alpha_surface,
            (settings.VIRTUAL_WIDTH // 2 - 152, settings.VIRTUAL_HEIGHT // 2 + y - 32),
        )

        # draw MATCH 3 text shadows
        for i, (l, x) in enumerate(self.LETTER_TABLE.items()):
            render_text(
                surface,
                l,
                settings.FONTS["huge"],
                settings.VIRTUAL_WIDTH // 2 + x,
                settings.VIRTUAL_HEIGHT // 2 + y,
                self.colors[i],
                center=True,
                shadowed=True,
            )

    def __draw_options(self, surface: pygame.Surface, y: int) -> None:
        surface.blit(
            self.text_alpha_surface,
            (settings.VIRTUAL_WIDTH // 2 - 152, settings.VIRTUAL_HEIGHT // 2 + y),
        )

        text_color = (
            (99, 155, 255, 255) if self.current_menu_item == 1 else (48, 96, 130, 255)
        )

        render_text(
            surface,
            "Start",
            settings.FONTS["medium"],
            settings.VIRTUAL_WIDTH // 2,
            settings.VIRTUAL_HEIGHT // 2 + y + 15,
            text_color,
            center=True,
            shadowed=True,
        )

        text_color = (
            (99, 155, 255, 255) if self.current_menu_item == 2 else (48, 96, 130, 255)
        )

        render_text(
            surface,
            "Quit Game",
            settings.FONTS["medium"],
            settings.VIRTUAL_WIDTH // 2,
            settings.VIRTUAL_HEIGHT // 2 + y + 45,
            text_color,
            center=True,
            shadowed=True,
        )
