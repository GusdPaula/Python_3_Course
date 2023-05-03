# Lambda function

def ex(function, *args):
    return function(*args)


print(ex(lambda x, y: x + y, 2, 3))

d = (ex(lambda m: lambda n: n * m, 2)) # lambda inside lambda is not recomended

print(d(2))
print()
print()

# List Comprehension and Mapping and Filter

numbers = [1, 2, 3, 4, 5]

division = [
            # Mapping
            number / 2 if number > 2 else number 
            # List comprehension
            for number in numbers
            # Filter
            if number > 1
            ]

print(numbers)
print(division)

print()
print()

rows_columns = [(x, y) for x in range(1,11) for y in range(1, 6)]

print(rows_columns)