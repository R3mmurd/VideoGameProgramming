--[[
    ISPPJ1 2024
    Study Case: The Legend of the Princess (ARPG)

    Author: Colton Ogden
    cogden@cs50.harvard.edu

    Modified by Alejandro Mujica (alejandro.j.mujic4@gmail.com) for teaching purpose.

    This file contains the base class BaseState.
]]
BaseState = Class{}

function BaseState:init() end
function BaseState:enter() end
function BaseState:exit() end
function BaseState:update(dt) end
function BaseState:render() end
function BaseState:processAI(params, dt) end
