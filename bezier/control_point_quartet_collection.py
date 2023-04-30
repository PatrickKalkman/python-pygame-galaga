from typing import Tuple, Any, Literal

from bezier.control_point import ControlPoint
from .control_point_quartet import ControlPointQuartet
from .control_point_handler import ControlPointHandler


class ControlPointQuartetCollection:
    def __init__(self) -> None:
        self.control_point_quartets: list[Any] = []

    def add(self, control_point_quartet: ControlPointQuartet) -> None:
        self.control_point_quartets.append(control_point_quartet)

    def number_of_quartets(self) -> int:
        return len(self.control_point_quartets)

    def get_quartet(self, quartet_index: int) -> ControlPointQuartet:
        return self.control_point_quartets[quartet_index]

    def get_quartet_from_time(self, time: float) -> ControlPointQuartet:
        return self.control_point_quartets[int(time)]

    def give_position_is_inside_control_point(
        self, x: float, y: float, image_width: float
    ) -> Tuple[int, int, bool]:
        for quartet_index, quartet in enumerate(self.control_point_quartets):
            control_point_index, is_inside = quartet.is_in_control_point(
                x, y, image_width
            )
            if is_inside:
                return quartet_index, control_point_index, True

        return -1, -1, False

    def get_control_point(
        self, control_point_handler: ControlPointHandler
    ) -> ControlPoint:
        quartet_index: int = control_point_handler.quartet_index
        control_point_index: int = control_point_handler.control_point_index
        return self.control_point_quartets[quartet_index].points[
            control_point_index
        ]

    def save_control_points(self) -> None:
        with open("control_points.txt", "w") as file:
            for quartet in self.control_point_quartets:
                file.write(
                    """
                control_point_quartet_collection.add(ControlPointQuartet("""
                )
                for index, point in enumerate(quartet.points):
                    separator: Literal[",", ""] = "," if index < 3 else ""
                    file.write(f"\n        {point.x}, {point.y}{separator}")
                file.write("))")
