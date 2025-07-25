# Write a function print_down_from_n(n) that prints numbers from n to 1 using recursion.
def print_down_from(n):
    if n < 1 or not isinstance(n, int):
        return
    print(n)
    print_down_from(n-1)
    
print_down_from(5)

# Write a function print_characters(s) that prints each character of a string on a new line using recursion.
def print_charecters(s):
    if not s or not isinstance(s, str):
        return
    print(s[0])
    print_charecters(s[1:])
    
print_charecters("hello")

# Write a recursive function to calculate the factorial of a number n.
def factorial(n):
    if not isinstance(n, int) or n < 0:
        return

    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(-10))

# Create a recursive function to find the sum of the first n natural numbers.
def sum_of_numbers(n):
    if not isinstance(n, int) or n < 0:
        return

    if n == 0:
        return 0
    else:
        return n + sum_of_numbers(n - 1)

print(sum_of_numbers(4))

# Write a recursive function to reverse a given string
def reverse_string(s):
    if not isinstance(s, str):
        return
    
    if not s:
        return ""
    else:
        return s[-1] + reverse_string(s[:-1])
    
print(reverse_string("hello"))

# Write a recursive function to check if a string is a palindrome.
def is_palindrome(s):
    if not isinstance(s, str):
        return
    
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])
    
print(is_palindrome("racecar"))

# Write a recursive function to calculate the power of a number x raised to n.
def power(x, n):
    if not isinstance(x, int) or not isinstance(x, int) or n < 0:
        return
    
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)
    
print(power(3, 3))

# Write a recursive function to calculate the sum of all digits in a number.
def sum_of_digits(n):
    if not isinstance(n, int) or n < 0:
        return
    
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)

print(sum_of_digits(456))
