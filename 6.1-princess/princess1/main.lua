require 'settings'

function love.load()
    love.window.setTitle("The Legend of the Princess")
    love.graphics.setDefaultFilter('nearest', 'nearest')

    push:setupScreen(VIRTUAL_WIDTH, VIRTUAL_HEIGHT, WINDOW_WIDTH, WINDOW_HEIGHT, {
        fullscreen = false,
        vsync = true,
        resizable = false
    })

    stateMachine = StateMachine {
        ['start'] = function() return StartState() end
    }

    stateMachine:change('start')

    SOUNDS['music']:setLooping(true)
    SOUNDS['music']:play()

    love.keyboard.keysPressed = {}
end

function love.keypressed(key)
    love.keyboard.keysPressed[key] = true
end

function love.keyboard.wasPressed(key)
    return love.keyboard.keysPressed[key]
end

function love.update(dt)
    stateMachine:update(dt)
    love.keyboard.keysPressed = {}
end

function love.draw()
    push:start()
    stateMachine:render()
    push:finish()
end
