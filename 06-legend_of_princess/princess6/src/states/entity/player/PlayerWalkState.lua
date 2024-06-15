--[[
    ISPPJ1 2024
    Study Case: The Legend of the Princess (ARPG)

    Author: Colton Ogden
    cogden@cs50.harvard.edu

    Modified by Alejandro Mujica (alejandro.j.mujic4@gmail.com) for teaching purpose.

    This file contains the class PlayerWalkState.
]]
PlayerWalkState = Class{__includes = EntityWalkState}

function PlayerWalkState:init(player, dungeon)
    self.entity = player
    self.dungeon = dungeon

    -- render offset for spaced character sprite
    self.entity.offsetY = 5
    self.entity.offsetX = 0
end

function PlayerWalkState:update(dt)
    if love.keyboard.isDown('left') then
        self.entity.direction = 'left'
        self.entity:changeAnimation('walk-left')
    elseif love.keyboard.isDown('right') then
        self.entity.direction = 'right'
        self.entity:changeAnimation('walk-right')
    elseif love.keyboard.isDown('up') then
        self.entity.direction = 'up'
        self.entity:changeAnimation('walk-up')
    elseif love.keyboard.isDown('down') then
        self.entity.direction = 'down'
        self.entity:changeAnimation('walk-down')
    else
        self.entity:changeState('idle')
    end

    if love.keyboard.wasPressed('space') then
        self.entity:changeState('swing-sword')
    elseif love.keyboard.wasPressed('enter') or love.keyboard.wasPressed('return') then
        local room = self.dungeon.currentRoom
        
        local takenPot = nil
        local potIdx = 0

        for k, obj in pairs(room.objects) do
            if obj.takeable then
                local playerY = self.entity.y + self.entity.height / 2
                local playerHeight = self.entity.height - self.entity.height / 2
                local playerXCenter = self.entity.x + self.entity.width / 2
                local playerYCenter = playerY + playerHeight / 2
                local playerCol = math.floor(playerXCenter / TILE_SIZE)
                local playerRow = math.floor(playerYCenter / TILE_SIZE)
                local objXCenter = obj.x + obj.width / 2
                local objYCenter = obj.y + obj.height / 2
                local objCol = math.floor(objXCenter / TILE_SIZE)
                local objRow = math.floor(objYCenter / TILE_SIZE)
                
                if (self.entity.direction == 'right') and (objRow == playerRow) and (objCol == (playerCol + 1)) then
                    takenPot = obj
                    potIdx = k
                    break
                end

                if (self.entity.direction == 'left') and (objRow == playerRow) and (objCol == (playerCol - 1)) then
                    takenPot = obj
                    potIdx = k
                    break
                end

                if (self.entity.direction == 'up') and (objCol == playerCol) and (objRow == (playerRow - 1)) then
                    takenPot = obj
                    potIdx = k
                    break
                end

                if (self.entity.direction == 'down') and (objCol == playerCol) and (objRow == (playerRow + 1)) then
                    takenPot = obj
                    potIdx = k
                    break
                end
            end

        end

        if takenPot ~= nil  then
            table.remove(room.objects, potIdx)
            self.entity:changeState('pot-lift', {
                pot = takenPot
            })
        end
    end

    -- perform base collision detection against walls
    EntityWalkState.update(self, dt)

    -- if we bumped something when checking collision, check any object collisions
    if self.bumped then
        if self.entity.direction == 'left' then
            
            -- temporarily adjust position
            self.entity.x = self.entity.x - self.entity.walkSpeed * dt

            for k, doorway in pairs(self.dungeon.currentRoom.doorways) do
                if self.entity:collides(doorway) and doorway.open then

                    -- shift entity to center of door to avoid phasing through wall
                    self.entity.y = doorway.y + 4
                    Event.dispatch('shift-left')
                end
            end

            -- readjust position
            self.entity.x = self.entity.x + self.entity.walkSpeed * dt
        elseif self.entity.direction == 'right' then
            -- temporarily adjust position
            self.entity.x = self.entity.x + self.entity.walkSpeed * dt

            for k, doorway in pairs(self.dungeon.currentRoom.doorways) do
                if self.entity:collides(doorway) and doorway.open then

                    -- shift entity to center of door to avoid phasing through wall
                    self.entity.y = doorway.y + 4
                    Event.dispatch('shift-right')
                end
            end
            
            -- readjust position
            self.entity.x = self.entity.x - self.entity.walkSpeed * dt
        elseif self.entity.direction == 'up' then
            -- temporarily adjust position
            self.entity.y = self.entity.y - self.entity.walkSpeed * dt

            for k, doorway in pairs(self.dungeon.currentRoom.doorways) do
                if self.entity:collides(doorway) and doorway.open then

                    -- shift entity to center of door to avoid phasing through wall
                    self.entity.x = doorway.x + 8
                    Event.dispatch('shift-up')
                end
            end

            -- readjust position
            self.entity.y = self.entity.y + self.entity.walkSpeed * dt
        else
            -- temporarily adjust position
            self.entity.y = self.entity.y + self.entity.walkSpeed * dt

            for k, doorway in pairs(self.dungeon.currentRoom.doorways) do
                if self.entity:collides(doorway) and doorway.open then

                    -- shift entity to center of door to avoid phasing through wall
                    self.entity.x = doorway.x + 8
                    Event.dispatch('shift-down')
                end
            end

            -- readjust position
            self.entity.y = self.entity.y - self.entity.walkSpeed * dt
        end
    end
end