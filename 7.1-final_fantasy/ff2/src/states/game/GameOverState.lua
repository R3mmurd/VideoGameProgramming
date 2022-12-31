--[[
    ISPPJ1 2023
    Study Case: Final Fantasy (RPG)

    Author: Alejandro Mujica
    aledrums@gmail.com

    This class contains the class GameOverState.
]]
GameOverState = Class{__includes = BaseState}

function GameOverState:update(dt)
    if love.keyboard.wasPressed('return') or love.keyboard.wasPressed('enter') then
        for k, s in pairs(SOUNDS) do
            s:stop()
        end
        stateStack:clear()
        stateStack:push(StartState())
    end
end

function GameOverState:render()
    love.graphics.clear(0, 0, 0, 255)
    love.graphics.setColor(255, 255, 255, 255)

    love.graphics.setFont(FONTS['medium'])
    love.graphics.printf('Your party was defeated!', 0, 10, VIRTUAL_WIDTH, 'center')

    love.graphics.setFont(FONTS['large'])
    love.graphics.setColor(255, 255, 255, 255)
    love.graphics.printf('Game Over', 0, VIRTUAL_HEIGHT / 2 - 32, VIRTUAL_WIDTH, 'center')
end