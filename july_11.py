# Write a function is palindrome that takes a string
# and returns True if it is a palindrome (reads the same forward and backward), otherwise False.
def isPalindrome(string):
    newString = string.lower()
    isPalindrome = newString == newString[::-1]

    return isPalindrome

print(isPalindrome ("Radar"))
print(isPalindrome ("hello"))

# Write a function celsius_to_fahrenheit that takes a temperature in
# Celsius and returns the temperature in Fahrenheit. Formula: F = C * 9/5 +32
def celsiusToFahrenheit(tempreture):
    F = tempreture * 9/5 + 32

    return F

print(celsiusToFahrenheit(0))
print(celsiusToFahrenheit(100))

# Write a function repeat_string that takes a string and an integer n, and returns the string repeated n times.
def repeatString(string, integer):
    return string * integer

print(repeatString("Hi", 3))

# Write a function average_list that takes a list of numbers and returns their average.
def averageList(numbers):
    return sum(numbers) / len(numbers)

print(averageList([10, 20, 30]))

# Write a function factorial that takes a non-negative integer and returns its factorial
import math

def factorial(number):
    return math.factorial(number)

number = abs(int(input("Enter your number: ")))

print(factorial(number))

# Write a function greet_many that takes a list of names and prints "Hello, [name]!" for each name.
def greetMany(names):
    for name in names:
        print(f"Hello, {name}!")

greetMany(["Anna", "Ben", "Charlie"])

# Write a function reverse_number that takes an integer and returns its digits reversed.
def reverseNumber1(number):
    sign = -1 if number < 0 else 1
    number = abs(number)
    strNumber = str(number)

    return sign * int(strNumber[::-1])

print(reverseNumber1(1234)) 
print(reverseNumber1(-5678)) 

def reverseNumber2(number):
    reversedNum = 0
    sign = -1 if number < 0 else 1
    number = abs(number)

    while number > 0:
        digit = number % 10
        reversedNum = reversedNum * 10 + digit
        number = number // 10

    return sign * reversedNum

print(reverseNumber2(1234))
print(reverseNumber2(-5678))

# Write a function count_vowe1s that takes a string and returns the number of vowels (a, e, i, o, u) in it.
def countVowels(string):
    vowels = ("a", "e", "i", "o", "u")
    count = 0

    for char in string:
        if char in vowels:
            count += 1

    return count

print(countVowels("hello"))