VIRTUAL_WIDTH = 384
VIRTUAL_HEIGHT = 224

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

TILE_SIZE = 16

Class = require 'lib/class'
push = require 'lib/push'
Timer = require 'lib/knife.timer'

require 'src/Animation'

-- definitions
require 'src/definitions/entity'
require 'src/definitions/tile_id'

-- State Machine, Base State, and State Stack.
require 'src/StateMachine'
require 'src/states/StateStack'
require 'src/states/BaseState'

-- Entity states
require 'src/states/entity/EntityBaseState'
require 'src/states/entity/NPCIdleState'
require 'src/states/entity/CharacterIdleState'
require 'src/states/entity/CharacterWalkState'
require 'src/states/entity/PartyBaseState'
require 'src/states/entity/PartyIdleState'
require 'src/states/entity/PartyWalkState'

-- Game States
require 'src/states/game/DialogueState'
require 'src/states/game/FadeInState'
require 'src/states/game/FadeOutState'
require 'src/states/game/PlayState'
require 'src/states/game/SelectCharacterState'
require 'src/states/game/ShowTextState'
require 'src/states/game/StartState'

-- World
require 'src/world/Region'
require 'src/world/Tile'
require 'src/world/TileMap'
require 'src/world/World'

-- Entity
require 'src/entity/Entity'
require 'src/entity/NPC'
require 'src/entity/Party'
require 'src/entity/BattleEntity'
require 'src/entity/Character'

-- gui
require 'src/gui/Menu'
require 'src/gui/Panel'
require 'src/gui/ProgressBar'
require 'src/gui/Selection'
require 'src/gui/Textbox'

-- Utilities
require 'src/utilities/quads'

TEXTURES = {
    ['tiles'] = love.graphics.newImage('graphics/sheet.png'),
    ['background'] = love.graphics.newImage('graphics/background.png'),
    ['cursor-right'] = love.graphics.newImage('graphics/cursor_right.png'),
    ['cursor-up'] = love.graphics.newImage('graphics/cursor_up.png'),
    ['healer-female'] = love.graphics.newImage('graphics/characters/healer_f.png'),
    ['healer-male'] = love.graphics.newImage('graphics/characters/healer_m.png'),
    ['mage-female'] = love.graphics.newImage('graphics/characters/mage_f.png'),
    ['mage-male'] = love.graphics.newImage('graphics/characters/mage_m.png'),
    ['warrior-female'] = love.graphics.newImage('graphics/characters/warrior_f.png'),
    ['warrior-male'] = love.graphics.newImage('graphics/characters/warrior_m.png'),
    ['ranger-female'] = love.graphics.newImage('graphics/characters/ranger_f.png'),
    ['ranger-male'] = love.graphics.newImage('graphics/characters/ranger_m.png'),
    ['npc-female'] = love.graphics.newImage('graphics/characters/townfolk_f.png'),
    ['npc-male'] = love.graphics.newImage('graphics/characters/townfolk_m.png'),
}

FRAMES = {
    ['tiles'] = generateQuads(TEXTURES['tiles'], 16, 16),
    ['healer-female'] = generateQuads(TEXTURES['healer-female'], 16, 18),
    ['healer-male'] = generateQuads(TEXTURES['healer-male'], 16, 18),
    ['mage-female'] = generateQuads(TEXTURES['mage-female'], 16, 18),
    ['mage-male'] = generateQuads(TEXTURES['mage-male'], 16, 18),
    ['warrior-female'] = generateQuads(TEXTURES['warrior-female'], 16, 18),
    ['warrior-male'] = generateQuads(TEXTURES['warrior-male'], 16, 18),
    ['ranger-female'] = generateQuads(TEXTURES['ranger-female'], 16, 18),
    ['ranger-male'] = generateQuads(TEXTURES['ranger-male'], 16, 18),
    ['npc-female'] = generateQuads(TEXTURES['npc-female'], 16, 18),
    ['npc-male'] = generateQuads(TEXTURES['npc-male'], 16, 18),
}

FONTS = {
    ['small'] = love.graphics.newFont('fonts/font.ttf', 8),
    ['medium'] = love.graphics.newFont('fonts/font.ttf', 16),
    ['large'] = love.graphics.newFont('fonts/font.ttf', 32),
    ['ff'] = love.graphics.newFont('fonts/finalf.ttf', 48),
    ['ff-small'] = love.graphics.newFont('fonts/finalf.ttf', 24)
}

SOUNDS = {
    ['intro'] = love.audio.newSource('sounds/intro.mp3', 'static'),
    ['town'] = love.audio.newSource('sounds/town.mp3', 'static'),
    ['world'] = love.audio.newSource('sounds/world.mp3', 'static'),
    ['blip'] = love.audio.newSource('sounds/blip.wav', 'static')
}
