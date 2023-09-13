#!/usr/bin/python3
""" creat a empty class """


class BaseGeometry:
    """Represent base geometry."""

    def area(self):
        """Not implemented."""
        raise Exception ("area() is not implemented")
