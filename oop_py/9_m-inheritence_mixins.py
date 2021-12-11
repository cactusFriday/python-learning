

class FoodMixin:
    food = None

    def get_food(self):
        if self.food is None:
            raise ValueError('Food should be set')
        print(f'I like {self.food}')

class Person:
    def hello(self):
        print('I am a Person')


class Student(FoodMixin, Person):
    food = 'Pizza'

    def hello(self):
        print('I am a Student')

# class Prof(Person):
#     def hello(self):
#         print('I am a Professor')

# class Someone(Student, Prof):
#     pass

s = Student()