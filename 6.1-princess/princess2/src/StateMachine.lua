--[[
    ISPPV1 2023
    Study Case: The Legend of the Princess (ARPG)

    Author: Colton Ogden
    cogden@cs50.harvard.edu

    This file contains the class StateMachine.
]]
StateMachine = Class{}

function StateMachine:init(states)
    self.empty = {
        render = function() end,
        update = function() end,
        processAI = function() end,
        enter = function() end,
        exit = function() end
    }

    self.states = states or {} -- [name] -> [function that returns states]
    self.current = self.empty
end

function StateMachine:change(stateName, enterParams)
    assert(self.states[stateName]) -- state must exist.
    self.current:exit()
    self.current = self.states[stateName]()
    self.current:enter(enterParams)
end

function StateMachine:update(dt)
    self.current:update(dt)
end

function StateMachine:render()
    self.current:render()
end

function StateMachine:processAI(params, dt)
    self.current:processAI(params, dt)
end
