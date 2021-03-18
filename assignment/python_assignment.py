# assignment 
# write a program that returns even numbers from 1 to 20 using loop

# create a python list with email and password
# display an error message if email is not in the list, if the email is in the list, 
# check if the two password fields match, if it does, Change the password to a new one
# and display success message. 



# Assignment 2
#1. Create a function that gives you the sum of numbers in a list. Do not use the Pythin inbuilt function
#2. Create a function that returns the multiplication table of any number passed to it
#3. Use Lambda and list comprehension to create a function that can add numbers from lower limit to an upper limit. 
#   call this function three times with different values.  


# Assignment 3
# 1. Create a Class called Product
#  determine what will be the class variable for the product class and create an init method with three parameters
#  for the product class, create another method that will calculate the discount prize for each product.
#  call it three times

# 2. Create a child class called shirt
# add new parameter that will be a list of sizes in the init method of the child class. 
# create a demethod that display information about this shirt class.
# access the attributes on the child class

multiply_number = int(input('Enter a number to print its multiplication table: '))

def print_table(num):
    for i in range(1, 13):
        result = num * i
        print(F'{num} X {i} = {result}')
print_table(multiply_number)






# user_email = input('Enter Email: ')
# user_pass = input('Enter Password: ')
# confirm_pass = input('Confirm Password: ')
# user_login = ['ransom2sure@gmail.com', 'password']

# if user_email != user_login[0]:
#     print('Email not found')
# elif user_pass != confirm_pass:
#     print('Password does not match')
# else:
#     user_login[1] = user_pass
#     print('Password changed successfully')
# print(user_login)



# # # Python program to print Even Numbers in given range 
# # start, end = 0, 21
# # # iterating each number in list 
# # for even in range(start, end + 1):
# # 	# checking condition 
# # 	if even % 2 == 0: 
# # 		print(num, end = " ") 


# for x in range(0, 22, 2):
#     print(x)
# else:
#     print("All Even Numbers")


# score = int(input('Enter Score: '))
# if score >=0 and score <=34:
#     grade = 'Fail'
#     print(F'Your score is {score} and this is a {grade}')
# elif score >=35 and score <=44:
#     grade = 'Pass'
#     print(F'Your score is {score} and this is a {grade}')
# elif score >=45 and score <=49:
#     grade = 'Fair'
#     print(F'Your score is {score} and this is {grade}')
# elif score >=50 and score <=59:
#     grade = 'Good'
#     print(F'Your score is {score} and this is {grade}')
# elif score >=60 and score <=69:
#     grade = 'Very Good'
#     print(F'Your score is {score} and this is {grade}')
# elif score >=70 and score <=100:
#     grade = 'Excellent'
#     print(F'Your score is {score} and this is {grade}')
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


# Multiplication Table
# num = 3
# x = 1
# while x <= 12:
#     result = num * x
#     print(F'{num} X {x} = {result}')
#     x += 1



# Sum the numbers in the list
# numbers = [10, 20, 30, 40, 70, 200, 300]
# total = 0
# x = 0

# while x < len(numbers):
#     total += numbers[x]
#     x += 1
# print('Total', total)
# print('Average', total/len(numbers))
