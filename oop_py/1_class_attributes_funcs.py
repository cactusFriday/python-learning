class Person:
    def __init__(self, name):
        self.name = name
    def create(self):
        self.name = 'Ivan'

    def display(self):
        print(self.name)



# Person.hello()
# Имя 'hello' - function
print(Person.__dict__)