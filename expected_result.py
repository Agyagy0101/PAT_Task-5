# List of numbers
data = [10, 501, 22, 37, 100, 999, 87, 351]

# Filter numbers greater than 4 using a lambda function
result = filter(lambda x: x > 4, data)

# Convert the filter object to a list and print it
print(list(result))

#result
[10, 501, 22, 37, 100, 999, 87, 351]
