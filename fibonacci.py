from functools import reduce

# Lambda function to generate a Fibonacci series up to 'n' elements
fibonacci = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [1, 1])

# Print Fibonacci series of 50 elements
print(fibonacci(50))
