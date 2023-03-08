--[[
    ISPPJ1 2023
    Study Case: Final Fantasy (RPG)

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This class contains the definition for tile ids.
]]
TILE_WIDTH = VIRTUAL_WIDTH / TILE_SIZE
TILE_HEIGHT = VIRTUAL_HEIGHT / TILE_SIZE

TILE_IDS = {
    ['grass'] = {46, 47},
    ['flowers'] = {16, 24, 32, 40, 48, 56, 64, 72},
    ['empty'] = 101,
    ['tall-grass'] = 42,
    ['half-tall-grass'] = 50,
    ['top-left-fence'] = 73,
    ['top-fence'] = 74,
    ['top-right-fence'] = 75,
    ['left-fence'] = 81,
    ['right-fence'] = 83,
    ['bottom-left-fence'] = 89,
    ['bottom-fence'] = 90,
    ['bottom-right-fence'] = 91,
    ['border-left-fence'] = 65,
    ['border-right-fence'] = 66,
    ['border-top-left-fence'] = 88,
    ['border-bottom-left-fence'] = 87,
    ['border-top-right-fence'] = 96,
    ['border-bottom-right-fence'] = 95
}
