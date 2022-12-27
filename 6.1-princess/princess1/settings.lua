Class = require 'lib/class'
push = require 'lib/push'

require 'src/StateMachine'

require 'src/states/BaseState'

require 'src/states/game/StartState'


VIRTUAL_WIDTH = 384
VIRTUAL_HEIGHT = 216

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

TEXTURES = {
    ['background'] = love.graphics.newImage('graphics/background.png')
}

FRAMES = {}

FONTS = {
    ['princess'] = love.graphics.newFont('fonts/princess.otf', 32),
    ['princess-small'] = love.graphics.newFont('fonts/princess.otf', 24)
}

SOUNDS = {
    ['music'] = love.audio.newSource('sounds/music.mp3', 'static')
}
