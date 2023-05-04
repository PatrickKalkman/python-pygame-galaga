import pygame
from pygame import Rect, Surface
from .base_state import BaseState


class Menu(BaseState):
    def __init__(self) -> None:
        super(Menu, self).__init__()
        self.active_index = 0
        self.options: list[str] = ["Start Game", "Quit Game"]
        self.next_state = "GAMEPLAY"

    def render_text(self, index: int) -> pygame.Surface:
        color: pygame.Color = (
            pygame.Color("red") if index == self.active_index else pygame.Color("white")
        )
        return self.font.render(self.options[index], True, color)

    def get_text_position(self, text: Surface, index: int) -> Rect:
        center: tuple[int, int] = (
            self.screen_rect.center[0],
            self.screen_rect.center[1] + (index * 50),
        )
        return text.get_rect(center=center)

    def handle_action(self) -> None:
        if self.active_index == 0:
            self.done = True
        elif self.active_index == 1:
            self.quit = True

    def get_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                self.active_index = 1 if self.active_index <= 0 else 0
            elif event.key == pygame.K_DOWN:
                self.active_index = 0 if self.active_index >= 1 else 1
            elif event.key == pygame.K_RETURN:
                self.handle_action()

    def draw(self, surface: Surface) -> None:
        surface.fill(pygame.Color("black"))
        for index, _ in enumerate(self.options):
            text_render: Surface = self.render_text(index)
            surface.blit(text_render, self.get_text_position(text_render, index))
