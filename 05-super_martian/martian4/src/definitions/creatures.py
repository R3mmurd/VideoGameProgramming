"""
ISPPJ1 2024
Study Case: Super Martian (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the definition for creatueres.
"""

from typing import Dict, Any

from src.states.entities import creatures_states

CREATURES: Dict[int, Dict[str, Any]] = {
    48: {
        "texture_id": "creatures",
        "walk_speed": 10,
        "animation_defs": {"walk": {"frames": [48, 49], "interval": 0.25}},
        "states": {"walk": creatures_states.SnailWalkState},
        "first_state": "walk",
    },
    52: {
        "texture_id": "creatures",
        "walk_speed": 15,
        "animation_defs": {"walk": {"frames": [52, 53], "interval": 0.18}},
        "states": {"walk": creatures_states.SnailWalkState},
        "first_state": "walk",
    },
}
