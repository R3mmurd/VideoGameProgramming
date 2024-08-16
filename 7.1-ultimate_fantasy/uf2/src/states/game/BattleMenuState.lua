--[[
    ISPPV1 2023
    Study Case: Ultimate Fantasy (RPG)

    Author: Colton Ogden
    cogden@cs50.harvard.edu

    Modified by: Alejandro Mujica (alejandro.j.mujic4@gmail.com)

    This class contains the class BattleMenuState.
]]
BattleMenuState = Class{__includes = BaseState}

function BattleMenuState:init(battleState)
    self.battleState = battleState
    
    self.battleMenu = Menu {
        x = VIRTUAL_WIDTH - 64,
        y = VIRTUAL_HEIGHT - 64,
        width = 64,
        height = 64,
        items = {
            {
                text = 'Fight',
                onSelect = function()
                    stateStack:pop()
                    stateStack:push(TakeTurnState(self.battleState))
                end
            },
            {
                text = 'Run',
                onSelect = function()
                    SOUNDS['run']:play()
                    
                    -- pop battle menu
                    stateStack:pop()

                    -- show a message saying they successfully ran, then fade in
                    -- and out back to the field automatically
                    stateStack:push(BattleMessageState(self.battleState, 'You fled successfully!',
                        function() end), false)
                    Timer.after(0.5, function()
                        stateStack:push(FadeInState({
                            r = 255, g = 255, b = 255
                        }, 1,
                        
                        -- pop message and battle state and add a fade to blend in the field
                        function()

                            -- resume world music
                            SOUNDS['world']:play()

                            -- pop message state
                            stateStack:pop()

                            -- pop battle state
                            stateStack:pop()

                            stateStack:push(FadeOutState({
                                r = 255, g = 255, b = 255
                            }, 1, function()
                                -- do nothing after fade out ends
                            end))
                        end))
                    end)
                end
            }
        }
    }
end

function BattleMenuState:update(dt)
    for k, e in pairs(self.battleState.enemies) do
        e:update(dt)
    end
    self.battleMenu:update(dt)
end

function BattleMenuState:render()
    self.battleMenu:render()
end