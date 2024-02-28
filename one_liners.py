# Normal syntax for defining a function
def add(a, b):
    return a + b
print(add(3, 8))

# Normal syntax for a loop
for i in range(5):
    print(i)

# Normal syntax for if-else statement
if 5 > 3:
    print("Condition is true")
else:
    print("Condition is false")

# Normal syntax for list comprehension
result = []
for i in range(5):
    result.append(i * 2)
print(result)



# One-line syntax for defining a function
add = lambda a, b: a + b
sum = add(3, 8)
print(sum)

# One-line syntax for a loop
[print(i) for i in range(5)]

# One-line syntax for if-else statement
print("Condition is true") if 5 > 3 else print("Condition is false")

# One-line syntax for list comprehension
print([i * 2 for i in range(5)])
