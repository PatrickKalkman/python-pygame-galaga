from bezier.control_point_quartet import ControlPointQuartet
from .control_point_quartet_collection import ControlPointQuartetCollection
from .path_point_selector import PathPointSelector
from .control_point_handler import ControlPointHandler


class ControlHandlerMover:
    def __init__(
        self,
        control_point_quartet_collection: ControlPointQuartetCollection,
        path_point_selector: PathPointSelector,
    ) -> None:
        self.control_point_quartet_collection: ControlPointQuartetCollection = (
            control_point_quartet_collection
        )
        self.path_point_selector: PathPointSelector = path_point_selector

    def move_control_handler(
        self, control_point_handler: ControlPointHandler, x: int, y: int
    ) -> None:
        dx: float = (
            self.control_point_quartet_collection.get_control_point(
                control_point_handler
            ).x
            - x
        )
        dy: float = (
            self.control_point_quartet_collection.get_control_point(
                control_point_handler
            ).y
            - y
        )

        self.control_point_quartet_collection.get_control_point(
            control_point_handler
        ).x = x
        self.control_point_quartet_collection.get_control_point(
            control_point_handler
        ).y = y

        if self.path_point_selector.is_path_point(control_point_handler):
            related_path_point: ControlPointHandler = (
                self.path_point_selector.find_related_path_point(
                    control_point_handler
                )
            )
            self.control_point_quartet_collection.get_control_point(
                related_path_point
            ).x = x
            self.control_point_quartet_collection.get_control_point(
                related_path_point
            ).y = y

            related_control_points: list[
                ControlPointHandler
            ] = self.path_point_selector.find_control_points_of_path_point(
                control_point_handler
            )
            self.control_point_quartet_collection.get_control_point(
                related_control_points[0]
            ).x -= dx
            self.control_point_quartet_collection.get_control_point(
                related_control_points[0]
            ).y -= dy
            self.control_point_quartet_collection.get_control_point(
                related_control_points[1]
            ).x -= dx
            self.control_point_quartet_collection.get_control_point(
                related_control_points[1]
            ).y -= dy

        else:  # It is a control point
            related_control_point: ControlPointHandler = (
                self.path_point_selector.find_related_control_point(
                    control_point_handler
                )
            )
            related_path_point = (
                self.path_point_selector.find_path_point_of_control_point(
                    control_point_handler
                )
            )

            xDistance: float = (
                self.control_point_quartet_collection.get_control_point(
                    related_path_point
                ).x
                - x
            )
            yDistance: float = (
                self.control_point_quartet_collection.get_control_point(
                    related_path_point
                ).y
                - y
            )

            self.control_point_quartet_collection.get_control_point(
                related_control_point
            ).x = (
                self.control_point_quartet_collection.get_control_point(
                    related_path_point
                ).x
                + xDistance
            )
            self.control_point_quartet_collection.get_control_point(
                related_control_point
            ).y = (
                self.control_point_quartet_collection.get_control_point(
                    related_path_point
                ).y
                + yDistance
            )

        # The basic tricks in getting this to be a smooth curve across the whole path is to:
        # p3 of the each segment is in common to p0 of next each segment.
        # To make the circular, p3 of last segment must be same as p0 of 1st segment.
        # p2 and p3 of each segment must be on a strait line with p0 and p1 or the next segment. So this means

        # If left handler moved,  must also move corresponding path point so it intersects line to other handler at mid point
        # If right handler moved, must also move corresponding path point so it intersects line to other handler at mid point

    def align_all(self) -> None:
        for quartet_index in range(
            self.control_point_quartet_collection.number_of_quartets()
        ):
            quartet: ControlPointQuartet = (
                self.control_point_quartet_collection.get_quartet(
                    quartet_index
                )
            )
            for point_index in range(4):
                control_point_handler = ControlPointHandler(
                    quartet_index, point_index
                )
                point = quartet.get_point(point_index)
                self.move_control_handler(
                    control_point_handler, int(point.x), int(point.y)
                )
