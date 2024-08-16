"""
ISPPV1 2024
Study Case: Super Martian (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the AnimatedMixin.
"""

from typing import Dict, Any

from gale.animation import Animation


class AnimatedMixin:
    def generate_animations(self, animation_defs: Dict[str, Dict[str, Any]]) -> None:
        for animation_id, values in animation_defs.items():
            animation = Animation(
                values["frames"],
                values.get("interval", 0),  # Given interval or zero
                loops=values.get("loops"),  # Given loops or None
            )
            self.animations[animation_id] = animation

    def change_animation(self, animation_id: str) -> None:
        new_animation = self.animations[animation_id]
        if new_animation != self.current_animation:
            self.current_animation = new_animation
            self.current_animation.reset()
            self.frame_index = self.current_animation.get_current_frame()

    def update(self, dt: float) -> None:
        self.current_animation.update(dt)
        self.frame_index = self.current_animation.get_current_frame()
