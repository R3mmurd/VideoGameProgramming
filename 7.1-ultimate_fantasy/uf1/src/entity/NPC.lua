--[[
    ISPPV1 2023
    Study Case: Ultimate Fantasy (RPG)

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains the class NPC.
]]
NPC = Class{__includes = Entity}

function NPC:init(def)
    Entity.init(self, def)
end

function NPC:onInteract()
    local text = ENTITY_DEFS.npcs.texts[math.random(#ENTITY_DEFS.npcs.texts)]
    stateStack:push(DialogueState(self.name .. ': ' .. text))
end
