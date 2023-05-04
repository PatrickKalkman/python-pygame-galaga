from typing import List, Optional, Union, Tuple
import pygame
from pygame import Color, Surface


class SpriteSheet:
    def __init__(self, filename: str) -> None:
        """Load the sheet."""
        try:
            self.sheet: Surface = pygame.image.load(filename).convert_alpha()
            self.sheet.set_colorkey(-1, pygame.RLEACCEL)
        except pygame.error as e:
            print(f"Unable to load spritesheet image: {filename}")
            raise SystemExit(e)

    def image_at(
        self,
        rectangle: Tuple[int, int, int, int],
        colorkey: Optional[Union[int, Color]] = None,
    ) -> Surface:
        """Load a specific image from a specific rectangle."""
        rect = pygame.Rect(rectangle)
        image: Surface = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image

    def images_at(
        self,
        rects: List[Tuple[int, int, int, int]],
        colorkey: Optional[Union[int, Color]] = None,
    ) -> List[Surface]:
        """Load a whole bunch of images and return them as a list."""
        return [self.image_at(rect, colorkey) for rect in rects]

    def load_strip(
        self,
        rect: Tuple[int, int, int, int],
        image_count: int,
        colorkey: Optional[Union[int, Color]] = None,
    ) -> List[Surface]:
        """Load a whole strip of images, and return them as a list."""
        tups: list[tuple[int, int, int, int]] = [
            (rect[0] + rect[2] * x, rect[1], rect[2], rect[3]) for x in range(image_count)
        ]
        return self.images_at(tups, colorkey)
