--[[
    ISPPJ1 2024
    Study Case: The Legend of the Princess (ARPG)

    Author: Colton Ogden
    cogden@cs50.harvard.edu

    Modified by Alejandro Mujica (alejandro.j.mujic4@gmail.com) for teaching purpose.

    This file contains the class PlayState for the game.
]]
PlayState = Class{__includes = BaseState}

function PlayState:init()
    self.dungeon = Dungeon()
    SOUNDS['dungeon-music']:setLooping(true)
    SOUNDS['dungeon-music']:play()
end

function PlayState:update(dt)
    if love.keyboard.wasPressed('escape') then
        love.event.quit()
    end
end

function PlayState:render()
    self.dungeon:render()
end
