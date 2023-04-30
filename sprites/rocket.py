import math
from typing import List, Any
import pygame
import constants
from spritesheet import SpriteSheet


class Rocket(pygame.sprite.Sprite):
    def __init__(self, sprites: SpriteSheet, xSpeed: int, ySpeed: int) -> None:
        super().__init__()
        self.timer: int = 0
        self.interval: int = 2
        self.number_of_images: int = 3
        self.ySpeed: int = ySpeed
        self.xSpeed: int = xSpeed
        self.images: List[pygame.Surface] = sprites.load_strip(
            (0, 177, 12, 14), self.number_of_images, -1
        )

        self.surf: pygame.Surface = self.images[1]
        self.rect: pygame.Rect = self.surf.get_rect(
            center=(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT - 20)
        )
        self.image_index: int = 0
        self.rotation: float = 0
        if self.ySpeed > 0:
            self.rotation = math.degrees(math.atan2(xSpeed, ySpeed)) + 180

    def get_event(self, event: pygame.event.Event) -> None:
        pass

    def update(self, *args: Any, **kwargs: Any) -> None:
        self.timer += 1
        self.rect.move_ip(self.xSpeed, self.ySpeed)

        if self.rect.bottom < 0 or self.rect.top > constants.SCREEN_HEIGHT:
            self.kill()

    def get_surf(self) -> pygame.Surface:
        if self.timer % self.interval == 0:
            self.image_index += 1
        if self.image_index >= self.number_of_images:
            self.image_index = 0

        rot_image: pygame.Surface = pygame.transform.rotate(
            self.images[self.image_index], self.rotation
        )
        self.rect = rot_image.get_rect(center=self.rect.center)

        return rot_image
