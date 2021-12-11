class Person():
    def init(self, name, surname):
        self._name = name
        self._surname = surname
        self.name = f'{self._name} {self._surname}'

p = Person('Ivan', 'Ivanov')
print(p.name)