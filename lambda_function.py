# Sample list containing different types of elements
data = [1, 'hello', 3, 'world', 5.5, 10, 'Python']

# Use map with a lambda function to classify each element as Integer, String, or Other
result = list(map(lambda x: 'Integer' if isinstance(x, int) else 'String' if isinstance(x, str) else 'Other', data))

# Print the resulting classification list
print(result)
