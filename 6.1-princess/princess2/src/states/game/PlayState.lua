PlayState = Class{__includes = BaseState}

function PlayState:init()
    self.dungeon = Dungeon()
end

function PlayState:update(dt)
    if love.keyboard.wasPressed('escape') then
        love.event.quit()
    end
end

function PlayState:render()
    self.dungeon:render()
end
