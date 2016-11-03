#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Task_04. New car module"""

import car


class CustomCar(car.Car):
    """Subclass of car.Car
    """
    def __init__(self, tires=None):
        """Constructor for CustomCar
        Args:
            tires(int): input for car tires
        Attribute:
            tires(int):car tires used
        Returns:
            returns a list of car tires
        Examples:
            >>> mycar = CustomCar()
            >>>len(mycar.tires)
            4
            >>>isinstance(mycar.tires[0], CustomTire)
            True
        """
        self.tires = tires
        car.Car.__init__(self, tires)
        self.tires = tires
        tires = CustomTire()
        if self.tires is None:
            self.tires = []
            while len(self.tires) < 4:
                self.tires.append(tires)


class CustomTire(car.Tire):
    """Subclass of car.Tire
    """
    __maximum_miles = 500
