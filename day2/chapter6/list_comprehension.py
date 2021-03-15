numbers = []

for n in range(1, 12):
    numbers.append(n)
print(numbers)

print('Using List Comprehension')

numbers = [n for n in range(1, 12)]
print(numbers)

# for even numbers
even_numbers = []

for n in range(1, 12):
    if n % 2 == 0:
        even_numbers.append(n)
print(even_numbers)

print('Using List comprehension')

even_numbers = [n for n in range(1, 12) if n % 2 == 0]
print(even_numbers)


def print_even_default(stop, start=1):
    while start <= stop:
        if start % 2 == 0:
            print(start)
        start += 1

print(print_even_default)
print_even_default(16, 4)


print('With Lambda and List Comprehension')
print_lambda_even = lambda start, stop:[start for start in range(start, stop) if start % 2 == 0]
print(print_lambda_even(1, 10))