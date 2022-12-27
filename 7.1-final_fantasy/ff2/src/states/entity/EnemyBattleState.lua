EnemyBattleState = Class{__includes = EntityBaseState}

function EnemyBattleState:init(entity)
    self.entity = entity
    self.entity:changeAnimation('default')
end
