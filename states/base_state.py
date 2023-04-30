import pygame
from pygame import Surface, Rect


class BaseState:
    def __init__(self) -> None:
        self.done: bool = False
        self.quit: bool = False
        self.next_state: str | None = None
        self.screen_rect: Rect = pygame.display.get_surface().get_rect()
        self.font: pygame.font.Font = pygame.font.Font(None, 32)

    def startup(self) -> None:
        pass

    def get_event(self, event: pygame.event.Event) -> None:
        pass

    def update(self, dt: float) -> None:
        pass

    def draw(self, surface: Surface) -> None:
        pass
