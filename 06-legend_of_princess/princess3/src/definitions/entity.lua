--[[
    ISPPJ1 2024
    Study Case: The Legend of the Princess (ARPG)

    Author: Colton Ogden
    cogden@cs50.harvard.edu

    Modified by Alejandro Mujica (alejandro.j.mujic4@gmail.com) for teaching purpose.

    This file contains the definition for entities.
]]
ENTITY_DEFS = {
    ['player'] = {
        walkSpeed = 60,
        animations = {
            ['walk-left'] = {
                frames = {13, 14, 15, 16},
                interval = 0.155,
                texture = 'character-walk'
            },
            ['walk-right'] = {
                frames = {5, 6, 7, 8},
                interval = 0.15,
                texture = 'character-walk'
            },
            ['walk-down'] = {
                frames = {1, 2, 3, 4},
                interval = 0.15,
                texture = 'character-walk'
            },
            ['walk-up'] = {
                frames = {9, 10, 11, 12},
                interval = 0.15,
                texture = 'character-walk'
            },
            ['idle-left'] = {
                frames = {13},
                texture = 'character-walk'
            },
            ['idle-right'] = {
                frames = {5},
                texture = 'character-walk'
            },
            ['idle-down'] = {
                frames = {1},
                texture = 'character-walk'
            },
            ['idle-up'] = {
                frames = {9},
                texture = 'character-walk'
            },
            ['sword-left'] = {
                frames = {13, 14, 15, 16},
                interval = 0.05,
                looping = false,
                texture = 'character-swing-sword'
            },
            ['sword-right'] = {
                frames = {9, 10, 11, 12},
                interval = 0.05,
                looping = false,
                texture = 'character-swing-sword'
            },
            ['sword-down'] = {
                frames = {1, 2, 3, 4},
                interval = 0.05,
                looping = false,
                texture = 'character-swing-sword'
            },
            ['sword-up'] = {
                frames = {5, 6, 7, 8},
                interval = 0.05,
                looping = false,
                texture = 'character-swing-sword'
            }
        }
    }
}