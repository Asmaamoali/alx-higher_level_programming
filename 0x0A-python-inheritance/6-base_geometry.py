#!/usr/bin/python3
""" creat a empty class """


class BaseGeometry:
    """Represent base geometry."""
    def area(self):
        raise Exception ("area() is not implemented")
