#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """Represent base geometry."""

    def area(self):
        """Not implemented."""
        raise Exception("area() is not implemented")
        
    def integer_validator(self, name, value):
        """Validate a parameter as an integer.

        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TabError("<name> must be an integer")
        if value <= 0 :
            raise TabError("<name> must be greater than 0")
        
class Rectangle (BaseGeometry):
    def __init__(self, width, height):
        self.integer_validator("width" , width)
        self.width = width
        self.integer_validator("height" , height)
        self.height = height
