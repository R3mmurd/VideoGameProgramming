import settings
from src.Match3 import Match3

if __name__ == '__main__':
    match3 = Match3(
        "Match 3",
        settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT,
        settings.VIRTUAL_WIDTH, settings.VIRTUAL_HEIGHT
    )
    match3.exec()
