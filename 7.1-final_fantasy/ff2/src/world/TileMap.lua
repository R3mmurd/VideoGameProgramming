--[[
    ISPPJ1 2023
    Study Case: Final Fantasy (RPG)

    Author: Colton Ogden
    cogden@cs50.harvard.edu

    Modified by Alejandro Mujica (alejandro.j.mujic4@gmail.com)

    This class contains the class Entity.
]]
TileMap = Class{}

function TileMap:init(width, height, offset)
    self.tiles = {}
    self.width = width
    self.height = height
    self.offsetX = offset and offset.x or 0
    self.offsetY = offset and offset.y or 0
end

function TileMap:render()
    for y = 1, self.height do
        for x = 1, self.width do
            self.tiles[y][x]:render(self.offsetX, self.offsetY)
        end
    end
end
