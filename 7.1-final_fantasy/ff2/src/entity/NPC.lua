NPC = Class{__includes = Entity}

function NPC:init(def)
    Entity.init(self, def)
end

function NPC:onInteract()
    local text = ENTITY_DEFS.npcs.texts[math.random(#ENTITY_DEFS.npcs.texts)]
    stateStack:push(DialogueState(self.name .. ': ' .. text))
end
