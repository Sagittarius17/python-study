import sys

print(sys.path)
# print(dir(__builtins__))


import builtins

def count_builtin_functions():
    return len([name for name in dir(builtins) if callable(getattr(builtins, name))])

count = count_builtin_functions()
# print(f"Number of built-in functions in Python: {count}")



# def generator(n):
#     for i in range(n):
#         yield i**2
        
# my_gen = generator(5)

# for num in my_gen:
#     print(num)
    
    
# def fib():
#     a, b = 0, 1
    
#     while True:
#         if a > 1000:
#             break
#         yield a
#         a, b = b, a+b

# fib = fib()
# print(next(fib))
# print(next(fib))
# print(next(fib))

# for i in fib:
#     print(i)


# word = "singhahgnis"
# n = len(word)

# if word == word[::-1]:
#     print("Palindrome")
# else:
#     print("not a palindrome")
    
# x = 0
# for i in range(n):
#     if word[i] != word[n-i-1]:
#         x = 1
#         break

# if x == 0:
#     print("Palindrome")
# else:
#     print("not a palindrome")
    
    
    
arr = [1, 2, 3, 4, 5, 6, 7]
arr_len = len(arr)

for i in range(arr_len // 2):
    arr[i], arr[arr_len-1-i] = arr[arr_len-1-i], arr[i]

print(arr)


x = [3, 8, 5, 6, 4, 6, 7, 1]
n = len(x)
for i in range(n):
    for j in range(n-i-1):
        if x[j] > x[j+1]:
            x[j], x[j+1] = x[j+1], x[j]
        
print(x)


# x = 20
# y = 30

# while y != 0:
#     temp = x & y
#     x = x ^ y
#     y = temp << 1

# print(x)


# def longestCommonPrefix(self, strs: List[str]) -> s:
#     n = len(strs)
#     i = 0
#     min_lenght = float('inf')
#     for s in strs:
#         if len(s) < min_lenght:
#             min_lenght = len(s)
            
#     while i < min_lenght:
#         for s in strs:
#             if s[i] != strs[0][i]:
#                 return s[:i]
#         i += 1
#     return strs[0][:i]



from datetime import datetime, timedelta
from nsetools import Nse

def get_one_week_high_low(stock_symbol):
    nse = Nse()
    today = datetime.today().date()
    one_week_ago = today - timedelta(days=7)
    
    historical_data = nse.get_historical_data(stock_symbol, one_week_ago, today)
    
    if not historical_data:
        return "No data found for the past week."
    
    highs = [data['High'] for data in historical_data.values()]
    lows = [data['Low'] for data in historical_data.values()]
    
    one_week_high = max(highs)
    one_week_low = min(lows)
    
    return {
        'Symbol': stock_symbol,
        'One Week High': one_week_high,
        'One Week Low': one_week_low
    }

if __name__ == "__main__":
    stock_symbol = input("Enter the stock symbol (e.g., INFY, RELIANCE): ").upper()
    result = get_one_week_high_low(stock_symbol)
    print(result)
