--[[
    ISPPV1 2023
    Study Case: Ultimate Fantasy (RPG)

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This class contains the class PartyIdleState.
]]
PartyIdleState = Class{__includes = PartyBaseState}

function PartyIdleState:init(party)
    PartyBaseState.init(self, party)
    for k, c in pairs(self.party.characters) do
        c:changeAnimation('idle-' .. c.direction)
    end
end

function PartyIdleState:update(dt)
    if love.keyboard.isDown('left') then
        self.party:changeState('walk', {direction = 'left'})
    elseif love.keyboard.isDown('right') then
        self.party:changeState('walk', {direction = 'right'})
    elseif love.keyboard.isDown('up') then
        self.party:changeState('walk', {direction = 'up'})
    elseif love.keyboard.isDown('down') then
        self.party:changeState('walk', {direction = 'down'})
    end
end