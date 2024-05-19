--[[
    ISPPJ1 2023
    Study Case: The Legend of the Princess (ARPG)

    Author: Colton Ogden
    cogden@cs50.harvard.edu

    Modified by Alejandro Mujica (alejandro.j.mujic4@gmail.com) for teaching purpose.

    This file contains the class PlayState for the game.
]]
PlayState = Class{__includes = BaseState}

function PlayState:init()
    self.player = Player {
        animations = ENTITY_DEFS['player'].animations,
        walkSpeed = ENTITY_DEFS['player'].walkSpeed,
        
        x = VIRTUAL_WIDTH / 2 - 8,
        y = VIRTUAL_HEIGHT / 2 - 11,
        
        width = 16,
        height = 22,

        -- one heart == 2 health
        health = 6,

        -- rendering and collision offset for spaced sprites
        offsetY = 5
    }

    self.dungeon = Dungeon(self.player)

    self.player.stateMachine = StateMachine {
        ['walk'] = function() return PlayerWalkState(self.player, self.dungeon) end,
        ['idle'] = function() return PlayerIdleState(self.player, self.dungeon) end,
        ['swing-sword'] = function() return PlayerSwingSwordState(self.player, self.dungeon) end,
        ['pot-lift'] = function() return PlayerPotLiftState(self.player, self.dungeon) end,
        ['pot-idle'] = function() return PlayerPotIdleState(self.player, self.dungeon) end,
        ['pot-walk'] = function() return PlayerPotWalkState(self.player, self.dungeon) end
    }
    self.player:changeState('idle')

    SOUNDS['dungeon-music']:setLooping(true)
    SOUNDS['dungeon-music']:play()
end

function PlayState:exit()
    SOUNDS['dungeon-music']:stop()
end

function PlayState:update(dt)
    if love.keyboard.wasPressed('escape') then
        love.event.quit()
    end

    self.dungeon:update(dt)
end

function PlayState:render()
    -- render dungeon and all entities separate from hearts GUI
    love.graphics.push()
    self.dungeon:render()
    love.graphics.pop()

    -- draw player hearts, top of screen
    local healthLeft = self.player.health
    local heartFrame = 1

    for i = 1, 3 do
        if healthLeft > 1 then
            heartFrame = 5
        elseif healthLeft == 1 then
            heartFrame = 3
        else
            heartFrame = 1
        end

        love.graphics.draw(TEXTURES['hearts'], FRAMES['hearts'][heartFrame],
            (i - 1) * (TILE_SIZE + 1), 2)
        
        healthLeft = healthLeft - 2
    end
end
