--[[
    ISPPV1 2023
    Study Case: Ultimate Fantasy (RPG)

    Author: Colton Ogden
    cogden@cs50.harvard.edu

    Modified by Alejandro Mujica (alejandro.j.mujic4@gmail.com)

    This class contains the class StateStack.
]]
StateStack = Class{}

function StateStack:init()
    self.states = {}
end

function StateStack:update(dt)
    assert(#self.states > 0)
    self.states[#self.states]:update(dt)
end

function StateStack:processAI(params, dt)
    assert(#self.states > 0)
    self.states[#self.states]:processAI(params, dt)
end

function StateStack:render()
    for i, state in ipairs(self.states) do
        state:render()
    end
end

function StateStack:clear()
    self.states = {}
end

function StateStack:push(state)
    table.insert(self.states, state)
    state:enter()
end

function StateStack:pop()
    assert(#self.states > 0)
    self.states[#self.states]:exit()
    table.remove(self.states)
end
