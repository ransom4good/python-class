a = 5
b = 3
if a > b:
    print('a is greater than b')
else:
    print('wrong component')
    # elif is the same as else if in javascript

a = 3
b = 5
if a > b:
    print('a is greater than b')
elif a == b:
    print('a is equal to b')
elif a != b:
    print('a is not equal to b')
elif a < b:
    print('a is less than b')
else:
    print('No answer')


name = 'Ransom'
if name.isalpha():
    if len(name) > 5:
        print('Hello World')
    else:
        print('your character is less than 5')
else:
    print('Your data is not an alphabet')