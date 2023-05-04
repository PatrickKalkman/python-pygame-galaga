import pygame
from pygame import Surface, Rect
from .base_state import BaseState


class GameOver(BaseState):
    def __init__(self) -> None:
        super(GameOver, self).__init__()
        self.title: Surface = self.font.render("Game Over", True, pygame.Color("white"))
        self.title_rect: Rect = self.title.get_rect(center=self.screen_rect.center)
        self.instructions: Surface = self.font.render(
            "Press R to start again, or enter to go to the menu",
            True,
            pygame.Color("white"),
        )
        instructions_center: tuple[int, int] = (
            self.screen_rect.center[0],
            self.screen_rect.center[1] + 50,
        )
        self.instructions_rect: Rect = self.instructions.get_rect(
            center=instructions_center
        )

    def get_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RETURN:
                self.next_state = "MENU"
                self.done = True
            elif event.key == pygame.K_r:
                self.next_state = "GAMEPLAY"
                self.done = True
            elif event.key == pygame.K_ESCAPE:
                self.quit = True

    def draw(self, surface: Surface) -> None:
        surface.fill(pygame.Color("black"))
        surface.blit(self.title, self.title_rect)
        surface.blit(self.instructions, self.instructions_rect)
