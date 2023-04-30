from typing import List, Tuple
import pygame
import random
import constants


class StarField:
    LIGHTGREY: Tuple[int, int, int] = (120, 120, 120)
    DARKGREY: Tuple[int, int, int] = (100, 100, 100)
    YELLOW: Tuple[int, int, int] = (120, 120, 0)

    star_field_slow: List[Tuple[int, int]]
    star_field_medium: List[Tuple[int, int]]
    star_field_fast: List[Tuple[int, int]]

    def __init__(self) -> None:
        self.star_field_slow = self._create_stars(50)
        self.star_field_medium = self._create_stars(35)
        self.star_field_fast = self._create_stars(30)

    def _create_stars(self, number_of_stars: int) -> List[Tuple[int, int]]:
        stars: List[Tuple[int, int]] = []
        for _ in range(number_of_stars):
            star_loc_x: int = random.randrange(0, constants.SCREEN_WIDTH)
            star_loc_y: int = random.randrange(0, constants.SCREEN_HEIGHT)
            stars.append((star_loc_x, star_loc_y))
        return stars

    def _render_star_layer(
        self,
        screen: pygame.Surface,
        star_collection: List[Tuple[int, int]],
        speed: int,
        size: int,
        color: Tuple[int, int, int],
    ) -> None:
        for i, star in enumerate(star_collection):
            new_y: int = star[1] + speed
            if new_y > constants.SCREEN_HEIGHT:
                star_x: int = random.randrange(0, constants.SCREEN_WIDTH)
                star_y: int = random.randrange(-20, -5)
                star: Tuple[int, int] = (star_x, star_y)
            else:
                star = (star[0], new_y)
            star_collection[i] = star
            pygame.draw.circle(screen, color, star, size)

    def render(self, screen: pygame.Surface) -> None:
        self._render_star_layer(
            screen, self.star_field_slow, 1, 3, self.DARKGREY
        )
        self._render_star_layer(
            screen, self.star_field_medium, 4, 2, self.LIGHTGREY
        )
        self._render_star_layer(
            screen, self.star_field_fast, 8, 1, self.YELLOW
        )
