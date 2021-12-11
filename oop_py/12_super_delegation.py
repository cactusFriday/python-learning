

# class Person:
#     def __init__(self, name) -> None:
#         self.name = name


# class Student(Person):
#     def __init__(self, name, surname) -> None:
#         super().__init__(name)
#         self.surname = surname

class Person:
    def hello(self):
        print(f'Bound with {self}')


class Student(Person):
    def hello(self):
        print('Student obj.hello() is called')
        super().hello()
        print(super())
        # print(dir(super().__this_class__))
        return super

s = Student()