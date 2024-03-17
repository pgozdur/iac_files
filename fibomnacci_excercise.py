
# First solution

fibonacci_numbers = [0, 1]  # Initialize the list with the first two Fibonacci numbers

for _ in range(8):  # Compute the next 8 Fibonacci numbers
    next_number = fibonacci_numbers[-1] + fibonacci_numbers[-2]  # Compute the next number
    fibonacci_numbers.append(next_number)  # Add the next number to the list

print(fibonacci_numbers)  # Output the list of Fibonacci numbers


# Second solution 

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequence = fibonacci(n - 1)
        sequence.append(sequence[-1] + sequence[-2])
        return sequence

print(fibonacci(10))



