--[[
    ISPPV1 2024
    Study Case: Ultimate Fantasy (RPG)

    Author: Colton Ogden
    cogden@cs50.harvard.edu

    Modified by Alejandro Mujica (alejandro.j.mujic4@gmail.com)

    This class contains the class Entity.
]]
Enemy = Class{__includes = BattleEntity}

function Enemy:init(def)
    BattleEntity.init(self, def)
    statusGenerated = def.statusGenerated
end
