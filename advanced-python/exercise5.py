class Students:
    def __init__(self, names):
        self.names = names

    def __len__(self):
        return len(self.names)

    def __str__(self):
        s = ''
        i = 0
        while i < len(self.names):
            if i > 0:
                s = s + ', '
            s = s + self.names[i]
            i = i + 1

        return s


'''
students = Students(['Curly', 'Larry', 'Mo'])
print(len(students))
print(students)
'''
