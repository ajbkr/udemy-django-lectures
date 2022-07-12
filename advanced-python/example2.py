class NameOfClass():
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def some_method(self):
        # perform some action
        print(self.param1)


name_of_class = NameOfClass('foo', 'bar')
name_of_class.some_method()
