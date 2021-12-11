
from typing import Type


class Room:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.area = self.x * self.y

    def __add__(self, room_obj):
        if isinstance(room_obj, Room):
            return self.area + room_obj.area
        raise TypeError('Wrong object')

    def __eq__(self, room_obj: object) -> bool:
        if isinstance(room_obj, Room):
            if self.area == room_obj.area:
                return True
            else:
                return False
        raise TypeError('Wrong object')

r1 = Room(3, 5)
r2 = Room(4, 8)