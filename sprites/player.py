import pygame
from pygame.locals import (
    K_LEFT,
    K_RIGHT,
)
from typing import List, Any, Tuple

import constants
from spritesheet import SpriteSheet


class Player(pygame.sprite.Sprite):
    def __init__(self, sprites: SpriteSheet, x: int, y: int) -> None:
        super().__init__()
        self.timer: int = 0
        self.interval: int = 2
        self.number_of_images: int = 6
        rect1: Tuple[int, int, int, int] = (0, 130, 48, 45)
        self.images: List[pygame.Surface] = sprites.load_strip(
            rect1, self.number_of_images, -1
        )
        self.surf: pygame.Surface = self.images[0]
        self.rect: pygame.Rect = self.surf.get_rect(
            center=(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT - 40)
        )
        self.image_index: int = 0

    def get_event(self, event: pygame.event.Event) -> None:
        pass

    def update(self, *args: Any, **kwargs: Any) -> None:
        self.timer += 1

        pressed_keys: Tuple[bool, ...] = pygame.key.get_pressed()

        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > constants.SCREEN_WIDTH:
            self.rect.right = constants.SCREEN_WIDTH

    def get_surf(self) -> pygame.Surface:
        if self.timer % self.interval == 0:
            self.image_index += 1
            if self.image_index >= self.number_of_images:
                self.image_index = 0
        return self.images[self.image_index]
