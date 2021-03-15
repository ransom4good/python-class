# assignment 
# write a program that returns even numbers from 1 to 20 using loop

# create a python list with email and password
# display an error message if email is not in the list, if the email is in the list, 
# check if the two password fields match, if it does, Change the password to a new one
# and display success message. 

user_email = input('Enter Email: ')
user_pass = input('Enter Password: ')
confirm_pass = input('Confirm Password: ')
user_login = ['ransom2sure@gmail.com', 'password']

if user_email != user_login[0]:
    print('Email not found')
elif user_pass != confirm_pass:
    print('Password does not match')
else:
    user_login[1] = user_pass
    print('Password changed successfully')
print(user_login)



# # Python program to print Even Numbers in given range 
# start, end = 0, 21
# # iterating each number in list 
# for even in range(start, end + 1):
# 	# checking condition 
# 	if even % 2 == 0: 
# 		print(num, end = " ") 


# for x in range(0, 22, 2):
#     print(x)
# else:
#     print("All Even Numbers")


# score = int(input('Enter Score: '))
# if score >=0 and score <=34:
#     print(F'Your score is {score} and you failed')
# elif score >=35 and score <=44:
#     print(F'Your score is {score} and this is a pass')
# elif score >=45 and score <=49:
#     print(F'Your score is {score} and this is fair')
# elif score >=50 and score <=59:
#     print(F'Your score is {score} and this is good')
# elif score >=60 and score <=69:
#     print(F'Your score is {score} and this is very good')
# elif score >=70 and score <=100:
#     print(F'Your score is {score} and this is excellent')
# else:
#     print(F'You have entered an invalid score number')


# number1 = int(input('Enter First Number: '))
# number2 = int(input('Enter Second Number: '))
# number3 = int(input('Enter Third Number: '))

# def smallest(num1, num2, num3):
#     if (num1 < num2) and (num1 < num3):
#         smallest_num = num1
#     elif (num2 < num1) and (num2 < num3):
#         smallest_num = num2
#     else:
#         smallest_num = num3
#     print("The smallest of the 3 number is: ", smallest_num)
# smallest(number1, number2, number3)

