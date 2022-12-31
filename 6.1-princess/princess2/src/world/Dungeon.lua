--[[
    ISPPJ1 2023
    Study Case: The Legend of the Princess (ARPG)

    Author: Colton Ogden
    cogden@cs50.harvard.edu

    Modified by Alejandro Mujica (alejandro.j.mujic4@gmail.com) for teaching purpose.

    This file contains the class Dungeon.
]]
Dungeon = Class{}

function Dungeon:init()
    -- current room we're operating in
    self.currentRoom = Room()
end

function Dungeon:render()
    self.currentRoom:render()
end
