--[[
    ISPPV1 2023
    Study Case: The Legend of the Princess (ARPG)

    Author: Colton Ogden
    cogden@cs50.harvard.edu

    Modified by Alejandro Mujica (alejandro.j.mujic4@gmail.com) for teaching purpose.

    This file contains the class PlayerIdleState.
]]
PlayerIdleState = Class{__includes = EntityIdleState}

function PlayerIdleState:enter(params)
    -- render offset for spaced character sprite
    self.entity.offsetY = 5
    self.entity.offsetX = 0
end

function PlayerIdleState:update(dt)
    EntityIdleState.update(self, dt)
    if love.keyboard.isDown('left') or love.keyboard.isDown('right') or
       love.keyboard.isDown('up') or love.keyboard.isDown('down') then
        self.entity:changeState('walk')
    end

    if love.keyboard.wasPressed('space') then
        self.entity:changeState('swing-sword')
    elseif love.keyboard.wasPressed('enter') or love.keyboard.wasPressed('return') then
        -- look for the pot
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
end