"""
ISPPJ1 2023
Study Case: Super Martian (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the definitions of the tiles.
"""
from typing import Dict, Any

TILES: Dict[int, Dict[str, Any]] = {
    # Ground
    0: {
        'solidness': dict(top=True, right=False, bottom=False, left=False)
    },
    1: {
        'solidness': dict(top=True, right=False, bottom=False, left=False)
    },
    2: {
        'solidness': dict(top=True, right=False, bottom=False, left=False)
    },
    3: {
        'solidness': dict(top=True, right=False, bottom=False, left=False)
    },
    4: {
        'solidness': dict(top=True, right=False, bottom=False, left=False)
    },
    5: {
        'solidness': dict(top=True, right=False, bottom=False, left=False)
    },
    10: {
        'solidness': dict(top=True, right=False, bottom=False, left=False)
    },

    # Blocks
    6: {
        'solidness': dict(top=True, right=True, bottom=True, left=True)
    },
    17: {
        'solidness': dict(top=True, right=True, bottom=True, left=True)
    },
    41: {
        'solidness': dict(top=True, right=True, bottom=True, left=True)
    }
}
