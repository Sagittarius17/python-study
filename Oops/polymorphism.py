# Polymorphism allows objects of different classes to be treated as objects of a common superclass. 
# It enables you to write code that can work with objects of different types.

class Bird:
    def speak(self):
        pass

class Parrot(Bird):
    def speak(self):
        return "Polly wants a cracker"

class Duck(Bird):
    def speak(self):
        return "Quack!"

def describe_bird(bird):
    print(f"This bird says: {bird.speak()}")

parrot = Parrot()
duck = Duck()

describe_bird(parrot)  # Output: "This bird says: Polly wants a cracker"
describe_bird(duck)    # Output: "This bird says: Quack!"
