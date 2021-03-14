# Area Of a Cirle
half = 0.5
base = 100
height = 50
areaOfACircle = half * base * height
print(areaOfACircle)

# Peremeter Of a Rectangle
num = 2
lenght = 200
breaht = 100
peremeter = num * (lenght + breaht)
print(peremeter)


# I am Ransom, from Houston and married with 4 children and i earn 3500.99 as salary
# where Ransom, 4, Houston and 3500.99 are variables. 

name = 'Ransom'
children = 4
convert_children = str(children)
resident = 'Houston'
salary = 3500.99
convert_salary = str(salary)

print ('I am'+' '+name+', from'+' '+resident+' and married with'+' '+str(children)+' children and i earn'+' '+convert_salary+' as salary')

result = 'I am {}, from {} and married with {} children and i earn {} as salary'.format(name, resident, children, salary)
result2 = f'I am {name}, from {resident} and married with {children} children and i earn {salary} as salary'
print(result2)
