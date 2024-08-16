--[[
    ISPPV1 2023
    Study Case: Ultimate Fantasy (RPG)

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains the game settings that include dependencies, constants of values to set
    up the game, sounds, textures, frames, and fonts.
]]
VIRTUAL_WIDTH = 384
VIRTUAL_HEIGHT = 224

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

TILE_SIZE = 16

Class = require 'lib/class'
push = require 'lib/push'
Timer = require 'lib/knife.timer'

-- definitions
require 'src/definitions/entity'

-- State Machine, Base State, and State Stack.
require 'src/StateMachine'
require 'src/states/StateStack'
require 'src/states/BaseState'

-- Game States
require 'src/states/game/FadeInState'
require 'src/states/game/FadeOutState'
require 'src/states/game/SelectCharacterState'
require 'src/states/game/StartState'

-- Utilities
require 'src/utilities/quads'

TEXTURES = {
    ['background'] = love.graphics.newImage('graphics/background.png'),
    ['cursor-up'] = love.graphics.newImage('graphics/cursor_up.png'),
    ['healer-female'] = love.graphics.newImage('graphics/characters/healer_f.png'),
    ['healer-male'] = love.graphics.newImage('graphics/characters/healer_m.png'),
    ['mage-female'] = love.graphics.newImage('graphics/characters/mage_f.png'),
    ['mage-male'] = love.graphics.newImage('graphics/characters/mage_m.png'),
    ['warrior-female'] = love.graphics.newImage('graphics/characters/warrior_f.png'),
    ['warrior-male'] = love.graphics.newImage('graphics/characters/warrior_m.png'),
    ['ranger-female'] = love.graphics.newImage('graphics/characters/ranger_f.png'),
    ['ranger-male'] = love.graphics.newImage('graphics/characters/ranger_m.png')
}

FRAMES = {
    ['healer-female'] = generateQuads(TEXTURES['healer-female'], 16, 18),
    ['healer-male'] = generateQuads(TEXTURES['healer-male'], 16, 18),
    ['mage-female'] = generateQuads(TEXTURES['mage-female'], 16, 18),
    ['mage-male'] = generateQuads(TEXTURES['mage-male'], 16, 18),
    ['warrior-female'] = generateQuads(TEXTURES['warrior-female'], 16, 18),
    ['warrior-male'] = generateQuads(TEXTURES['warrior-male'], 16, 18),
    ['ranger-female'] = generateQuads(TEXTURES['ranger-female'], 16, 18),
    ['ranger-male'] = generateQuads(TEXTURES['ranger-male'], 16, 18)
}

FONTS = {
    ['small'] = love.graphics.newFont('fonts/font.ttf', 8),
    ['medium'] = love.graphics.newFont('fonts/font.ttf', 16),
    ['large'] = love.graphics.newFont('fonts/font.ttf', 32),
    ['ff'] = love.graphics.newFont('fonts/finalf.ttf', 48),
    ['ff-small'] = love.graphics.newFont('fonts/finalf.ttf', 24)
}

SOUNDS = {
    ['intro'] = love.audio.newSource('sounds/intro.mp3', 'static')
}
