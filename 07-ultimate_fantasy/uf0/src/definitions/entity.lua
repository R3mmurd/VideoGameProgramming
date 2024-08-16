--[[
    ISPPV1 2024
    Study Case: Ultimate Fantasy (RPG)

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains the definition for entities.
]]
DEFAULT_CHARACTER_FRAME = 8
ENTITY_WIDTH = 16
ENTITY_HEIGHT = 18
NUM_CHARACTERS = 4

ENTITY_DEFS = {
    characters = {
        [1] = {
            type = 'warrior',
            female = {
                name  = 'Celes',
                texture = 'warrior-female',
            },
            male = {
                name  = 'Squall',
                texture = 'warrior-male',
            }
        },
        [2] = {
            type = 'ranger', 
            female = {
                name = 'Terra',
                texture = 'ranger-female',
            },
            male = {
                name = 'Cloud',
                texture = 'ranger-male',
            }
        },
        [3] = {
            type = 'healer',
            female = {
                name = 'Tifa',
                texture = 'healer-female',
            },
            male = {
                name = 'Kimahri',
                texture = 'healer-male',
            }
        },
        [4] = {
            type = 'mage',
            female = {
                name = 'Rinoa',
                texture = 'mage-female',
            },
            male = {
                name = 'Sephiroth',
                texture = 'mage-male',
            }
        }
    }
}