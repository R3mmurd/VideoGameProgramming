--[[
    ISPPV1 2023
    Study Case: The Legend of the Princess (ARPG)

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains the game settings that include dependencies, constants of values to set
    up the game, sounds, textures, frames, and fonts.
]]
Class = require 'lib/class'
push = require 'lib/push'

require 'src/Animation'
require 'src/Entity'
require 'src/GameObject'
require 'src/Hitbox'
require 'src/Player'
require 'src/StateMachine'

require 'src/definitions/entity'
require 'src/definitions/game_objects'

require 'src/states/BaseState'

require 'src/states/entity/EntityIdleState'
require 'src/states/entity/EntityWalkState'

require 'src/states/entity/player/PlayerIdleState'
require 'src/states/entity/player/PlayerSwingSwordState'
require 'src/states/entity/player/PlayerWalkState'

require 'src/states/game/PlayState'
require 'src/states/game/StartState'

require 'src/utilities/quads'

require 'src/world/Doorway'
require 'src/world/Dungeon'
require 'src/world/Room'

VIRTUAL_WIDTH = 384
VIRTUAL_HEIGHT = 216

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

TILE_SIZE = 16

--
-- map constants
--
MAP_WIDTH = VIRTUAL_WIDTH / TILE_SIZE - 2
MAP_HEIGHT = math.floor(VIRTUAL_HEIGHT / TILE_SIZE) - 2

MAP_RENDER_OFFSET_X = (VIRTUAL_WIDTH - (MAP_WIDTH * TILE_SIZE)) / 2
MAP_RENDER_OFFSET_Y = (VIRTUAL_HEIGHT - (MAP_HEIGHT * TILE_SIZE)) / 2

--
-- tile IDs
--
TILE_TOP_LEFT_CORNER = 4
TILE_TOP_RIGHT_CORNER = 5
TILE_BOTTOM_LEFT_CORNER = 23
TILE_BOTTOM_RIGHT_CORNER = 24

TILE_EMPTY = 19

TILE_FLOORS = {
    7, 8, 9, 10, 11, 12, 13,
    26, 27, 28, 29, 30, 31, 32,
    45, 46, 47, 48, 49, 50, 51,
    64, 65, 66, 67, 68, 69, 70,
    88, 89, 107, 108
}

TILE_TOP_WALLS = {58, 59, 60}
TILE_BOTTOM_WALLS = {79, 80, 81}
TILE_LEFT_WALLS = {77, 96, 115}
TILE_RIGHT_WALLS = {78, 97, 116}

TEXTURES = {
    ['tiles'] = love.graphics.newImage('graphics/tilesheet.png'),
    ['background'] = love.graphics.newImage('graphics/background.png'),
    ['character-walk'] = love.graphics.newImage('graphics/character_walk.png'),
    ['character-swing-sword'] = love.graphics.newImage('graphics/character_swing_sword.png'),
    ['hearts'] = love.graphics.newImage('graphics/hearts.png'),
    ['switches'] = love.graphics.newImage('graphics/switches.png'),
}

FRAMES = {
    ['tiles'] = generateQuads(TEXTURES['tiles'], 16, 16),
    ['character-walk'] = generateQuads(TEXTURES['character-walk'], 16, 32),
    ['character-swing-sword'] = generateQuads(TEXTURES['character-swing-sword'], 32, 32),
    ['hearts'] = generateQuads(TEXTURES['hearts'], 16, 16),
    ['switches'] = generateQuads(TEXTURES['switches'], 16, 18)
}

FONTS = {
    ['princess'] = love.graphics.newFont('fonts/princess.otf', 32),
    ['princess-small'] = love.graphics.newFont('fonts/princess.otf', 24)
}

SOUNDS = {
    ['start-music'] = love.audio.newSource('sounds/start_music.mp3', 'static'),
    ['dungeon-music'] = love.audio.newSource('sounds/dungeon_music.mp3', 'static'),
    ['sword'] = love.audio.newSource('sounds/sword.wav', 'static'),
    ['door'] = love.audio.newSource('sounds/door.wav', 'static')
}
