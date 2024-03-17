squares = []
for number in range(10):
    squares.append(number * number)

print(squares)



# The list comprehension equivalent of the above code is:

squares = [number * number for number in range(10)]
print(squares)

# The list comprehension syntax is:
#   [expression for item in iterable] # without condition
#   [expression for item in iterable if condition]  # with condition
