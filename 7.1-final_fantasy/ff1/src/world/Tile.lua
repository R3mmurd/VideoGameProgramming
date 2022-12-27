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
