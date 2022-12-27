CharacterWalkState = Class{__includes = EntityBaseState}

function CharacterWalkState:init(entity)
    self.entity = entity
    self.entity:changeAnimation('walk-' .. self.entity.direction)
end
