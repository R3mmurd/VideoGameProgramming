import settings
from src.Breakout import Breakout

if __name__ == '__main__':
    game = Breakout(
        'Breakout',
        settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT,
        settings.VIRTUAL_WIDTH, settings.VIRTUAL_HEIGHT
    )
    game.exec()
