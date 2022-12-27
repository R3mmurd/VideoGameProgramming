--[[
    GD50
    Legend of Zelda

    Author: Alejandro Mujica
    aledrums@gmail.com
]]

PlayerPotLiftState = Class{__includes = BaseState}

function PlayerPotLiftState:init(player, dungeon)
    self.player = player
    self.dungeon = dungeon
    self.player:changeAnimation('pot-lift-' .. self.player.direction)
end

function PlayerPotLiftState:enter(params)
    self.pot = params.pot
    self.pot.taken = true
    self.player.currentAnimation:refresh()
    Timer.tween(0.3, {
        [self.pot] = {
            x = self.player.x,
            y = self.player.y - self.pot.height / 2
        }
    })
end

function PlayerPotLiftState:update(dt)
    if self.player.currentAnimation.timesPlayed > 0 then
        self.player.currentAnimation.timesPlayed = 0
        self.player:changeState('pot-idle', {
            pot = self.pot
        })
    end
end

function PlayerPotLiftState:render()
    local anim = self.player.currentAnimation
    love.graphics.draw(TEXTURES[anim.texture], FRAMES[anim.texture][anim:getCurrentFrame()],
        math.floor(self.player.x - self.player.offsetX), math.floor(self.player.y - self.player.offsetY))
    self.pot:render(0, 0)
end