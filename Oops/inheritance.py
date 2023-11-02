# Inheritance allows a class to inherit attributes and methods from another class. 
# It promotes code reuse and establishes a relationship between classes.

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

my_dog = Dog()
my_cat = Cat()

print(my_dog.speak())  # Output: "Woof!"
print(my_cat.speak())  # Output: "Meow!"
