class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed


dog1 = Dog('Hans', 'German Shepherd')
dog2 = Dog('Lou', 'Labrador')

print(f'{dog1.name} and {dog2.name} are friends')
