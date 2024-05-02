--[[
    ISPPJ1 2023
    Study Case: Ultimate Fantasy (RPG)

    Author: Colton Ogden
    cogden@cs50.harvard.edu

    Modified by Alejandro Mujica (alejandro.j.mujic4@gmail.com)

    This class contains the class Entity.
]]
Entity = Class{}

function Entity:init(def)
    self.name = def.name
    
    self.direction = def.direction or 'down'
    self.texture = def.texture

    self.animations = self:createAnimations(def.animations)

    self.mapX = def.mapX
    self.mapY = def.mapY

    self.width = def.width
    self.height = def.height

    self.x = (self.mapX - 1) * TILE_SIZE

    -- halfway raised on the tile just to simulate height/perspective
    self.y = (self.mapY - 1) * TILE_SIZE - self.height / 2
end

function Entity:changeState(name)
    self.stateMachine:change(name)
end

function Entity:changeAnimation(name)
    self.currentAnimation = self.animations[name]
end

function Entity:createAnimations(animationDefs)
    local animations = {}

    for k, animationDef in pairs(animationDefs) do
        animations[k] = Animation {
            texture = self.texture,
            frames = animationDef.frames,
            interval = animationDef.interval
        }
    end

    return animations
end

--[[
    Called when we interact with this entity, as by pressing enter.
]]
function Entity:onInteract()

end

function Entity:processAI(params, dt)
    self.stateMachine:processAI(params, dt)
end

function Entity:update(dt)
    self.currentAnimation:update(dt)
    self.stateMachine:update(dt)
end

function Entity:render()
    self.stateMachine:render()
end
