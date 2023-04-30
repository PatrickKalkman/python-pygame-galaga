import pygame
from typing import List, Tuple, Any
from pygame import Rect, Surface
from pygame.sprite import Sprite

from spritesheet import SpriteSheet


class Explosion(Sprite):
    def __init__(self, sprites: SpriteSheet, x: int, y: int) -> None:
        super().__init__()
        self.timer: int = 0
        self.interval: int = 2
        self.number_of_images: int = 10
        self.images: List[Surface] = self.load_explosion_images(sprites)

        self.surf: Surface = self.images[0]
        self.rect: Rect = self.surf.get_rect(center=(x, y))
        self.image_index: int = 0

    def load_explosion_images(self, sprites: SpriteSheet) -> List[Surface]:
        rect1: Tuple[int, int, int, int] = (64, 0, 64, 64)
        rect2: Tuple[int, int, int, int] = (0, 64, 64, 64)
        rect3: Tuple[int, int, int, int] = (0, 128, 64, 64)
        images: List[Surface] = sprites.load_strip(rect1, 3, -1)
        images.extend(sprites.load_strip(rect2, 4, -1))
        images.extend(sprites.load_strip(rect3, 3, -1))

        return [pygame.transform.scale(image, (128, 128)) for image in images]

    def get_event(self, event: pygame.event.Event) -> None:
        pass

    def update(self, *args: Any, **kwargs: Any) -> None:
        self.timer += 1
        if self.timer % self.interval == 0:
            self.image_index += 1

        if self.image_index >= self.number_of_images:
            self.kill()

    def get_surf(self) -> Surface:
        return self.images[self.image_index]
