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
