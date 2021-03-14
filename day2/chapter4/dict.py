person = {
    'username' : 'Ransom4good',
    'password' : 'pass12345',
    'active' : False,
    'first_name' : 'Ransom',
    'last_name' : 'Adekola',
    'age' : 45
}

print(person['active'])

print(person.get('last_name'))

person['username'] = 'Jonathan123'
print(person)