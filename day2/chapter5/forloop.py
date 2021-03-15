south_east = ['Imo', 'Abia', 'Anambra', 'Enugu', 'Ebonyi']

for state in south_east:
    print(state)

for n in range(6):
    print(n)

for n in range(2,6):
    print(n)

# num = 3
# x = 1
# while x <= 12:
#     result = num * x
#     print(F'{num} X {x} = {result}')
#     x += 1


# For Loop Multiplication Table
num = 3
for multiply in range(1, 13):
    result = num * multiply
    print(F'{num} X {multiply} = {result}')


states = {
    'imo' : 'Owerri',
    'Ondo' : 'Akure',
    'Osun' : 'Osogbo',
    'Kwara' : 'Ilorin',
    'Lagos' : 'Ikeja'
}

for new_state in states:
    print(F'key: {new_state}, Value: {states[new_state]}')

print('PRINTING VALUES')
for new_state in states.values():
    print(new_state)

print('PRINTING KEYS')
for new_state in states.keys():
    print(new_state)
    
print('PRINTING KEYS AND VALUE')
for new_state, new_capital in states.items():
    print(new_state, new_capital)