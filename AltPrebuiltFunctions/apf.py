import sys
# sys.path.append("C:\\Users\\shuve\\OneDrive\\Documents\\GitHub\\python-DSA\\custom_print")
# sys.path.append("C:/Users/shuve/OneDrive/Documents/GitHub/python-DSA/custom_print")
sys.path.append('..')
# from custom_print import custom_print


# 1))) Prebuild function "len()"
lst = [1, 2, 3, 4]
print(len(lst))

# Alternative or without using "len()" function.
def custom_len(sequence):
    count = 0
    for _ in sequence:
        count += 1
    return count

lst = [1, 2, 3, 4]
print(custom_len(lst))
# custom_print(custom_len(lst))



# 2))) Prebuild function "sum()"
lst1 = [1, 2, 3, 4]
print(sum(lst1))

# Alternative or without using "sum()" function.
def custom_sum(iterable):
    total = 0
    for item in iterable:
        total += item
    return total

lst1 = [1, 2, 3, 4]
print(custom_sum(lst1))



# 3))) Prebuild function "max()"
lst2 = [1, 2, 3, 4]
print(max(lst2))

# Alternative or without using "max()" function:
def custom_max(iterable):
    max_item = iterable[0]
    for item in iterable:
        if item > max_item:
            max_item = item
    return max_item

lst2 = [1, 2, 3, 4]
print(custom_max(lst2))



# 4))) Prebuild function "min()"
lst3 = [1, 2, 3, 4]
print(min(lst3))

# Alternative or without using "min()" function:
def custom_min(iterable):
    min_item = iterable[0]
    for item in iterable:
        if item < min_item:
            min_item = item
    return min_item

lst3 = [1, 2, 3, 4]
print(custom_min(lst3))



# 5))) Prebuild function "abs()"
print(abs(-5))  # Output: 5

# Alternative or without using "abs()" function:
def custom_abs(x):
    return x if x >= 0 else -x

print(custom_abs(-5))  # Output: 5



# 6))) Prebuild function "str()"
num = 123
print(str(num))  # Output: '123'

# Alternative or without using "str()" function:
def custom_str(obj):
    return obj.__str__()

num = 123
print(custom_str(num))  # Output: '123'



# 7))) Prebuild function "round()"
print(round(5.678, 2))  # Output: 5.68

# Alternative or without using "round()" function:
def custom_round(number, ndigits=None):
    multiplier = 10 ** ndigits if ndigits is not None else 1
    return int(number * multiplier + 0.5 if number > 0 else number * multiplier - 0.5) / multiplier

print(custom_round(5.678, 2))  # Output: 5.68



# 8))) Prebuild function "type()"
print(type(5))  # Output: <class 'int'>

# Alternative or without using "type()" function:
def custom_type(obj):
    return obj.__class__

print(custom_type(5))  # Output: <class 'int'>



# 9))) Prebuild function "pow()"
print(pow(2, 3))  # Output: 8

# Alternative or without using "pow()" function:
def custom_pow(base, exponent):
    return base ** exponent

print(custom_pow(2, 3))  # Output: 8



# 10))) Prebuild function "sort()"
lst4 = [2, 1, 4, 3]  
lst4.sort()
print(lst4) # Output: [1, 2, 3, 4]

# Alternative or without using "sort()" function:
def custom_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                
arr = [2, 1, 4, 3]
custom_sort(arr)
print(arr) # Output: [1, 2, 3, 4]






