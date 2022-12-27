require 'settings'

function love.load()
    math.randomseed(os.time())
    love.window.setTitle("The Legend of the Princess")
    love.graphics.setDefaultFilter('nearest', 'nearest')

    push:setupScreen(VIRTUAL_WIDTH, VIRTUAL_HEIGHT, WINDOW_WIDTH, WINDOW_HEIGHT, {
        fullscreen = false,
        vsync = true,
        resizable = false
    })

    stateMachine = StateMachine {
        ['start'] = function() return StartState() end,
        ['play'] = function() return PlayState() end,
        ['game-over'] = function() return GameOverState() end
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
    Timer.update(dt)
    stateMachine:update(dt)
    love.keyboard.keysPressed = {}
end

function love.draw()
    push:start()
    stateMachine:render()
    push:finish()
end
