

class Person:
    def __init__(self, name, surname):
        self._name = name
        self._surname = surname
        self._full_name = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name = val
        self._full_name = None
    
    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, val):
        self._surname = val
        self._full_name = None
    
    @property
    def full_name(self):
        if self._full_name is None:
            self._full_name = f'{self._name} {self._surname}'
        return self._full_name
