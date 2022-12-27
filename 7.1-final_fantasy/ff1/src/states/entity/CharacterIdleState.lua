CharacterIdleState = Class{__includes = EntityBaseState}

function CharacterIdleState:init(entity)
    self.entity = entity
    self.entity:changeAnimation('idle-' .. self.entity.direction)
end
