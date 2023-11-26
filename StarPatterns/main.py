def print_right_triangle(rows):
    for i in range(1, rows + 1):
        print('* ' * i)

# Example usage:
print_right_triangle(5)

'''
output: 

*
* *
* * *
* * * *
* * * * *
'''



def print_inverted_right_triangle(rows):
    for i in range(rows, 0, -1):
        print('* ' * i)

# Example usage:
print_inverted_right_triangle(5)

'''
output:

* * * * *
* * * *
* * *
* *
*
'''



def print_pyramid(rows):
    for i in range(1, rows + 1):
        print(' ' * (rows - i) + '* ' * i)

# Example usage:
print_pyramid(5)

'''
output:

    *
   * *
  * * *
 * * * *
* * * * *
'''




def print_diamond(rows):
    for i in range(1, rows + 1):
        print(' ' * (rows - i) + '* ' * i)
    for i in range(rows - 1, 0, -1):
        print(' ' * (rows - i) + '* ' * i)

# Example usage:
print_diamond(5)

'''
output:

    *
   * *
  * * *
 * * * *
* * * * *
 * * * *
  * * *
   * *
    *
'''