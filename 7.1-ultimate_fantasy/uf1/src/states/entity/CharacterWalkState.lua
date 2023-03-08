--[[
    ISPPJ1 2023
    Study Case: Ultimate Fantasy (RPG)

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains the class CharacterWalkState.
]]
CharacterWalkState = Class{__includes = EntityBaseState}

function CharacterWalkState:init(entity)
    self.entity = entity
    self.entity:changeAnimation('walk-' .. self.entity.direction)
end
