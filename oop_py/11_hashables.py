class Person:
    def __init__(self, name) -> None:
        self._name = name

    @property
    def name(self):
        return self._name
    
    def __hash__(self) -> int:
        print('inside hash')
        return hash(self.name)
    
    def __eq__(self, o: object) -> bool:
        print('inside equal')
        return isinstance(o, Person) and self.name == o.name


p1 = Person('Ivan')
p2 = Person('Ivan')