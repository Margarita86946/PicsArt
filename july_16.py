# Write a function fibonacci(n) that calculates the n-th Fibonacci number without using recursion.
# Use an iterative approach to compute the result.
def fibonacci(n):
    if  n < 0 or not isinstance(n, int):
        print("Wrong n.")
        return

    a , b = 0, 1
    for _ in range(n):
        a, b = b, a + b

    print(a)

fibonacci(10)

# Write a function factorial(n) that calculates the factorial of a given number using an iterative approach.
def factorial(n):
    if n < 0 or not isinstance(n, int):
        print("Wrong n.")
        return
    
    res = 1

    if n == 0:
        print(res)
    else:
        while n != 1:
            res *= n
            n -= 1

        print(res)

factorial(10)

# Write a function is_prime(n) that checks if a number is a prime number using a loop.
# The function should return True if the number is prime and False otherwise.
def is_prime(n):
    if n <= 0 or not isinstance(n, int):
        print("Wrong n.")
        return
    
    if n < 2:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

print(is_prime(1))

# Write a function reverse_string(s) that reverses a string without using slicing or built-in functions like reversed().
# Use a loop to construct the reversed string
def reverse_sring(s):
    if not isinstance(s, str):
        print("s is not a string")
        return

    reversed_sring = ""

    for i in range(len(s) - 1, -1, -1):
        reversed_sring += s[i]

    print(reversed_sring)

reverse_sring("barev")

# Implement a function that takes a number and returns the sum of its digits.
def sumOfDigits(number):
    if not isinstance(number, int):
        print("number is not an integer")
        return
    
    if number < 0:
        number = abs(number)

    sumOfDigits = 0

    while number != 0:
        sumOfDigits += number % 10
        number //= 10

    print(sumOfDigits)

sumOfDigits(-123)

# Implement a function that returns an int value that returns 1 if the integer passed to the function
# can be expressed as the sum of two prime numbers, otherwise the function will return 0.
def is_sum_of_two_primes(n):
    if not isinstance(n, int) or n < 0:
        return 0
    
    for i in range(2, n // 2 + 1):
        if is_prime(i) and is_prime(n - i):
            return 1
    
    return 0
    
# Implement a function that has the following prototype def power (num: int, exp: int).
# The function returns the value of the power exp of the integer num.
def power(num, exp):
    if not isinstance(num, int) or not isinstance(exp, int):
        print("Wrong number or exponent.")
        return

    if exp < 0:
        num = 1 / num
        exp = abs(exp)
    elif exp == 0:
        return 1

    res = 1

    for _ in range(exp):
        res *= num

    print(res)

power(2,-2)

# Enter a number, print the digits of the number separately on a separate screen.
# For example, for the entered number 5479, print '5', '4', '7', '9'.
def number_separator(number):
    if not isinstance(number, int):
        print("Number is not an integer.")
        return
    
    if number < 0:
        number = abs(number)

    ls = []
    
    while number != 0:
        ls.append(number % 10)
        number //= 10
    
    ls.reverse()
    print(ls)

number_separator(1234)