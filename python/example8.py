'''
my_iterable = [1, 2, 3]
for item_name in my_iterable:
    print(item_name)
'''

'''
# my_list = [1, 2, 3, 4, 5]
# sales = [1, 2, 3, 4, 5]
sales = (1, 2, 3, 4, 5)

# for item in my_list:
# for jelly in my_list:
for num in sales:
    # print(item)
    # print(jelly)
    # print('hello')
    print(f'Example sale of: {num}')
'''

'''
employees = {'ceo': 'cindy', 'cfo': 'james'}

#for key in employees:
for position in employees:
    #print(key)
    #print(employees[key])
    print(f'The {position.upper()} is held by '
          f'{employees[position].capitalize()}')

print(employees.items())

for position, name in employees.items():
    print(f'The {position.upper()} is held by {name.capitalize()}')
'''

my_list = [('a', 'b'), ('c', 'd'), (1, 2)]

# for item in my_list:
for (item1, item2) in my_list:
    # print(item)
    # print(item1)
    # print(item2)
    print('hello')
