--[[
    ISPPJ1 2023
    Study Case: Final Fantasy (RPG)

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains the class Region.
]]
Region = Class{}

function Region:init(def)
    self.tileWidth = def.tileWidth or TILE_WIDTH
    self.tileHeight = def.tileHeight or TILE_HEIGHT

    self.isTown = def.isTown or false
    self.numNPCS = self.isTown and math.random(2, 4) or 0
    self.npcs = {}

    self.baseLayer = TileMap(self.tileWidth, self.tileHeight)
    self.fenceLayer = TileMap(self.tileWidth, self.tileHeight)
    self.grassLayer = TileMap(self.tileWidth, self.tileHeight)

    self.gates = {
        north = def.northGate,
        south = def.southGate,
        east = def.eastGate,
        west = def.westGate
    }
    
    self:createMaps()

end

function Region:createMaps()
    -- fill the base tiles table with random grass IDs
    for y = 1, self.tileHeight do
        table.insert(self.baseLayer.tiles, {})

        for x = 1, self.tileWidth do
            local id = TILE_IDS['grass'][math.random(#TILE_IDS['grass'])]

            table.insert(self.baseLayer.tiles[y], Tile(x, y, id))
        end
    end

    -- fill fence layer
    for y = 1, self.tileHeight do
        table.insert(self.fenceLayer.tiles, {})

        for x = 1, self.tileWidth do
            local id = nil

            if y == 1 then
                if x == 1 then
                    id = TILE_IDS['top-left-fence']
                elseif x == self.tileWidth then
                    id = TILE_IDS['top-right-fence']
                else 
                    id = TILE_IDS['top-fence']
                end
            elseif y == self.tileHeight then
                if x == 1 then
                    id = TILE_IDS['bottom-left-fence']
                elseif x == self.tileWidth then
                    id = TILE_IDS['bottom-right-fence']
                else
                    id = TILE_IDS['bottom-fence']
                end
            else
                if x == 1 then
                    id = TILE_IDS['left-fence']
                elseif x == self.tileWidth then
                    id = TILE_IDS['right-fence']
                else
                    id = TILE_IDS['empty']
                end
            end
            table.insert(self.fenceLayer.tiles[y], Tile(x, y, id))
        end
    end

    -- create north gate
    if self.gates.north then
        local x = self.tileWidth / 2
        local y = 1
        self.fenceLayer.tiles[y][x - 1].id = TILE_IDS['border-left-fence']
        self.fenceLayer.tiles[y][x].id = TILE_IDS['empty']
        self.fenceLayer.tiles[y][x + 1].id = TILE_IDS['empty']
        self.fenceLayer.tiles[y][x + 2].id = TILE_IDS['border-right-fence']
    end

    -- create south gate
    if self.gates.south then
        local x = self.tileWidth / 2
        local y = self.tileHeight
        self.fenceLayer.tiles[y][x - 1].id = TILE_IDS['border-left-fence']
        self.fenceLayer.tiles[y][x].id = TILE_IDS['empty']
        self.fenceLayer.tiles[y][x + 1].id = TILE_IDS['empty']
        self.fenceLayer.tiles[y][x + 2].id = TILE_IDS['border-right-fence']
    end

    -- create west gate
    if self.gates.west then
        local x = 1
        local y = self.tileHeight / 2
        self.fenceLayer.tiles[y - 1][x].id = TILE_IDS['border-bottom-left-fence']
        self.fenceLayer.tiles[y][x].id = TILE_IDS['empty']
        self.fenceLayer.tiles[y + 1][x].id = TILE_IDS['empty']
        self.fenceLayer.tiles[y + 2][x].id = TILE_IDS['border-top-left-fence']
    end

    -- create east gate
    if self.gates.east then
        local x = self.tileWidth
        local y = self.tileHeight / 2
        self.fenceLayer.tiles[y - 1][x].id = TILE_IDS['border-bottom-right-fence']
        self.fenceLayer.tiles[y][x].id = TILE_IDS['empty']
        self.fenceLayer.tiles[y + 1][x].id = TILE_IDS['empty']
        self.fenceLayer.tiles[y + 2][x].id = TILE_IDS['border-top-right-fence']
    end

    -- place tall grass in the grass layer by ensuring that there is no grass on a fence
    table.insert(self.grassLayer.tiles, {})
    for x = 1, self.tileWidth do
        table.insert(self.grassLayer.tiles[1], Tile(x, 1, TILE_IDS['empty']))
    end

    for y = 2, self.tileHeight - 1 do
        table.insert(self.grassLayer.tiles, {})

        table.insert(self.grassLayer.tiles[y], Tile(1, y, TILE_IDS['empty']))
        
        for x = 2, self.tileWidth - 1 do
            local id = TILE_IDS['empty']
            if self.isTown then
                -- chance to generate a flower
                if math.random() < 0.2 then
                    id = TILE_IDS['flowers'][math.random(#TILE_IDS['flowers'])]
                else
                    -- chance to spawn an npc
                    if #self.npcs < self.numNPCS and math.random() < 0.05 and y ~= self.tileHeight / 2 then
                        self:createNPC(x, y)
                        self.numPeople = self.numNPCS + 1
                    end
                end
            else
                -- chance to generate a tall grass
                if math.random() < 0.3 then 
                    id = TILE_IDS['tall-grass']
                end
            end
            table.insert(self.grassLayer.tiles[y], Tile(x, y, id))
        end

        table.insert(self.grassLayer.tiles[y], Tile(self.tileWidth, y, TILE_IDS['empty']))
    end
    
    table.insert(self.grassLayer.tiles, {})
    for x = 1, self.tileWidth do
        table.insert(self.grassLayer.tiles[self.tileHeight], Tile(x, self.tileHeight, TILE_IDS['empty']))
    end
end

function Region:createNPC(x, y)
    local direction = ''

    if x <= self.tileWidth / 2 and y <= self.tileHeight/ 2 then
        -- direction should be down or right
        direction = math.random() < 0.6 and 'down' or 'right'
    elseif x <= self.tileWidth / 2 then
        -- direction should be up or right
        direction = math.random() < 0.4 and 'up' or 'right'
    elseif y <= self.tileHeight/ 2 then
        -- direction should be down or left
        direction = math.random() < 0.6 and 'down' or 'left'
    else
        -- direction should be up or left
        direction = math.random() < 0.4 and 'up' or 'left'
    end

    local gender = math.random() < 0.5 and 'male' or 'female'

    local namePos = math.random(#ENTITY_DEFS.npcs[gender].names)
    local name = nil

    for k, n in pairs(ENTITY_DEFS.npcs[gender].names) do
        if namePos == 1 then
            name = n
            table.remove(ENTITY_DEFS.npcs[gender].names, k)
            break
        end
        namePos = namePos - 1
    end

    npc = NPC({
        name = name,
        mapX = x,
        mapY = y,
        width = ENTITY_WIDTH,
        height = ENTITY_HEIGHT,
        direction = direction,
        animations = ENTITY_DEFS['animations'],
        texture = ENTITY_DEFS.npcs[gender].texture
    })

    npc.stateMachine = StateMachine {
        ['idle'] = function() return NPCIdleState(npc) end
    }
    npc.stateMachine:change('idle')

    table.insert(self.npcs, npc) 
end

function Region:update(dt) end

function Region:render()
    self.baseLayer:render()
    self.fenceLayer:render()
    self.grassLayer:render()

    for k, npc in pairs(self.npcs) do
        npc:render()
    end
end
