--[[
    ISPPV1 2024
    Study Case: Ultimate Fantasy (RPG)

    Author: Colton Ogden
    cogden@cs50.harvard.edu

    This class contains the class BaseMessageState.
]]
BattleMessageState = Class{__includes = BaseState}

function BattleMessageState:init(battleState, msg, onClose, canInput)
    self.battleState = battleState
    self.textbox = Textbox(0, VIRTUAL_HEIGHT - 64, VIRTUAL_WIDTH, 64, msg, FONTS['medium'])

    -- function to be called once this message is popped
    self.onClose = onClose or function() end

    -- whether we can detect input with this or not; true by default
    self.canInput = canInput

    -- default input to true if nothing was passed in
    if self.canInput == nil then self.canInput = true end
end

function BattleMessageState:update(dt)
    for k, e in pairs(self.battleState.enemies) do
        e:update(dt)
    end
    if self.canInput then
        self.textbox:update(dt)

        if self.textbox:isClosed() then
            stateStack:pop()
            self.onClose()
        end
    end
end

function BattleMessageState:render()
    self.textbox:render()
end