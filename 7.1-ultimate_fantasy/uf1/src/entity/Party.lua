--[[
    ISPPJ1 2023
    Study Case: Ultimate Fantasy (RPG)

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains the class Party.
]]
Party = Class{}

function Party:init(def)
    self.characters = {}
    self.world = def.world

    local x = TILE_WIDTH / 2 + 2
    local y = TILE_HEIGHT / 2

    for k, g in pairs(def.party) do
        local characterInfo = ENTITY_DEFS.characters[k]
        local character = Character({
            level = characterInfo.properties.level,
            name = characterInfo[g].name,
            class = characterInfo.type,
            texture = characterInfo[g].texture,
            actions = characterInfo.actions,
            baseHP = characterInfo.properties.baseHP,
            baseAttack = characterInfo.properties.baseAttack,
            baseDefense = characterInfo.properties.baseDefense,
            baseMagic = characterInfo.properties.baseMagic,
            HPIV = characterInfo.properties.HPIV,
            attackIV = characterInfo.properties.attackIV,
            defenseIV = characterInfo.properties.defenseIV,
            magicIV = characterInfo.properties.magicIV,
            level = characterInfo.properties.level,
            direction = 'down',
            mapX = x,
            mapY = y,
            width = ENTITY_WIDTH,
            height = ENTITY_HEIGHT,
            animations = ENTITY_DEFS.animations
        })
        
        character.stateMachine = StateMachine {
            ['idle'] = function() return CharacterIdleState(character) end,
            ['walk'] = function() return CharacterWalkState(character) end
        }
        character.stateMachine:change('idle')
    
        self.characters[k] = character
        x = x - 1
    end

    self.stateMachine = StateMachine {
        ['idle'] = function() return PartyIdleState(self) end,
        ['walk'] = function() return PartyWalkState(self) end
    }
    self.stateMachine:change('idle')
end

function Party:setBattlePositions()
    for k, c in pairs(self.characters) do
        if not c.dead then
            c.mapX = PARTY_BATTLE_POSITIONS[k].x
            c.mapY = PARTY_BATTLE_POSITIONS[k].y
            c.x = (c.mapX - 1) * TILE_SIZE
            c.y = (c.mapY - 1) * TILE_SIZE - ENTITY_HEIGHT / 2
            c.direction = 'right'
        end
    end
    self:changeState('idle')
end

function Party:setPosition(x, y, direction)
    local dx = 0
    local dy = 0

    if direction == 'up' then
        dy = 1
    elseif direction == 'down' then
        dy = -1
    elseif direction == 'right' then
        dx = -1
    elseif direction == 'left' then
        dx = 1
    end

    for k, c in pairs(self.characters) do
        if not c.dead then
            c.mapX = x
            c.mapY = y
            c.x = (c.mapX - 1) * TILE_SIZE
            c.y = (c.mapY - 1) * TILE_SIZE - ENTITY_HEIGHT / 2
            c.direction = direction
            x = x + dx
            y = y + dy
        end
    end

    self:changeState('idle')
end

function Party:changeState(name, params)
    self.stateMachine:change(name, params)
end

function Party:update(dt)
    self.stateMachine:update(dt)
    for k, c in pairs(self.characters) do
        if not c.dead then
            c:update(dt)
        end
    end
end

function Party:firstAlivePosition()
    local first = 1

    for k, c in pairs(self.characters) do
        if c.dead then
            first = first + 1
        else
            break
        end
    end

    return first
end

function Party:firstAlive()
    for k, c in pairs(self.characters) do
        if not c.dead then
            return c
        end
    end
end

function Party:render()
    self.stateMachine:render()
end
