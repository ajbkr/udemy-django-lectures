class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def calculate_human_age(self):
        return self.age * 7


dog = Dog('Hans', 'German Shepherd', 7)
print(dog.calculate_human_age())
