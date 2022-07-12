'''
employees = {'chef': 'Amy', 'ceo': 'Jason'}
print(employees['ceo'])

employees['waiter'] = 'Mike'
print(employees)
print(employees['waiter'])

print(employees['chef'])
print('UPDATE CHEF!')
employees['chef'] = 'Jose'
print(employees['chef'])

employees['chef'] = 'Amy'
print(employees['chef'].upper())
'''

'''
stock_prices = {'GOOGL': [200, 210, 220], 'GME': [20, 100, 300]}
print(stock_prices['GOOGL'])

history = stock_prices['GOOGL']

print(f'First day price is: {history[0]}')
'''

# my_dict = {'OUTER': {'INNER': 100}}
# print(my_dict['OUTER']['INNER'])

my_dict = {'key1': 100, 'key2': 200, 'key3': 400}
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

print(my_dict['key1'])
my_dict['key1'] = '...'
my_dict['brand_new'] = 2323
print(my_dict)
