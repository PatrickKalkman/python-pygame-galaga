from .control_point_quartet import ControlPointQuartet
from .path_point import PathPoint


class PathPointCalculator:
    @staticmethod
    def calculate_path_point(
        control_point_quartet: ControlPointQuartet, time_to_calculate: float
    ) -> PathPoint:
        time: float = time_to_calculate - int(time_to_calculate)

        cx: float = 3.0 * (
            control_point_quartet.get_point(1).x
            - control_point_quartet.get_point(0).x
        )
        cy: float = 3.0 * (
            control_point_quartet.get_point(1).y
            - control_point_quartet.get_point(0).y
        )

        bx: float = (
            3.0
            * (
                control_point_quartet.get_point(2).x
                - control_point_quartet.get_point(1).x
            )
            - cx
        )
        by: float = (
            3.0
            * (
                control_point_quartet.get_point(2).y
                - control_point_quartet.get_point(1).y
            )
            - cy
        )

        ax: float = (
            control_point_quartet.get_point(3).x
            - control_point_quartet.get_point(0).x
            - cx
            - bx
        )
        ay: float = (
            control_point_quartet.get_point(3).y
            - control_point_quartet.get_point(0).y
            - cy
            - by
        )

        cube: float = time * time * time
        square: float = time * time

        resx: float = (
            (ax * cube)
            + (bx * square)
            + (cx * time)
            + control_point_quartet.get_point(0).x
        )
        resy: float = (
            (ay * cube)
            + (by * square)
            + (cy * time)
            + control_point_quartet.get_point(0).y
        )

        return PathPoint(resx, resy)
