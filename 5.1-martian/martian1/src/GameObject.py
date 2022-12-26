from src import mixins


class GameObject(mixins.DrawableMixin):
    def __init__(
        self, x: float, y: float, width: float, height: float,
        texture_id: str, frame_index: int
    ) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.texture_id = texture_id
        self.frame_index = frame_index
        self.flipped = False
