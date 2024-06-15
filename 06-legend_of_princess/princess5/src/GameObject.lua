--[[
    ISPPJ1 2024
    Study Case: The Legend of the Princess (ARPG)

    Author: Colton Ogden
    cogden@cs50.harvard.edu

    Modified by Alejandro Mujica (alejandro.j.mujic4@gmail.com) for teaching purpose.

    This file contains the class GameObject.
]]
GameObject = Class{}

function GameObject:init(def, x, y)
    -- string identifying this object type
    self.type = def.type

    self.texture = def.texture
    self.frame = def.frame or 1

    -- whether it acts as an obstacle or not
    self.solid = def.solid

    self.defaultState = def.defaultState
    self.state = self.defaultState
    self.states = def.states

    -- dimensions
    self.x = x
    self.y = y
    self.width = def.width
    self.height = def.height

    -- default empty collision callback
    self.onCollide = function() end
end

function GameObject:update(dt)

end

function GameObject:render(adjacentOffsetX, adjacentOffsetY)
    love.graphics.draw(TEXTURES[self.texture], FRAMES[self.texture][self.states[self.state].frame or self.frame],
        self.x + adjacentOffsetX, self.y + adjacentOffsetY)
end
