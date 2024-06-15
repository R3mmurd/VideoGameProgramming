--[[
    ISPPJ1 2024
    Study Case: Ultimate Fantasy (RPG)

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains the configure the framework.
]]
require 'settings'

function love.load()
    math.randomseed(os.time())
    love.window.setTitle('Ultimate Fantasy')
    love.graphics.setDefaultFilter('nearest', 'nearest')

    push:setupScreen(VIRTUAL_WIDTH, VIRTUAL_HEIGHT, WINDOW_WIDTH, WINDOW_HEIGHT, {
        fullscreen = false,
        vsync = true,
        resizable = true
    })

    SOUNDS['intro']:setLooping(true)

    stateStack = StateStack()
    stateStack:push(StartState())

    love.keyboard.keysPressed = {}
end

function love.resize(w, h)
    push:resize(w, h)
end

function love.keypressed(key)
    if key == 'escape' then
        love.event.quit()
    end
    love.keyboard.keysPressed[key] = true
end

function love.keyboard.wasPressed(key)
    return love.keyboard.keysPressed[key]
end

function love.update(dt)
    Timer.update(dt)
    stateStack:update(dt)
    love.keyboard.keysPressed = {}
end

function love.draw()
    push:start()
    stateStack:render()
    push:finish()
end