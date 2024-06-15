--[[
    ISPPJ1 2024
    Study Case: Ultimate Fantasy (RPG)

    Author: Alejandro Mujica
    aledrums@gmail.com

    This class contains the class StatsMenuState.
]]
StatsMenuState = Class{__includes = BaseState}

function StatsMenuState:init(character, stats, onClose)
    self.character = character
    self.HPIncrease = stats.HPIncrease
    self.attackIncrease = stats.attackIncrease
    self.defenseIncrease = stats.defenseIncrease
    self.magicIncrease = stats.magicIncrease

    self.previousHP = self.character.HP - self.HPIncrease
    self.previousAttack = self.character.attack - self.attackIncrease
    self.previousDefense = self.character.defense - self.defenseIncrease
    self.previousMagic = self.character.magic - self.magicIncrease

    self.onClose = onClose or function() end
    
    self.statsMenu = Menu {
        x = 0,
        y = VIRTUAL_HEIGHT - 64,
        width = VIRTUAL_WIDTH,
        height = 64,
        showCursor = false,
        font = FONTS['small'],
        items = {
            {
                text = 'HP: ' .. self.previousHP .. ' + ' .. self.HPIncrease .. ' = ' .. self.character.HP,
                onSelect = function()
                    self:close()
                end
            },
            {
                text = 'Attack: ' .. self.previousAttack .. ' + ' .. self.attackIncrease .. ' = ' .. self.character.attack,
                onSelect = function()
                    self:close()
                end
            },
            {
                text = 'Defense: ' .. self.previousDefense .. ' + ' .. self.defenseIncrease .. ' = ' .. self.character.defense,
                onSelect = function()
                    self:close()
                end
            },
            {
                text = 'Magic: ' .. self.previousMagic .. ' + ' .. self.magicIncrease .. ' = ' .. self.character.magic,
                onSelect = function()
                    self:close()
                end
            }
        }
    }
end

function StatsMenuState:close()
    stateStack:pop()
    self.onClose()
end

function StatsMenuState:update(dt)
    self.statsMenu:update(dt)
end

function StatsMenuState:render()
    self.statsMenu:render()
end