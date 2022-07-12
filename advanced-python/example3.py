'''
# class Sample:
class Sample():
    # pass

    def __init__(self, name):
        self.name = name


x = Sample(name='Becky')
# print(type(x))
# print(x.name)
'''


'''
class Student:
    planet = 'Earth'  # CLASS OBJECT ATTRIBUTE

    def __init__(self, name, gpa):
        self.name = name  # ATTRIBUTES
        self.gpa = gpa

    def print_planet(self):
        print(self.planet)


stu1 = Student(name='Andrew', gpa=4.0)
stu2 = Student(name='Taylor', gpa=4.2)
print(stu1.name)
print(stu1.gpa)
print(stu1)
stu1.print_planet()
print(stu1.planet)
'''


class Agent:
    origin = 'USA'

    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight


x = Agent('Jose', 6, 170)
print(x.weight)
x.weight = 160
print(x.weight)

print(x.origin)
x.origin = 'banana'
print(x.origin)

y = Agent('Minion', 4, 50)
print(y.origin)
