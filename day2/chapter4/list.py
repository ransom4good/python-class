person = ['Ransom', 45, True, "Fair"]

# True and False are written in capital T and F
print(f'My name is {person[0]}, I am {person[1]} years old and {person[3]} in complextion')

# Adding to the end of the list
person.append('Developer')
print(person)

# Change item on a list
person[2] = False
print(person)

# Adding an item @ a specified index
person.insert(1, "Dark Hair")
print(person)

# Create a list that will hold username and password
# and create two password fields check if the first password is greater or lesser than 7 then display
# an error message and another error message if the two password fields do not match
# if it matches then chnage the password in the list to
# a new one and display success message. 

user_db = ['Ransom', 'password']
password = input('Enter Password: ')
confirm_password = input('Enter Confirm Passowrd: ')

if len(password.lower()) < 7:
    print('Password is too short')
elif password.lower() != confirm_password.lower():
    print('Passwords do not match')
else:
    user_db[1] = password.lower()
    print('Password changed successfully')
print(user_db)