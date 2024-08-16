"""
ISPPV1 2024
Input handler by observers.

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class InputHandler to register and unregister listeners.
It also fetches the events and notifies to all of its listeners about the event occurred.
"""

import sys
from typing import Union, Optional, Tuple, List

import pygame

import settings

from Listener import Listener


class KeyBoardEvent:
    def __init__(
        self, pressed: bool, released: bool, modifier: int, unicode: str
    ) -> None:
        self.pressed: bool = pressed
        self.released: bool = released
        self.modifier: int = modifier
        self.unicode: str = unicode


class MouseClickEvent:
    def __init__(
        self, pressed: bool, released: bool, button: int, position: Tuple[int, int]
    ) -> None:
        self.pressed: bool = pressed
        self.released: bool = released
        self.button: int = button
        self.position: Tuple[int, int] = position


class MouseMotionEvent:
    def __init__(
        self, position: Tuple[int, int], buttons: Tuple[int, int, int]
    ) -> None:
        self.position: Tuple[int, int] = position
        self.buttons: Tuple[int, int, int] = buttons


class MouseWheelEvent:
    def __init__(self, x: int, y: int, flipped: bool) -> None:
        self.x: int = x
        self.y: int = y
        self.flipped: bool = flipped


class InputHandler:

    listeners: List[Listener] = []

    @classmethod
    def register(cls, listener: Listener) -> None:
        cls.listeners.append(listener)

    @classmethod
    def unregister(cls, listener: Listener) -> None:
        cls.listeners = [l for l in cls.listeners if l != listener]

    @classmethod
    def notify(
        cls,
        action: str,
        event: Optional[Union[KeyBoardEvent, MouseClickEvent, MouseMotionEvent]],
    ) -> None:
        for l in cls.listeners:
            l.on_input(action, event)

    @classmethod
    def handle_input(cls) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type in (pygame.KEYDOWN, pygame.KEYUP):
                keyboard_binding = settings.input_binding.get("keyboard")
                if keyboard_binding is not None:
                    action = keyboard_binding.get(event.key)
                    if action is not None:
                        evt = KeyBoardEvent(
                            event.type == pygame.KEYDOWN,
                            event.type == pygame.KEYUP,
                            event.mod,
                            event.unicode,
                        )
                        cls.notify(action, evt)
            elif event.type in (pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP):
                mouse_binding = settings.input_binding.get("mouse")
                if mouse_binding is not None:
                    action = mouse_binding.get(event.button)
                    if action is not None:
                        evt = MouseClickEvent(
                            event.type == pygame.MOUSEBUTTONDOWN,
                            event.type == pygame.MOUSEBUTTONUP,
                            event.button,
                            event.pos,
                        )
                        cls.notify(action, evt)
            elif event.type == pygame.MOUSEMOTION:
                motion_binding = settings.input_binding.get("motion")
                if motion_binding is not None:
                    action = motion_binding.get(event.rel)
                    if action is not None:
                        evt = MouseMotionEvent(event.pos, event.buttons)
                        cls.notify(action, evt)
            elif event.type == pygame.MOUSEWHEEL:
                wheel_binding = settings.input_binding.get("wheel")
                if wheel_binding is not None:
                    action = wheel_binding.get((event.x, event.y))
                    if action is not None:
                        evt = MouseWheelEvent(event.x, event.y, event.flipped)
                        cls.notify(action, evt)
