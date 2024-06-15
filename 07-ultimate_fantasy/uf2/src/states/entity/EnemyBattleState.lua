--[[
    ISPPJ1 2024
    Study Case: Ultimate Fantasy (RPG)

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains the class EnemyBattleState.
]]
EnemyBattleState = Class{__includes = EntityBaseState}

function EnemyBattleState:init(entity)
    self.entity = entity
    self.entity:changeAnimation('default')
end
