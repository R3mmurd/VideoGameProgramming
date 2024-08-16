--[[
    ISPPV1 2023
    Study Case: Ultimate Fantasy (RPG)

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains the class StartState.
]]
StartState = Class{__includes = BaseState}

function StartState:init()
    SOUNDS['intro']:play()
end

function StartState:update(dt)
    if love.keyboard.wasPressed('enter') or love.keyboard.wasPressed('return') then
        stateStack:push(FadeInState({
            r = 0, g = 0, b = 0
        }, 1,
        function()
            stateStack:pop()
            stateStack:push(SelectCharacterState({character = 1}))
            stateStack:push(FadeOutState({
                r = 0, g = 0, b = 0
            }, 0.5,
            function() end))
        end))
    end
end

function StartState:render()
    love.graphics.draw(TEXTURES['background'], 0, 0, 0, 
                    VIRTUAL_WIDTH / TEXTURES['background']:getWidth(),
                    VIRTUAL_HEIGHT / TEXTURES['background']:getHeight())

    love.graphics.setFont(FONTS['ff'])
    love.graphics.setColor(love.math.colorFromBytes(34, 34, 34, 255))
    love.graphics.printf('ULTIMATE FANTASY', 2, VIRTUAL_HEIGHT / 2 - 30, VIRTUAL_WIDTH, 'center')

    love.graphics.setColor(love.math.colorFromBytes(212, 175, 55, 255))
    love.graphics.printf('ULTIMATE FANTASY', 0, VIRTUAL_HEIGHT / 2 - 32, VIRTUAL_WIDTH, 'center')

    love.graphics.setColor(love.math.colorFromBytes(255, 255, 255, 255))
    love.graphics.setFont(FONTS['ff-small'])
    love.graphics.printf('PRESS ENTER', 0, VIRTUAL_HEIGHT / 2 + 64, VIRTUAL_WIDTH, 'center')
end