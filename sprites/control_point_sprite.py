from typing import Any, Tuple
from bezier.control_handler_mover import ControlHandlerMover
from bezier.control_point_handler import ControlPointHandler
import pygame

from bezier.control_point_quartet_collection import (
    ControlPointQuartetCollection,
)


class ControlPointSprite(pygame.sprite.Sprite):
    def __init__(
        self,
        x: int,
        y: int,
        color: pygame.Color,
        q_index: int,
        p_index: int,
        control_points: ControlPointQuartetCollection,
        control_handler_mover: ControlHandlerMover,
    ) -> None:
        super(ControlPointSprite, self).__init__()

        self.control_points: ControlPointQuartetCollection = control_points
        self.q_index: int = q_index
        self.p_index: int = p_index
        self.control_handler_mover: ControlHandlerMover = control_handler_mover
        self.original_image = pygame.Surface((50, 50), pygame.SRCALPHA)
        pygame.draw.circle(self.original_image, color, (25, 25), 10)
        self.selected_image = pygame.Surface((50, 50), pygame.SRCALPHA)
        pygame.draw.circle(self.selected_image, color, (25, 25), 10)
        pygame.draw.circle(
            self.selected_image, (255, 255, 255), (25, 25), 10, 2
        )
        self.image: pygame.Surface = self.original_image
        self.rect: pygame.Rect = self.image.get_rect(center=(x, y))
        self.selected = False

    def get_event(self, event: pygame.event.Event) -> None:
        pass

    def update(self, *args: Any, **kwargs: Any) -> None:
        mouse_pos: Tuple[int, int] = pygame.mouse.get_pos()
        mouse_buttons: Tuple[bool, bool, bool] = pygame.mouse.get_pressed()
        self.selected: bool = self.rect.collidepoint(mouse_pos) and any(
            mouse_buttons
        )
        self.image = (
            self.selected_image if self.selected else self.original_image
        )

        if self.selected:
            self.rect = self.image.get_rect(
                center=(mouse_pos[0], mouse_pos[1])
            )
            self.control_handler_mover.move_control_handler(
                ControlPointHandler(self.q_index, self.p_index),
                mouse_pos[0],
                mouse_pos[1],
            )
        else:
            self.x: float = (
                self.control_points.get_quartet(self.q_index)
                .get_point(self.p_index)
                .x
            )
            self.y: float = (
                self.control_points.get_quartet(self.q_index)
                .get_point(self.p_index)
                .y
            )
            self.rect = self.image.get_rect(center=(self.x, self.y))

    def get_surf(self) -> pygame.Surface:
        return self.image
