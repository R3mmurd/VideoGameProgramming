import pygame

from gale.input_handler import InputHandler, KEY_ESCAPE, InputData
from gale.game import Game
from gale.text import render_text

InputHandler.set_keyboard_action(KEY_ESCAPE, "quit")

class TimerGame(Game):
    def init(self) -> None:
        self.timer = 0
        self.interval = 1
        self.counter = 0
        self.font = pygame.font.Font("font.ttf", 64)
        InputHandler.register_listener(self)
    
    def update(self, dt: float) -> None:
        self.timer += dt

        if self.timer >= self.interval:
            self.timer %= self.interval
            self.counter += 1
        
    def render(self, surface: pygame.Surface) -> None:
        render_text(surface, str(self.counter), self.font, 640, 360, (255, 255, 255), center=True)

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == 'quit' and input_data.pressed:
            self.quit()


if __name__ == '__main__':
    timer_game = TimerGame("Timer 0", 1280, 720)
    timer_game.exec()
