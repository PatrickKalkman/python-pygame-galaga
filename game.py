import pygame
from typing import Dict
from states.base_state import BaseState
from pygame import Surface

import constants


class Game:
    def __init__(
        self,
        screen: pygame.Surface,
        states: Dict[str, BaseState],
        start_state: str,
    ) -> None:
        self.done = False
        self.screen: Surface = screen
        self.clock = pygame.time.Clock()
        self.fps = constants.FPS
        self.states: Dict[str, BaseState] = states
        self.state_name: str = start_state
        self.state: BaseState = self.states[self.state_name]

    def event_loop(self) -> None:
        for event in pygame.event.get():
            self.state.get_event(event)

    def flip_state(self) -> None:
        if self.state.next_state is None:
            raise Exception("No next state")

        next_state: str = self.state.next_state
        self.state.done = False
        self.state_name = next_state
        self.state = self.states[self.state_name]
        self.state.startup()

    def update(self, dt: float) -> None:
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.flip_state()
        self.state.update(dt)

    def draw(self) -> None:
        self.screen.fill((0, 0, 0))
        self.state.draw(self.screen)

    def run(self) -> None:
        while not self.done:
            dt: int = self.clock.tick(self.fps)
            self.event_loop()
            self.update(dt)
            self.draw()
            pygame.display.update()
