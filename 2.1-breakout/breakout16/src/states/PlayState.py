from typing import Any

import random

import pygame

from gale.state_machine import BaseState
from gale.input_handler import InputHandler
from gale.text import render_text

import settings
from src import powerups

class PlayState(BaseState):
    def enter(self, **params: dict):
        self.level = params['level']
        self.score = params['score']
        self.lives = params['lives']
        self.paddle = params['paddle']
        self.balls = params['balls']
        self.bricks = params['bricks']
        self.broken_bricks_counter = params['broken_bricks_counter']
        self.live_factor = params['live_factor']
        self.points_to_next_live = params['points_to_next_live']
        self.points_to_next_grow_up = self.score + settings.PADDLE_GROW_UP_POINTS * (self.paddle.size + 1) * self.level
        self.powerups = params.get('powerups', [])

        if not params.get('resume', False):
            self.balls[0].vx = random.randint(-80, 80)
            self.balls[0].vy = random.randint(-170, -100)
            settings.SOUNDS['paddle_hit'].play()

        InputHandler.register_listener(self)

    def exit(self) -> None:
        InputHandler.unregister_listener(self)
    
    def update(self, dt: float) -> None:
        self.paddle.update(dt)

        for ball in self.balls:
            ball.update(dt)
            ball.solve_world_boundaries()

            # Check collision with the paddle
            if ball.collides(self.paddle):
                settings.SOUNDS['paddle_hit'].stop()
                settings.SOUNDS['paddle_hit'].play()
                ball.rebound(self.paddle)
                ball.push(self.paddle)

        # Removing all balls that are not in play
        self.balls = [ball for ball in self.balls if ball.in_play]

        if not self.balls:
            self.lives -= 1
            if self.lives == 0:
                self.state_machine.change("game_over", score=self.score)
            else:
                self.paddle.dec_size()
                self.state_machine.change(
                    'serve',
                    level=self.level,
                    score=self.score,
                    lives=self.lives,
                    paddle=self.paddle,
                    bricks=self.bricks,
                    broken_bricks_counter=self.broken_bricks_counter,
                    points_to_next_live=self.points_to_next_live,
                    live_factor=self.live_factor
                )

        # Check collision with bricks
        for brick in self.bricks:
            brick.update(dt)

            for ball in self.balls:
                if not ball.collides(brick) or not brick.in_play:
                    continue

                brick.hit()
                self.score += brick.score()
                ball.rebound(brick)

                # Check earn life
                if self.score >= self.points_to_next_live:
                    settings.SOUNDS['life'].play()
                    self.lives = min(3, self.lives + 1)
                    self.live_factor += 0.5
                    self.points_to_next_live += settings.LIVE_POINTS_BASE * self.live_factor

                # Check growing up of the paddle
                if self.score >= self.points_to_next_grow_up:
                    settings.SOUNDS['grow_up'].play()
                    self.points_to_next_grow_up += settings.PADDLE_GROW_UP_POINTS * (self.paddle.size + 1) * self.level
                    self.paddle.inc_size()
                
                # Chance to generate two more balls
                if random.random() < 0.05:
                    r = brick.get_collision_rect()
                    self.powerups.append(powerups.TwoMoreBall(r.centerx - 8, r.centery - 8))

                if not brick.in_play:
                    self.broken_bricks_counter += 1
        
        # Update powerups
        for powerup in self.powerups:
            powerup.update(dt)

            if powerup.collides(self.paddle):
                powerup.take(self)
        
        # Remove powerups that are not in play
        self.powerups = [p for p in self.powerups if p.in_play]
        
        # Check victory
        if self.broken_bricks_counter == len(self.bricks):
            self.state_machine.change(
                'victory',
                lives=self.lives,
                level=self.level,
                score=self.score,
                paddle=self.paddle,
                balls=self.balls,
                points_to_next_live=self.points_to_next_live,
                live_factor=self.live_factor
            )

                
    def render(self, surface: pygame.Surface) -> None:
        heart_x = settings.VIRTUAL_WIDTH - 120

        i = 0
        # Draw filled hearts
        while i < self.lives:
            surface.blit(settings.TEXTURES['hearts'], (heart_x, 5), settings.FRAMES['hearts'][0])
            heart_x += 11
            i += 1
        
        # Draw empty hearts
        while i < 3:
            surface.blit(settings.TEXTURES['hearts'], (heart_x, 5), settings.FRAMES['hearts'][1])
            heart_x += 11
            i += 1

        render_text(
            surface, f'Score: {self.score}', settings.FONTS['tiny'],
            settings.VIRTUAL_WIDTH - 80, 5, (255, 255, 255)
        )

        for brick in self.bricks:
            brick.render(surface)

        self.paddle.render(surface)

        for ball in self.balls:
            ball.render(surface)
        
        for powerup in self.powerups:
            powerup.render(surface)

    def on_input(self, input_id: str, input_data: Any) -> None:
        if input_id == 'move_left':
            if input_data.pressed:
                self.paddle.vx = -settings.PADDLE_SPEED
            elif input_data.released and self.paddle.vx < 0:
                self.paddle.vx = 0
        elif input_id == 'move_right':
            if input_data.pressed:
                self.paddle.vx = settings.PADDLE_SPEED
            elif input_data.released and self.paddle.vx > 0:
                self.paddle.vx = 0
        elif input_id == 'pause' and input_data.pressed:
            self.state_machine.change(
                "pause",
                level=self.level,
                score=self.score,
                lives=self.lives,
                paddle=self.paddle,
                balls=self.balls,
                bricks=self.bricks,
                broken_bricks_counter=self.broken_bricks_counter,
                points_to_next_live=self.points_to_next_live,
                live_factor=self.live_factor,
                powerups=self.powerups
            )

