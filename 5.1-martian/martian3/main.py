import settings
from src.SuperMartian import SuperMartian

if __name__ ==  '__main__':
    super_martian = SuperMartian(
        "Super Martian",
        settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT,
        settings.VIRTUAL_WIDTH, settings.VIRTUAL_HEIGHT
    )
    super_martian.exec()
