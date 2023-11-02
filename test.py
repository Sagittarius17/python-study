import sys

print(sys.path)
print(dir(__builtins__))


import builtins

def count_builtin_functions():
    return len([name for name in dir(builtins) if callable(getattr(builtins, name))])

count = count_builtin_functions()
print(f"Number of built-in functions in Python: {count}")

