PartyBaseState = Class{}

function PartyBaseState:init(party)
    self.party = party
end

function PartyBaseState:update(dt) end
function PartyBaseState:enter() end
function PartyBaseState:exit() end
function PartyBaseState:processAI(params, dt) end

function PartyBaseState:render()
    for k, c in pairs(self.party.characters) do
        if not c.dead then
            c:render()
        end
    end
end