--[[
    ISPPJ1 2024
    Study Case: The Legend of the Princess (ARPG)

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains the class Projectile.
]]
local PROJECTILE_SPEED = 150
local PROJECTILE_MAX_TILES = 4

Projectile = Class{}

function Projectile:init(obj, direction)
    self.obj = obj
    self.direction = direction
    self.distance = 0
    self.dead = false
end

function Projectile:update(dt)
    if self.dead then
        return
    end

    local d = PROJECTILE_SPEED*dt
    
    if self.direction == 'up' then
        self.obj.y = self.obj.y - d
        if self.obj.y <= MAP_RENDER_OFFSET_Y + TILE_SIZE - self.obj.height / 2 then 
            self.obj.y = MAP_RENDER_OFFSET_Y + TILE_SIZE - self.obj.height / 2
            self.dead = true
        end
    elseif self.direction == 'down' then
        self.obj.y = self.obj.y + d
        local bottomEdge = VIRTUAL_HEIGHT - (VIRTUAL_HEIGHT - MAP_HEIGHT * TILE_SIZE) 
            + MAP_RENDER_OFFSET_Y - TILE_SIZE

        if self.obj.y + self.obj.height >= bottomEdge then
            self.obj.y = bottomEdge - self.obj.height
            self.dead = true
        end
    elseif self.direction == 'left' then
        self.obj.x = self.obj.x - d
        if self.obj.x <= MAP_RENDER_OFFSET_X + TILE_SIZE then 
            self.obj.x = MAP_RENDER_OFFSET_X + TILE_SIZE
            self.dead = true
        end
    elseif self.direction == 'right' then
        self.obj.x = self.obj.x + d
        if self.obj.x + self.obj.width >= VIRTUAL_WIDTH - TILE_SIZE * 2 then
            self.obj.x = VIRTUAL_WIDTH - TILE_SIZE * 2 - self.obj.width
            self.dead = true
        end
    end

    if self.dead then
        SOUNDS['pot-wall']:play()
        return
    end

    self.distance = self.distance + d

    if self.distance > PROJECTILE_MAX_TILES*TILE_SIZE then
        self.dead = true
    end
end

function Projectile:render()
    self.obj:render(0, 0)
end

function Projectile:collides(target)
    return not (self.obj.x + self.obj.width < target.x or self.obj.x > target.x + target.width or
                self.obj.y + self.obj.height < target.y or self.obj.y > target.y + target.height)
end
