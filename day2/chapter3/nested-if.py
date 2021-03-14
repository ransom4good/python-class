name1 = "5656775"
name2 = "am^&hhdhj@3"

if name1.isalpha():
    if len(name1) > 8:
        print('Welcome Online')
        # Else Statement
    else:
        print('Your Character is less than 8')
else: 
    print('Your Data is not an alphabet')


# Write a method to check username and password is correct

# username = input('Enter Username: ')
# password = input('Enter Password: ')

# db_username = 'Ransom'
# db_password = 'God@123'
# # for upper and lowercase letters, make use of ".lower()"

# if username.lower() == db_username and password.lower() == db_password:
#     print('Username and password is correct')
# else:
#     print('Username and password is wrong')


# Write a program that displays an error message if username is worng or another error message if password
# is wrong also display error message 
# if both are wrong 
# and then a success message if both are correct

username = input('Enter Username: ')
password = input('Enter Password: ')

db_username = 'ransom'
db_password = 'God@123'

if username != db_username:
    print('username is wrong')
elif password != db_password:
    print('Password is worng')
elif username == db_username and password == db_password:
    print('Username and Password is correct')
                

    


