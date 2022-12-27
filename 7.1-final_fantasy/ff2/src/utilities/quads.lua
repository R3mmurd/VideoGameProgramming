function generateQuads(spriteSheet, tileWidth, tileHeight)
    local sheetWidth = spriteSheet:getWidth() / tileWidth
    local sheetHeight = spriteSheet:getHeight() / tileHeight

    local quadCounter = 1
    local quads = {}

    for y = 0, sheetHeight - 1 do
        for x = 0, sheetWidth - 1 do
            quads[quadCounter] =
                love.graphics.newQuad(
                    x * tileWidth, y * tileHeight, tileWidth, tileHeight, spriteSheet:getDimensions()
                )
                quadCounter = quadCounter + 1
            end
        end
    return quads
end