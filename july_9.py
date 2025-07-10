# Write a function named greet that prints "Hello, World!". Call the function.
def greet():
    print("Hello, World!")

greet()

# Write a function add that takes two numbers as arguments and returns their sum.
# Call the function with different inputs.
def add(x, y):
    return x + y

print(add(5, 9))
print(add(-1, 10))

# Create a function Create a function multiply that takes two numbers and returns their product.
def multiply(x, y):
    return x * y

print(multiply(22, 4))

# Write a function personal_greet that takes a name as an argument and prints "Hello, [name]!".
def personalGreet(name):
    print(f"Hello, {name}!")

personalGreet()

# Write a function calculate_area that takes length and width as parameters and returns the area of a rectangle.
def calculateArea(length, width):
    return length * width

print(calculateArea(5, 10))

# Write a function greet_with_message that takes a name and an optional message.
# The default message should be "Welcome!".
def greetWithMessage(name, massage = "Welcome!"):
    print(f"{name} {massage}")

greetWithMessage("Alice")
greetWithMessage("Bob", "Good morning!")

# Write a function power that takes a number and an optional exponent.
# The default exponent should be 2 (square the number).
def power(number, exponent = 2):
    return pow(number, exponent)

print(power(3))
print(power(3, 3))

# Write a program with a global variable x.
# Create a function that changes the value of x inside the function and prints both the global and local values.
x = 7

def modifyVariable():
    x = 8

    print("Local x:", x)

modifyVariable()
print("Global x:", x)

# Write a function is even that takes a number and returns True if the number is even and False otherwise.
def isEven(number):
    isEven = number % 2 == 0

    return isEven

print(isEven(4))
print(isEven(5))

# Write a function find_max that takes two numbers and returns the larger of the two.
def findMax(x, y):
    maximum = x if x > y else y

    return maximum

print(findMax(10, 20))

# Write a function calculate_discount that takes a price and a discount percentage
# and returns the discounted price.
def calculateDiscount(price, discount):
    return price - (price * discount) / 100

print(calculateDiscount(100, 20))

# Write a function filter_positive that takes a list of numbers
# and returns a new list containing only the positive numbers.
def filterPositive(numbers):
    filtered = []

    for number in numbers:
        if number > 0:
            filtered.append(number)

    return filtered

print(filterPositive([-5, 3, -1, 2, 0]))

# Write a function count_digits that takes an integer and returns the number of digits in it.
def countDigits(number):
    count = 0

    while number != 0:
        number //= 10
        count += 1

    return count

print(countDigits(12345))

# Write a function sum_of_digits that calculates the sum of all digits in an integer
def sumOfDigits(number):
    sumOfDigits = 0

    while number != 0:
        sumOfDigits += number % 10
        number //= 10

    return sumOfDigits

print(sumOfDigits(123))