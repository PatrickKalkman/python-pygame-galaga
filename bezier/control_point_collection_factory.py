from .control_point_quartet import ControlPointQuartet
from .control_point_quartet_collection import ControlPointQuartetCollection


class ControlPointCollectionFactory:
    @staticmethod
    def create_collection1() -> ControlPointQuartetCollection:
        control_point_quartet_collection = ControlPointQuartetCollection()

        control_point_quartet_collection.add(
            ControlPointQuartet(513, -15, 700, 151, 888, 650, 501, 648)
        )

        control_point_quartet_collection.add(
            ControlPointQuartet(501, 648, 114, 646, 208, 488, 235, 343)
        )

        control_point_quartet_collection.add(
            ControlPointQuartet(235, 343, 262, 198, 326, -181, 513, -15)
        )

        return control_point_quartet_collection

    @staticmethod
    def create_collection2() -> ControlPointQuartetCollection:
        control_point_quartet_collection = ControlPointQuartetCollection()

        control_point_quartet_collection.add(
            ControlPointQuartet(513, -15, 430, 11, 204, 659, 516, 654)
        )

        control_point_quartet_collection.add(
            ControlPointQuartet(516, 654, 828, 649, 420, 388, 525, 375)
        )

        control_point_quartet_collection.add(
            ControlPointQuartet(525, 375, 630, 362, 596, -41, 513, -15)
        )

        return control_point_quartet_collection

    @staticmethod
    def create_collection3() -> ControlPointQuartetCollection:
        control_point_quartet_collection = ControlPointQuartetCollection()

        control_point_quartet_collection.add(
            ControlPointQuartet(513, -15, 365, 16, 663, 556, 516, 654)
        )

        control_point_quartet_collection.add(
            ControlPointQuartet(516, 654, 269, 652, 476, 535, 528, 393)
        )

        control_point_quartet_collection.add(
            ControlPointQuartet(528, 393, 480, 251, 461, 14, 513, -15)
        )

        return control_point_quartet_collection

    @staticmethod
    def create_collection4() -> ControlPointQuartetCollection:
        control_point_quartet_collection = ControlPointQuartetCollection()

        control_point_quartet_collection.add(
            ControlPointQuartet(513, -15, 330, 11, 204, 659, 516, 654)
        )

        control_point_quartet_collection.add(
            ControlPointQuartet(516, 654, 528, 649, 220, 388, 525, 375)
        )

        control_point_quartet_collection.add(
            ControlPointQuartet(525, 375, 530, 362, 396, -41, 513, -15)
        )

        return control_point_quartet_collection
