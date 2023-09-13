#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """Represent base geometry."""

    def area(self):
        """Not implemented."""
        raise Exception("area() is not implemented")
        
    def integer_validator(self, name, value):
        if type(value) != int:
            raise TabError("<name> must be an integer")
        
        if value <= 0 :
            raise TabError("<name> must be greater than 0")


