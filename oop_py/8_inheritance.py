

# class IntelCPU:
#     cpu_socket = 1151
#     name = 'Intel'

# class I7(IntelCPU):
#     pass

# class I5(IntelCPU):
#     pass

# class Person:
#     def hello(self):
#         print('I am Person')


# class Student(Person):
#     def hello(self):
#         print('Hello I am Student')

class Person:
    def __init__(self, name) -> None:
        self.name = name

    def hello(self):
        print(f'Hello from {self.name}')

class Student(Person):
    pass

s = Student('Ivan')