--[[
    ISPPJ1 2023
    Study Case: Ultimate Fantasy (RPG)

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains the class EntityBaseState.
]]
EntityBaseState = Class{}

function EntityBaseState:init(entity)
    self.entity = entity
end

function EntityBaseState:update(dt) end
function EntityBaseState:enter() end
function EntityBaseState:exit() end
function EntityBaseState:processAI(params, dt) end

function EntityBaseState:render()
    local anim = self.entity.currentAnimation
    love.graphics.draw(TEXTURES[anim.texture], FRAMES[anim.texture][anim:getCurrentFrame()],
        math.floor(self.entity.x), math.floor(self.entity.y))
end