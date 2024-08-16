--[[
    ISPPV1 2023
    Study Case: Ultimate Fantasy (RPG)

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This class contains the class PlayState.
]]
ShowTextState = Class{__includes = BaseState}

function ShowTextState:init(color, text, onShowTextComplete)
    self.r = color.r
    self.g = color.g
    self.b = color.b
    self.opacity = 0
    self.text = string.upper(text)

    Timer.tween(1, {
        [self] = {opacity = 255}
    })
    :finish(function()
        Timer.tween(2, {
            [self] = {opacity = 0}
        })
        :finish(function()
            stateStack:pop()
            onShowTextComplete()
        end)
    end)
end

function ShowTextState:render()
    love.graphics.setColor(love.math.colorFromBytes(self.r, self.g, self.b, self.opacity))
    love.graphics.setFont(FONTS['large'])
    love.graphics.printf(self.text, 2, VIRTUAL_HEIGHT / 2 - 30, VIRTUAL_WIDTH, 'center')
    love.graphics.setColor(love.math.colorFromBytes(255, 255, 255, 255))
end