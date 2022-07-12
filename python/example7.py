'''
#if True:
if False:
  print('True!')
  print('another statement')
'''

password = 'mypassword'
# password = 'mypasswordsdsd'
stored_pw = 'mypassword'
# some_condition = password == stored_pw
admin = True
# admin = False

# if some_condition:
if password == stored_pw:
    print('passwords match!')
elif admin:
    print('passwords did not match, but ADMIN granted')
else:
    print('no password match and not an admin!')
