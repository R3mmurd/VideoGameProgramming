--[[
    ISPPV1 2023
    Study Case: Ultimate Fantasy (RPG)

    Author: Colton Ogden
    cogden@cs50.harvard.edu

    This class contains the class DialogueState.
]]
DialogueState = Class{__includes = BaseState}

function DialogueState:init(text, callback)
    self.textbox = Textbox(6, 6, VIRTUAL_WIDTH - 12, 64, text, FONTS['small'])
    self.callback = callback or function() end
end

function DialogueState:update(dt)
    self.textbox:update(dt)

    if self.textbox:isClosed() then
        self.callback()
        stateStack:pop()
    end
end

function DialogueState:render()
    self.textbox:render()
end