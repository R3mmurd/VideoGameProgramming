--[[
    ISPPJ1 2023
    Study Case: The Legend of the Princess (ARPG)

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains the configure the framework.
]]
require 'settings'

function love.load()
    math.randomseed(os.time())
    love.window.setTitle("The Legend of the Princess")
    love.graphics.setDefaultFilter('nearest', 'nearest')

    push:setupScreen(VIRTUAL_WIDTH, VIRTUAL_HEIGHT, WINDOW_WIDTH, WINDOW_HEIGHT, {
        fullscreen = false,
        resizable = false
    })

    stateMachine = StateMachine {
        ['start'] = function() return StartState() end,
        ['play'] = function() return PlayState() end
    }

    stateMachine:change('start')

    love.keyboard.keysPressed = {}
end

function love.keypressed(key)
    love.keyboard.keysPressed[key] = true
end

function love.keyboard.wasPressed(key)
    return love.keyboard.keysPressed[key]
end

function love.update(dt)
    Timer.update(dt)
    stateMachine:update(dt)
    love.keyboard.keysPressed = {}
end

function love.draw()
    push:start()
    stateMachine:render()
    push:finish()
end
