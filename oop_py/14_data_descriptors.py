from time import time
import ctypes

# Non data desc for class MyTime
# class Epoch:
#     def __get__(self, instance, owner_class):
#         print(f'Self: {self}')                  # Epoch object
#         print(f'Instance: {instance}')          # MyTime object or None if call from Class
#         print(f'Owner class: {owner_class}')    # MyTime class
#         print(f'ID of self: {id(self)}')        # Можно создать 2 объекта класса MyTime и проверить их id -> будет ясно что все экземпляры работают с одним объектом
#         if instance is None:
#             return self
#         return int(time())

#     def __set__(self, instance, value):
#         pass


# class MyTime:
#     epoch = Epoch()

# m = MyTime()

def ref_count(obj_id):
    '''return reference amount linked with obj_id (id of the object)'''
    return ctypes.c_long.from_address(obj_id).value

class IntDescriptor:
    def __init__(self):
        self._values = {}

    def __set__(self, instance, value):
        self._values[instance] = value
        # self._value = value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self._values.get(instance)
        # return self._value

class Vector:
    x = IntDescriptor()
    y = IntDescriptor()
    # def __init__(self) -> None:
    #     self.coord = IntDescriptor()
    # def get_new(self):
    #     pass


v1 = Vector()
v2 = Vector()