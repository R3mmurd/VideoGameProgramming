"""
ISPPJ1 2023
Input handler by commands.

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class InputHandler that retrieves the events
and matches them with their associated actions.
"""
import sys
import pygame

import settings

from Action import Action


class InputHandler:
    @staticmethod
    def handle_input() -> Action:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                keyboard_binding = settings.input_binding.get("keyboard")
                if keyboard_binding is not None:
                    action_class = keyboard_binding.get(event.key)
                    if action_class is not None:
                        return action_class()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_binding = settings.input_binding.get("mouse")
                if mouse_binding is not None:
                    action_class = mouse_binding.get(event.button)
                    if action_class is not None:
                        return action_class()
        return None
