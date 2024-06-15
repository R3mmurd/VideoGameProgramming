--[[
    ISPPJ1 2024
    Study Case: Ultimate Fantasy (RPG)

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com
]]
BattleState = Class{__includes = BaseState}

function BattleState:init(party, region, onExit)
    self.party = party
    self.region = region
    self.onExit = onExit or function() end

    self.tileWidth = BATTLE_WIDTH
    self.tileHeight = BATTLE_HEIGHT

    self.baseLayer = TileMap(self.tileWidth, self.tileHeight, BATTLE_PADDLE)
    self.grassLayer = TileMap(self.tileWidth, self.tileHeight, BATTLE_PADDLE)

    self:createMap()
    self.party:setBattlePositions()  

    self.bottomPanel = Panel(0, VIRTUAL_HEIGHT - 64, VIRTUAL_WIDTH, 64)

    -- flag for when the battle can take input, set in the first update call
    self.battleStarted = false

    self.enemies = {}
    self.finalBoss = false

    self:createEnemies()

    self.energyBars = {}
    self.expBars = {}

    -- add party energy and exp bars
    for k, c in pairs(self.party.characters) do
        if not c.dead then
            self.energyBars[c.name] = ProgressBar {
                x = c.x - math.floor(c.width/4),
                y = c.y - 8,
                width = math.floor(c.width*1.5),
                height = 3,
                color = {r = 189, g = 32, b = 32},
                value = c.currentHP,
                max = c.HP
            }
            self.expBars[c.name] = ProgressBar {
                x = c.x - math.floor(c.width/4),
                y = c.y - 5,
                width = math.floor(c.width*1.5),
                height = 3,
                color = {r = 32, g = 32, b = 189},
                value = c.currentExp,
                max = c.expToLevel
            }
        end
    end

    -- add enemy energy bars
    for k, e in pairs(self.enemies) do
        if not e.dead then
            self.energyBars[e.name] = ProgressBar {
                x = e.x - math.floor(e.width/4),
                y = e.y - 5,
                width = math.floor(e.width*1.5),
                height = 3,
                color = {r = 189, g = 32, b = 32},
                value = e.currentHP,
                max = e.HP
            }
        end
    end
end

function BattleState:createEnemies()
    -- chance to spawn final boss
    if self.region == 'west' and math.random(10) == 1 then
        self.finalBoss = true
        local positions = ENEMIES_POSITIONS[3]

        local enemyInfo = ENTITY_DEFS.enemies.boss
        local enemy = Enemy({
            level = enemyInfo.level,
            name = enemyInfo.name,
            actions = enemyInfo.actions,
            class = enemyInfo.type,
            texture = enemyInfo.texture,
            direction = 'left',
            mapX = positions[1].x,
            mapY = positions[1].y,
            width = enemyInfo.width,
            height = enemyInfo.height,
            baseHP = enemyInfo.baseHP,
            baseAttack = enemyInfo.baseAttack,
            baseDefense = enemyInfo.baseDefense,
            baseMagic = enemyInfo.baseMagic,
            statusGenerated = enemyInfo.statusGenerated,
            animations = enemyInfo.animations
        })
        enemy.stateMachine = StateMachine {
            ['battle'] = function() return EnemyBattleState(enemy) end
        }
        enemy.stateMachine:change('battle')
        table.insert(self.enemies, enemy)

        local enemySet = ENTITY_DEFS.enemies[self.region]

        for i = 2, 3 do
            local enemyInfo = enemySet[math.random(#enemySet)]
            local enemy = Enemy({
                level = enemyInfo.level,
                name = enemyInfo.type .. '-' .. i,
                actions = enemyInfo.actions,
                class = enemyInfo.type,
                texture = enemyInfo.texture,
                direction = 'left',
                mapX = positions[i].x,
                mapY = positions[i].y,
                width = enemyInfo.width,
                height = enemyInfo.height,
                baseHP = enemyInfo.baseHP,
                baseAttack = enemyInfo.baseAttack,
                baseDefense = enemyInfo.baseDefense,
                baseMagic = enemyInfo.baseMagic,
                statusGenerated = enemyInfo.statusGenerated,
                animations = enemyInfo.animations
            })
            enemy.stateMachine = StateMachine {
                ['battle'] = function() return EnemyBattleState(enemy) end
            }
            enemy.stateMachine:change('battle')
            table.insert(self.enemies, enemy)
        end
    else
        local numEnemies = math.random(3, 5)
        local positions = ENEMIES_POSITIONS[numEnemies]
        local enemySet = ENTITY_DEFS.enemies[self.region]

        for i = 1, numEnemies do
            local enemyInfo = enemySet[math.random(#enemySet)]
            local enemy = Enemy({
                level = enemyInfo.level,
                name = enemyInfo.type .. '-' .. i,
                actions = enemyInfo.actions,
                class = enemyInfo.type,
                texture = enemyInfo.texture,
                direction = 'left',
                mapX = positions[i].x,
                mapY = positions[i].y,
                width = enemyInfo.width,
                height = enemyInfo.height,
                baseHP = enemyInfo.baseHP,
                baseAttack = enemyInfo.baseAttack,
                baseDefense = enemyInfo.baseDefense,
                baseMagic = enemyInfo.baseMagic,
                statusGenerated = enemyInfo.statusGenerated,
                animations = enemyInfo.animations
            })
            enemy.stateMachine = StateMachine {
                ['battle'] = function() return EnemyBattleState(enemy) end
            }
            enemy.stateMachine:change('battle')
            table.insert(self.enemies, enemy)
        end
    end
end

function BattleState:createMap()
    for y = 1, self.tileHeight do
        table.insert(self.baseLayer.tiles, {})

        for x = 1, self.tileWidth do
            local id = TILE_IDS['grass'][math.random(#TILE_IDS['grass'])]

            table.insert(self.baseLayer.tiles[y], Tile(x, y, id))
        end
    end

    for y = 1, self.tileHeight do
        table.insert(self.grassLayer.tiles, {})

        for x = 1, self.tileWidth do
            local id = math.random() < 0.3 and TILE_IDS['tall-grass'] or TILE_IDS['empty']
            table.insert(self.grassLayer.tiles[y], Tile(x, y, id))
        end
    end
end

function BattleState:enter(params)
    
end

function BattleState:exit()
    SOUNDS['battle']:stop()
    self.onExit()
end

function BattleState:update(dt)
    -- this will trigger the first time this state is actively updating on the stack
    if not self.battleStarted then
        self:triggerStartingDialogue()
    end

    for k, e in pairs(self.enemies) do
        if not e.dead then
            e:update(dt)
        end
    end
end

function BattleState:render()
    love.graphics.clear(0, 0, 0, 255)
    self.baseLayer:render()
    self.grassLayer:render()

    -- render party
    self.party:render()

    -- render party energy and exp bars
    for k, c in pairs(self.party.characters) do
        if not c.dead then
            self.energyBars[c.name]:render()
            self.expBars[c.name]:render()
        end
    end

    -- render enemies and their energy bars
    for k, e in pairs(self.enemies) do
        if not e.dead then
            e:render()
            self.energyBars[e.name]:render()
        end
    end

    self.bottomPanel:render()
end


function BattleState:triggerStartingDialogue()
    self.battleStarted = true
    --
    -- display a dialogue first for the pokemon that appeared, then the one being sent out
    stateStack:push(BattleMessageState(self, 'A wild creatures horde appeared!',
    
    -- callback for when the battle message is closed
    function()
        names = ''
        for k, c in pairs(self.party.characters) do
            if not c.dead then
                names = names .. c.name .. ', '
            end
        end

        local prefix = self.finalBoss and 'The final boss is here, this is your opportunity to save the world! ' or ''

        stateStack:push(BattleMessageState(self, prefix .. 'Go, ' .. names:sub(1, -3) .. '!',
    
        -- push a battle menu onto the stack that has access to the battle state
        function()
            stateStack:push(BattleMenuState(self))
        end))
    end))

end