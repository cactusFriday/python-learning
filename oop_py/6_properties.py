

class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, val):
        self._name = val
    # def set_name(self, val):
    #     print('From set_name()')
    #     self._name = val

    # name = name.setter(set_name)


p = Person('Dima')