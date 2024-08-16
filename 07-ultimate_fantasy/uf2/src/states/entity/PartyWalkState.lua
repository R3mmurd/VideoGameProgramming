--[[
    ISPPV1 2024
    Study Case: Ultimate Fantasy (RPG)

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains the class PartyWalkState.
]]
PartyWalkState = Class{__includes = PartyBaseState}

function PartyWalkState:enter(params)
    self.direction = params.direction
    self:checkForEncounter()

    if not self.encounterFound then
        self:attemptMove()
    end
end

function PartyWalkState:checkForEncounter()
    local entity = self.party:firstAlive()
    local x, y = entity.mapX, entity.mapY
    local direction = entity.direction

    -- chance to go to battle if we're walking into a grass tile, else move as normal
    if self.party.world:currentRegion().grassLayer.tiles[y][x].id == TILE_IDS['tall-grass'] and math.random(10) == 1 then
        self.party:changeState('idle')

        -- trigger music changes
        SOUNDS['world']:pause()
        SOUNDS['battle']:play()
        
        -- first, push a fade in; when that's done, push a battle state and a fade
        -- out, which will fall back to the battle state once it pushes itself off
        stateStack:push(
            FadeInState({
                r = 255, g = 255, b = 255,
            }, 1, 
            
            -- callback that will execute once the fade in is complete
            function()
                stateStack:push(BattleState(self.party, self.party.world.current_region, 
                    function() self.party:setPosition(x, y, direction) end))
                stateStack:push(FadeOutState({
                    r = 255, g = 255, b = 255,
                }, 1,
            
                function()
                end))
            end)
        )

        self.encounterFound = true
    else
        self.encounterFound = false
    end
end

function PartyWalkState:attemptMove()

    local first = self.party:firstAlivePosition()
 
    for i = #self.party.characters, first + 1, -1 do
        if not self.party.characters[i].dead then
            local j = i - 1
            
            while j >= first do
                if self.party.characters[j].dead then
                    j = j - 1
                else
                    break
                end
            end

            if self.party.characters[i].mapX < self.party.characters[j].mapX then
                self.party.characters[i].direction = 'right'
            elseif self.party.characters[i].mapX > self.party.characters[j].mapX then
                self.party.characters[i].direction = 'left'
            elseif self.party.characters[i].mapY < self.party.characters[j].mapY then
                self.party.characters[i].direction = 'down'
            elseif self.party.characters[i].mapY > self.party.characters[j].mapY then
                self.party.characters[i].direction = 'up'
            end
            self.party.characters[i]:changeState('walk')

        end
    end
    
    local entity = self.party.characters[first]
    entity.direction = self.direction
    entity:changeState('walk')

    local toX, toY = entity.mapX, entity.mapY

    if entity.direction == 'left' then
        toX = toX - 1
    elseif entity.direction == 'right' then
        toX = toX + 1
    elseif entity.direction == 'up' then
        toY = toY - 1
    else
        toY = toY + 1
    end

    -- move to another region
    if toX < 1 then
        self.party.world:move('left')
        return
    elseif toX > TILE_WIDTH then
        self.party.world:move('right')
        return
    elseif toY < 1 then
        self.party.world:move('up')
        return
    elseif toY > TILE_HEIGHT then
        self.party.world:move('down')
        return
    end

    -- break out if we try to move to the fence
    local fence = self.party.world:currentRegion().fenceLayer
    if fence.tiles[toY][toX].id ~= TILE_IDS['empty'] then
        self.party:changeState('idle')
        return
    end

    for i = #self.party.characters, first + 1, -1 do
        if not self.party.characters[i].dead then
            local j = i - 1
            
            while j >= first do
                if self.party.characters[j].dead then
                    j = j - 1
                else
                    break
                end
            end

            self.party.characters[i].mapX = self.party.characters[j].mapX
            self.party.characters[i].mapY = self.party.characters[j].mapY

        end
    end

    entity.mapY = toY
    entity.mapX = toX

    local lastTween = nil

    for k, c in pairs(self.party.characters) do
        if not c.dead then
            lastTween = Timer.tween(0.5, {
                [c] = {x = (c.mapX - 1) * TILE_SIZE, y = (c.mapY - 1) * TILE_SIZE - ENTITY_HEIGHT / 2}
            })
        end
    end
    lastTween:finish(function()
        if love.keyboard.isDown('left') then
            self.party:changeState('walk', {direction = 'left'})
        elseif love.keyboard.isDown('right') then
            self.party:changeState('walk', {direction = 'right'})
        elseif love.keyboard.isDown('up') then
            self.party:changeState('walk', {direction = 'up'})
        elseif love.keyboard.isDown('down') then
            self.party:changeState('walk', {direction = 'down'})
        else
            self.party:changeState('idle')
        end
    end)
end
