class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def greet(self):
        print(f'Hi! My name is {self.name} and I am a {self.species}')


class Cat(Animal):
    def __init__(self, name):
        Animal.__init__(self, name, 'cat')

    def sound(self):
        print('meow')


class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self, name, 'dog')

    def sound(self):
        print('woof')


cat = Cat('Bluey')
cat.greet()
cat.sound()

dog = Dog('Mila-B')
dog.greet()
dog.sound()
