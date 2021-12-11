# name = 'Ivan'
class Parent:
    def hello(self):
        print(f'hello {self.name}')


class Person(Parent):
    def __init__(self, name) -> None:
        self.name = name

    @classmethod
    def from_file(cls, file):
        with open(file) as f:
            name = f.read().strip()
        return cls(name = name)
    
    @classmethod
    def from_file2(cls, file):
        with open(file) as f:
            name = f.read().strip()
        return Person(name = name)
    
    @classmethod
    def from_obj(cls, obj):
        if hasattr(obj, 'name'):
            name = getattr(obj, 'name')
            return cls(name=name)
        else:
            return cls()