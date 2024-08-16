--[[
    ISPPV1 2023
    Study Case: Ultimate Fantasy (RPG)

    Author: Colton Ogden
    cogden@cs50.harvard.edu

    Modified by Alejandro Mujica (alejandro.j.mujic4@gmail.com)

    This class contains the class Tile.
]]
Tile = Class{}

function Tile:init(x, y, id)
    self.x = x
    self.y = y
    self.id = id
end

function Tile:render(offsetX, offsetY)
    love.graphics.draw(TEXTURES['tiles'], FRAMES['tiles'][self.id],
        (self.x - 1 + offsetX) * TILE_SIZE, (self.y - 1 + offsetY) * TILE_SIZE)
end
