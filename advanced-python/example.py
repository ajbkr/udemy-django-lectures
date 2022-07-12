# print('hello)

try:
    # print('hello')
    # raise IOError('Aaaarrrggh!')
    print('10' + 10)
    # print(10 + 10)
# except:
except IOError:
    print('You have an input/output error')
    print('Did you check the file permissions?')
except TypeError:
    # print('error!')
    print('You are using the wrong data types!')
except:  # noqa
    print('hey you got an error')
# else:
    # print('ELSE BLOCK RAN')
finally:
    print('FINALLY WILL ALWAYS RUN, ERROR OR NO ERROR!')
