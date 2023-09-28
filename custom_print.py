# Simplified version of the python "print()" function.
import sys

def custom_print(*objects, sep=' ', end='\n', file=sys.stdout):
    # Convert all objects to string
    output = sep.join(map(str, objects)) + end
    file.write(output)


list = [0, 1, 2, 3, 4, 5, 6]
print(list)
custom_print(list)