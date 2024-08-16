--[[
    ISPPV1 2024
    Study Case: Ultimate Fantasy (RPG)

    Author: Alejandro Mujica
    aledrums@gmail.com

    This class contains the class PlayState.
]]
PlayState = Class{__includes = BaseState}

function PlayState:init(def)
    world = World(def)
end

function PlayState:update(dt)
    world:update(dt)
end

function PlayState:render()
    world:render()
end
