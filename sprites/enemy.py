import math
from typing import Any, List, Tuple
import pygame
from bezier.control_point_quartet_collection import (
    ControlPointQuartetCollection,
)
from bezier.path_point import PathPoint

import constants

from bezier.path_point_calculator import PathPointCalculator
from spritesheet import SpriteSheet


class Enemy(pygame.sprite.Sprite):
    def __init__(
        self,
        sprites: SpriteSheet,
        control_points: ControlPointQuartetCollection,
        enemy: int,
    ) -> None:
        super(Enemy, self).__init__()
        self.rotation: float = 0
        self.timer = 0
        self.control_points: ControlPointQuartetCollection = control_points
        self.bezier_timer = 0.0
        self.interval: int = 2
        self.sprite_index_count: int = 1

        if enemy == 0:
            self.nr_images = 7
            rect1: Tuple[int, int, int, int] = (0, 199, 48, 40)
            self.images: List[pygame.Surface] = sprites.load_strip(
                rect1, self.nr_images, -1
            )
        elif enemy == 1:
            self.nr_images = 4
            rect1 = (0, 248, 48, 40)
            self.images = sprites.load_strip(rect1, self.nr_images, -1)
        elif enemy == 2:
            self.nr_images = 4
            rect1 = (0, 62, 64, 66)
            self.images = sprites.load_strip(rect1, self.nr_images, -1)

        self.surf: pygame.Surface = self.images[0]
        self.rect: pygame.Rect = self.surf.get_rect(
            center=(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT - 20)
        )
        self.image_index = 0
        self.calculator = PathPointCalculator()
        self.previous_point: PathPoint | None = None
        self.rotation_calc = 0

    def get_event(self, event: pygame.event.Event) -> None:
        pass

    def update(self, *args: Any, **kwargs: Any) -> None:
        control_point_index = int(self.bezier_timer)
        path_point: PathPoint = self.calculator.calculate_path_point(
            self.control_points.get_quartet(control_point_index),
            self.bezier_timer,
        )
        if self.previous_point is None:
            self.previous_point = path_point

        self.rotation = self.calculate_rotation(
            self.previous_point, path_point
        )
        self.previous_point = path_point
        self.rect.centerx = int(path_point.xpos)
        self.rect.centery = int(path_point.ypos)
        self.timer += 1
        self.bezier_timer += 0.012
        timer = int(self.bezier_timer)
        if timer > self.control_points.number_of_quartets() - 1:
            self.kill()

    def calculate_rotation(
        self, previous_point: PathPoint, current_point: PathPoint
    ) -> float:
        dx: float = current_point.xpos - previous_point.xpos
        dy: float = current_point.ypos - previous_point.ypos

        return math.degrees(math.atan2(dx, dy)) + 180

    def get_surf(self) -> pygame.Surface:
        if self.timer % self.interval == 0:
            self.image_index += self.sprite_index_count
            if self.image_index == self.nr_images - 1 or self.image_index == 0:
                self.sprite_index_count = -self.sprite_index_count

        rot_image: pygame.Surface = pygame.transform.rotate(
            self.images[self.image_index], self.rotation
        )
        self.rect = rot_image.get_rect(center=self.rect.center)

        return rot_image
