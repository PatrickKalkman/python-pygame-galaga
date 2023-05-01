import pygame
import pytest
from states.splash import Splash

# Initialize pygame to avoid an error when creating Surfaces
pygame.init()

# Create a display surface before testing the Splash class
pygame.display.set_mode((800, 600))


@pytest.fixture
def splash_state() -> Splash:
    return Splash()


def test_splash_state_initialization(splash_state: Splash) -> None:
    assert splash_state.title is not None
    assert splash_state.title_rect is not None
    assert splash_state.next_state == "MENU"
    assert splash_state.time_active == 0
    assert splash_state.done is False


def test_splash_state_update(splash_state: Splash) -> None:
    dt = 1000
    splash_state.update(dt)
    assert splash_state.time_active == 1000
    assert splash_state.done is False

    splash_state.update(dt)
    assert splash_state.time_active == 2000
    assert splash_state.done is True
