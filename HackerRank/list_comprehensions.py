if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    # Using list comprehension to generate coordinates
    coordinates = [
        [i, j, k] 
        for i in range(x + 1)
        for j in range(y + 1)
        for k in range(z + 1)
        if (i + j + k) != n
    ]

    print(coordinates)


my_list = [10, 20, 30, 30, 40, 50]
print([i for i in my_list if i != 30 and i != 40]) # list comprehension

even_squares = [ i * i for i in range(100) if i%2 == 0]
print(even_squares)