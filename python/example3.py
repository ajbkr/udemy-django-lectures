'''
my_var = 42
v = ['item', 0, 10.2, 'some', my_var]
print(v)
'''

my_var = 10
# my_list = [1, 2, 3, my_var]
my_list = [100, 200, 300, 400, 500]
# print(my_list)
# print(my_list[0])
# print(my_list[0:3])
print(my_list[1:3])

my_var = 'NEW'
# my_list.append(my_var)
print(my_list)

# my_list.insert(0, my_var)
my_list.insert(1, my_var)
print(my_list)

item_removed = my_list.pop()
print(my_list)
print(item_removed)

my_list.append(item_removed)
my_list.pop()
print(my_list)

my_list.pop(0)
print(my_list)

my_list.reverse()
print(my_list)

my_list = [4, 5, 2, 59, 1, 2, 3, 9, 2, 1, 2]
my_list.sort()
print(my_list)

my_list.sort()
my_list.reverse()
print(my_list)
