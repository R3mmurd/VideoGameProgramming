World = Class{}

function World:init(def)
    self.regions = {
        ['center'] = Region({
            isTown = true,
            northGate = true,
            southGate = true,
            eastGate = true,
            westGate = true
        }),
        ['north'] = Region({
            southGate = true
        }),
        ['south'] = Region({
            northGate = true
        }),
        ['east'] = Region({
            westGate = true
        }),
        ['west'] = Region({
            eastGate = true
        }),
    }
    self.current_region = 'center'
    def['world'] = self
    self.party = Party(def)

    SOUNDS['town']:play()
end

function World:currentRegion()
    return self.regions[self.current_region]
end

function World:move(direction)
    local next_region = nil

    local first = self.party:firstAlivePosition()
    local x = self.party.characters[first].mapX
    local y = self.party.characters[first].mapY
    local d = 0

    for k, c in pairs(self.party.characters) do
        if not c.dead then
            d = d + 1
        end
    end

    local xs, ys = {}, {}
    
    if direction == 'right' and self.current_region == 'center' then
        next_region = 'east'
        x = d
    elseif direction == 'left' and self.current_region == 'center' then
        next_region = 'west'
        x = TILE_WIDTH - d + 1
    elseif direction == 'up' and self.current_region == 'center' then
        next_region = 'north'
        y = TILE_HEIGHT - d + 1
    elseif direction == 'down' and self.current_region == 'center' then
        next_region = 'south'
        y = d
    elseif direction == 'right' and self.current_region == 'west' then
        next_region = 'center'
        x = d
    elseif direction == 'left' and self.current_region == 'east' then
        next_region = 'center'
        x = TILE_WIDTH - d + 1
    elseif direction == 'up' and self.current_region == 'south' then
        next_region = 'center'
        y = TILE_HEIGHT - d + 1
    elseif direction == 'down' and self.current_region == 'north' then
        next_region = 'center'
        y = d
    end

    if next_region ~= nil then
        stateStack:push(FadeInState({
            r = 255, g = 255, b = 255
        }, 1,
        function()
            
            if self.current_region == 'center' then
                SOUNDS['town']:stop()
                SOUNDS['world']:play()
            else
                SOUNDS['world']:stop()
                SOUNDS['town']:play()
            end

            self.current_region = next_region
            self.party:setPosition(x, y, direction)

            stateStack:push(FadeOutState({
                r = 255, g = 255, b = 255
            }, 0.5,
            function()
                stateStack:push(ShowTextState({
                    r = 0, g = 0, b = 0
                }, self.current_region,
                function()
                end))
            end))
        end))
    end
end

function World:update(dt)
    self.regions[self.current_region]:update(dt)
    self.party:update(dt)

    if love.keyboard.wasPressed('space') then
        local player = self.party:firstAlive()
        -- look for npcs
        for k, npc in pairs(self.regions[self.current_region].npcs) do
            local dx = math.abs(npc.mapX - player.mapX)
            local dy = math.abs(npc.mapY - player.mapY)

            if dx <= 1 and dy <= 1 then
                npc:onInteract()
            end
        end
    end

end

function World:render()
    self.regions[self.current_region]:render()
    self.party:render()
end