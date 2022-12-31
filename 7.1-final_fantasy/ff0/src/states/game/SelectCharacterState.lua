--[[
    ISPPJ1 2023
    Study Case: Final Fantasy (RPG)

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains the class SelectCharacterState.
]]
SelectCharacterState = Class{__includes = BaseState}

function SelectCharacterState:init(def)
    self.character = def.character or 1
    self.selected = def.selected or 'male'
    self.character_type = ENTITY_DEFS.characters[self.character]
    self.party = def.party or {}
end

function SelectCharacterState:update(dt)
    if love.keyboard.wasPressed('right') or love.keyboard.wasPressed('left') then
        if self.selected == 'male' then
            self.selected = 'female'
        else
            self.selected = 'male'
        end
    elseif love.keyboard.wasPressed('enter') or love.keyboard.wasPressed('return') then
        table.insert(self.party, self.character, self.selected)
        if self.character < NUM_CHARACTERS then
            stateStack:pop()
            stateStack:push(SelectCharacterState({
                character = self.character + 1,
                selected = self.selected,
                party = self.party
            }))
        else
            SOUNDS['intro']:stop()
            stateStack:push(FadeInState({
                r = 255, g = 255, b = 255
            }, 1,
            function()
                stateStack:pop()
                stateStack:push(FadeOutState({
                    r = 255, g = 255, b = 255
                }, 1,
                function() end))
            end))
        end
    end
end

function SelectCharacterState:render()
    love.graphics.setColor(255, 255, 255, 255)
    love.graphics.setFont(FONTS['medium'])
    love.graphics.printf(self.character_type.type, 0, 20, VIRTUAL_WIDTH, 'center')

    local x = VIRTUAL_WIDTH / 2 - ENTITY_WIDTH / 2 - 30
    local y = VIRTUAL_HEIGHT / 2 - ENTITY_HEIGHT

    love.graphics.draw(TEXTURES[self.character_type.male.texture], 
                       FRAMES[self.character_type.male.texture][8], x, y)
    love.graphics.setFont(FONTS['small'])
    love.graphics.printf(self.character_type.male.name, x - ENTITY_WIDTH, y - 10, ENTITY_WIDTH*3, 'center')

    if self.selected == 'male' then
        love.graphics.draw(TEXTURES['cursor-up'], x, y + ENTITY_HEIGHT + 10)
    end

    x = VIRTUAL_WIDTH / 2 - ENTITY_WIDTH / 2 + 30

    love.graphics.draw(TEXTURES[self.character_type.female.texture], 
                       FRAMES[self.character_type.female.texture][8], x, y)
    love.graphics.setFont(FONTS['small'])
    love.graphics.printf(self.character_type.female.name, x - ENTITY_WIDTH, y - 10, ENTITY_WIDTH*3, 'center')

    if self.selected == 'female' then
        love.graphics.draw(TEXTURES['cursor-up'], x, y + ENTITY_HEIGHT + 10)
    end
end

