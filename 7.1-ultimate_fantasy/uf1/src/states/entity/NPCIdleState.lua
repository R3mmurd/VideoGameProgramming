--[[
    ISPPJ1 2023
    Study Case: Ultimate Fantasy (RPG)

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This class contains the class NPCIdleState.
]]
NPCIdleState = Class{__includes = EntityBaseState}

function NPCIdleState:init(entity)
    self.entity = entity
    self.entity:changeAnimation('idle-' .. self.entity.direction)
end
