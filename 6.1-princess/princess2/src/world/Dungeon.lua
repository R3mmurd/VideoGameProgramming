Dungeon = Class{}

function Dungeon:init()
    -- current room we're operating in
    self.currentRoom = Room()
end

function Dungeon:render()
    self.currentRoom:render()
end
