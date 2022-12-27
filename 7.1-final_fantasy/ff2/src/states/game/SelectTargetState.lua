--[[
    GD50
    Final Fifty

    Author: Alejandro Mujica
    aledrums@gmail.com
]]

SelectTargetState = Class{__includes = BaseState}

function SelectTargetState:init(battleState, targets, onTargetSelected)
    self.battleState = battleState
    self.targets = targets
    self.onTargetSelected = onTargetSelected or function() end
    self.currentSelection = 1
    for k, t in pairs(targets) do
        if t.dead then
            self.currentSelection =  self.currentSelection + 1
        else
            break
        end
    end
end

function SelectTargetState:findNextAlive()
    local i = self.currentSelection < #self.targets and self.currentSelection + 1 or 1

    while self.targets[i].dead do
        i = i == #self.targets and 1 or i + 1
    end

    self.currentSelection = i
end

function SelectTargetState:findPrevAlive()
    local i = self.currentSelection > 1 and self.currentSelection - 1 or #self.targets

    while self.targets[i].dead do
        i = i == 1 and #self.targets or i - 1
    end

    self.currentSelection = i
end


function SelectTargetState:update(dt)
    for k, e in pairs(self.battleState.enemies) do
        e:update(dt)
    end
    if love.keyboard.wasPressed('right') then
        self:findNextAlive()
    elseif love.keyboard.wasPressed('left') then
        self:findPrevAlive()
    elseif love.keyboard.wasPressed('enter') or love.keyboard.wasPressed('return') then
        -- pop this state
        stateStack:pop()
        self.onTargetSelected(self.targets[self.currentSelection])
    end
end

function SelectTargetState:render()
    love.graphics.draw(TEXTURES['cursor-right'], 
    self.targets[self.currentSelection].x - TILE_SIZE, self.targets[self.currentSelection].y)
end