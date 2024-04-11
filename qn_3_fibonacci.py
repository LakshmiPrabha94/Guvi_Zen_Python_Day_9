#Name: Lakshmi Prabha
#Program : Using python lambda function create a fibbonaccie series from 1 to 50 elements
#Version: 1
#Pragramming language: Python
#Python Version: 3.12.0

# Function to generate Fibonacci series up to 'n' elements
def fibonacci_series(n):
    series = [0, 1]
    for i in range(2, n):
        series.append(series[-1] + series[-2])
    return series

# Function to calculate Fibonacci number using the previous two numbers
calculate_fibonacci = lambda x: fibonacci_series(x)[-1] + fibonacci_series(x)[-2]

# Number of elements in the Fibonacci series
num_elements = 50

# Generate Fibonacci series up to 'num_elements' without list comprehension
fib_series = fibonacci_series(num_elements)

for i in range(2, num_elements):
    fib_series.append(calculate_fibonacci(i))

# Print the generated Fibonacci series
print("Fibonacci Series ({} elements):".format(num_elements))
print(fib_series)
