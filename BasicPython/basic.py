# 1))) Data Types and Variables

string_var = "Hello, World!"
integer_var = 10
float_var = 20.5
list_var = [1, 2, 3, 4, 5]
tuple_var = (1, 2, 3, 4, 5)
dict_var = {"name": "John", "age": 30}



# 2))) Control Structures
# Conditional:
age = 18
if age < 18:
    print("Minor")
elif age == 18:
    print("Just turned adult")
else:
    print("Adult")
    
# Loop:
# For Loop
for i in range(5):
    print(i)

# While Loop
count = 0
while count < 5:
    print(count)
    count += 1
    
    
    
# 3))) Functions
def greet(name):
    return "Hello, " + name + "!"

message = greet("Alice")
print(message)



# 4))) List Comprehensions
numbers = [1, 2, 3, 4, 5]
squared_numbers = [n ** 2 for n in numbers]
print(squared_numbers)



# 5))) Lambda Functions and Map
numbers = [1, 2, 3, 4, 5]
doubled_numbers = list(map(lambda x: x*2, numbers))
print(doubled_numbers)



# 6))) File Handling
with open('sample.txt', 'w') as file:
    file.write("Hello, World!")

with open('sample.txt', 'r') as file:
    content = file.read()
    print(content)
    
    
    
# 7))) Error Handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")
    
    
    
# 8))) Classes and Objects
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return "Woof!"

fido = Dog("Fido")
print(fido.name)
print(fido.bark())



# 9))) Modules
# If you have a file named math_operations.py with content:

# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# # You can import and use it as:

# from math_operations import add, subtract

# print(add(5, 3))
# print(subtract(5, 3))



# 10))) Dictionaries and Iterating
person = {"name": "John", "age": 30, "city": "New York"}

for key, value in person.items():
    print(key, ":", value)



# 11))) String Manipulation
s = "hello"
print(s.capitalize())  # Hello
print(s.replace('l', '(ell)'))  # he(ell)(ell)o



# 12))) Sets
primes = {2, 3, 5, 7}
odds = {1, 3, 5, 7, 9}
print(primes & odds)  # Intersection: {3, 5, 7}
print(primes | odds)  # Union: {1, 2, 3, 5, 7, 9}



# 13))) Generators and Iterators
def generate_numbers(n):
    for i in range(n):
        yield i

gen = generate_numbers(3)
print(next(gen))  # 0
print(next(gen))  # 1



# 14))) Decorators
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()



# 15))) List Slices
nums = [0, 1, 2, 3, 4]
print(nums[2:4])    # [2, 3]
print(nums[2:])     # [2, 3, 4]
print(nums[:2])     # [0, 1]
print(nums[:])      # [0, 1, 2, 3, 4]
print(nums[:-1])    # [0, 1, 2, 3]
nums[2:4] = [8, 9]  # replace sub-parts
print(nums)         # [0, 1, 8, 9, 4]



# 16))) Built-in Functions
# Some important built-in functions include abs(), len(), type(), isinstance(), range(), input(), enumerate(), zip(), etc.

for index, value in enumerate(['a', 'b', 'c']):
    print(index, value)
    
    
    
# 17))) Command Line Arguments (using sys)
import sys
script_name = sys.argv[0]
first_arg = sys.argv[1]
    
    
    
# 18))) Regular Expressions (using re)
import re
pattern = re.compile(r"\d{3}-\d{2}-\d{4}")
match = pattern.match("123-45-6789")
if match:
    print("Valid SSN")
    
    

# 19))) Dunder (Magic) Methods
# These are special methods in Python classes that start and end with double underscores, e.g., __init__, __str__, __len__.
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"

book = Book("1984", "George Orwell")
print(book)
    
    
    
# 20))) Working with Date and Time (using datetime)
from datetime import datetime
now = datetime.now()
print(now.strftime('%Y-%m-%d %H:%M:%S'))



# 21))) Understanding Scope and Namespace
x = 10  # Global variable

def foo():
    x = 5  # Local variable
    print(x)

foo()    # prints 5
print(x)  # prints 10



