--[[
    ISPPJ1 2023
    Study Case: Final Fantasy (RPG)

    Author: Alejandro Mujics
    alejandro.j.mujic4@gmail.com

    This class contains the class NPC.
]]
NPC = Class{__includes = Entity}

function NPC:init(def)
    Entity.init(self, def)
end

function NPC:onInteract()
    local text = ENTITY_DEFS.npcs.texts[math.random(#ENTITY_DEFS.npcs.texts)]
    stateStack:push(DialogueState(self.name .. ': ' .. text))
end
