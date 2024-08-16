--[[
    ISPPV1 2023
    Study Case: The Legend of the Princess (ARPG)

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains the class PlayerPotIdleState.
]]
PlayerPotIdleState = Class{__includes = BaseState}

function PlayerPotIdleState:init(player, dungeon)
    self.player = player
    self.dungeon = dungeon
    self.player:changeAnimation('pot-idle-' .. self.player.direction)
end

function PlayerPotIdleState:enter(params)
    self.pot = params.pot
end

function PlayerPotIdleState:update(dt)
    if love.keyboard.isDown('left') or love.keyboard.isDown('right') or
       love.keyboard.isDown('up') or love.keyboard.isDown('down') then
        self.player:changeState('pot-walk', {
            pot = self.pot
        })
    end

    if love.keyboard.wasPressed('enter') or love.keyboard.wasPressed('return') then
        table.insert(self.dungeon.currentRoom.projectiles, Projectile(self.pot, self.player.direction))
        self.player:changeState('idle')
    end
end

function PlayerPotIdleState:render()
    local anim = self.player.currentAnimation
    love.graphics.draw(TEXTURES[anim.texture], FRAMES[anim.texture][anim:getCurrentFrame()],
        math.floor(self.player.x - self.player.offsetX), math.floor(self.player.y - self.player.offsetY))
    self.pot:render(0, 0)
end