Dungeon = Class{}

function Dungeon:init(player)
    self.player = player
    -- current room we're operating in
    self.currentRoom = Room(self.player)
end

function Dungeon:update(dt)
    self.currentRoom:update(dt)
    self.player.currentAnimation:update(dt)
end

function Dungeon:render()
    self.currentRoom:render()
end
