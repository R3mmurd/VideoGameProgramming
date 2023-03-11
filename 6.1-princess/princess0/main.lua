--[[
    ISPPJ1 2023
    Study Case: The Legend of the Princess (ARPG)

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains the configure the framework.
]]
require 'settings'

function love.load()
    love.window.setTitle("The Legend of the Princess")
    love.graphics.setDefaultFilter('nearest', 'nearest')

    push:setupScreen(VIRTUAL_WIDTH, VIRTUAL_HEIGHT, WINDOW_WIDTH, WINDOW_HEIGHT, {
        fullscreen = false,
        resizable = false
    })
end

function love.draw()
    push:start()
    -- render my game
    push:finish()
end
