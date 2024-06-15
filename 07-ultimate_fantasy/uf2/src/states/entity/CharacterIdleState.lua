--[[
    ISPPJ1 2024
    Study Case: Ultimate Fantasy (RPG)

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains the class CharacterIdleState.
]]
CharacterIdleState = Class{__includes = EntityBaseState}

function CharacterIdleState:init(entity)
    self.entity = entity
    self.entity:changeAnimation('idle-' .. self.entity.direction)
end
