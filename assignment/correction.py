# 1. Create a function thats gives you the average of numbers
#    in any list. Do not use the python inbuilt sum and average
#    funtion to achieve this.


def my_avg(data):
    total = 0
    for n in data:
        total += n
    av = total/len(data)
    return av

data1 = [5, 10, 15, 20, 25, 30]
data2 = [10, 20, 30, 40, 50 , 60]

print(my_avg(data1))
print(my_avg(data2))

# 2. Create a funtion that returns the multiplication table of any
#    number passed to it

def multiplication(number, start=1, stop=12):
    for start in range(start, stop+1):
        result = number * start
        print(f'{number} X {start} = {result}')

print('2 times')
multiplication(2, 5, 12)
print('3 times')
multiplication(3)

# 3. Use Lamda and List comprehension to create a 
# function that can add numbers from a lower limit 
# to an upper limit. Call this 
# functon three times with different values

# add_range = lambda start, stop: total = 0  [ start for start in range(start, stop+1) total += start ]


