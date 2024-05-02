--[[
    ISPPJ1 2023
    Study Case: Ultimate Fantasy (RPG)

    Author: Colton Ogden
    cogden@cs50.harvard.edu

    This class contains the class FadeOutState.
]]
FadeOutState = Class{__includes = BaseState}

function FadeOutState:init(color, time, onFadeComplete)
    self.opacity = 255
    self.r = color.r
    self.g = color.g
    self.b = color.b
    self.time = time

    Timer.tween(self.time, {
        [self] = {opacity = 0}
    })
    :finish(function()
        stateStack:pop()
        onFadeComplete()
    end)
end

function FadeOutState:render()
    love.graphics.setColor(love.math.colorFromBytes(self.r, self.g, self.b, self.opacity))
    love.graphics.rectangle('fill', 0, 0, VIRTUAL_WIDTH, VIRTUAL_HEIGHT)

    love.graphics.setColor(love.math.colorFromBytes(255, 255, 255, 255))
end