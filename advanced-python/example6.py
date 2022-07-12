'''
my_list = [1, 2, 3]

print(my_list)
print(len(my_list))
'''


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __len__(self):
        # return 99
        return self.pages

    def __str__(self):
        return f'{self.title} written by {self.author}'


my_book = Book('Python Rocks!', 'Jose', 120)
print(my_book)
print(len(my_book))
