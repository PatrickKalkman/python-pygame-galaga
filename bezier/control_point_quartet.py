from typing import Tuple
from .control_point import ControlPoint


class ControlPointQuartet:
    def __init__(
        self,
        x0: float,
        y0: float,
        x1: float,
        y1: float,
        x2: float,
        y2: float,
        x3: float,
        y3: float,
    ) -> None:
        self.points: list[ControlPoint] = [
            ControlPoint(x0, y0),
            ControlPoint(x1, y1),
            ControlPoint(x2, y2),
            ControlPoint(x3, y3),
        ]

    def get_point(self, point_index: int) -> ControlPoint:
        return self.points[point_index]

    def length(self) -> int:
        return len(self.points)

    def is_in_control_point(
        self, x: float, y: float, radius: float
    ) -> Tuple[int, bool]:
        for index, point in enumerate(self.points):
            distance_squared: float = (point.x - x) ** 2 + (point.y - y) ** 2

            if distance_squared < (radius**2):
                return index, True

        return -1, False
