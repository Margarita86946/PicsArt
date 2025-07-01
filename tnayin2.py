import fractions
import decimal

# Write a program that prompts the user to create an empty list.
# Then, the user should be able to add elements to the list using three different methods: append(), extend(), and insert().
ls = []

forAppend = input("Enter element: ")
ls.append(forAppend)

forExtend = input("Enter elements: ").split(" ")
forExtendInt = list(map(int, forExtend))
ls.extend(forExtendInt)

forInsert = input("Enter position and element: ").split(" ")
ls.insert(int(forInsert[0]), float(forInsert[1]))

print("Final list:", ls)

# Extend the previous program to allow the user to remove elements using two methods: remove() and pop().
forRemove = input("Enter the number to remove: ")
ls.remove(forRemove)

forPop = int(input("Enter the index to remove: "))
ls.pop(forPop)

print(list)

# Write a program to create a list and a tuple with some elements. Print them and display their types.
list = [1, 30, 'hello', 6.5]
print(list)
print(type(list))

tuple = ('oops', 0.0023, 23)
print(tuple)
print(type(tuple))

# Write a program to count the occurrences of a specific element in a list and tuple.
elementToFind = 1
print(list.count(elementToFind))
print(tuple.count(elementToFind))

# Write a program to find and print the maximum and minimum values a list and a tuple.
myList = [2, 5, 1]
print(f"Max element: {max(myList)}\nMin element: {min(myList)}")

myTuple = [22, 10, 45]
print(f"Max element: {max(myTuple)}\nMin element: {min(myTuple)}")

# Write a program to access elements from a nested list and a nested tuple
nastedList = [[1,2,3]]
print(nastedList[0][1])

nastedTuple = ([3, 4], (5, 6, 7))
print(nastedTuple[1][2])

# Write a program to find the sum of all elements in a list and a tuple.
print(sum(myList))
print(sum(myTuple))

# Write a program to reverse a list and a tuple.
myList.reverse()
print(myList)
print(tuple(reversed(nastedTuple)))

# Create a program that adds, subtracts, multiplies,
# and divides two integers, two floats, and a combination of both
int1 = 12
int2 = 7
print(int1 + int2) 
print(int1 - int2)
print(int1 * int2)
print(int1 / int2)

float1 = 7.6563
float2 = 20.422
print(float1 + float2)
print(float1 - float2)
print(float1 * float2)
print(float1 / float2)

print(int1 + float2)
print(int1 - float2)
print(int1 * float2)
print(int1 / float2)

# Write a program to calculate the product of two complex numbers.
comp1 = 2j
comp2 = 5 + 3j
print(comp1 * comp2)

# Create a fraction that represents 1/2 and another fraction representing 2/3.
# Add them and print the result.
frac1 = fractions.Fraction(1, 2)
frac2 = fractions.Fraction(2, 3)
print(frac1 + frac2)

# Using decimal, calculate the sum of 0.1 and 0.2 and compare it with float.
float1 = 0.1
float2 = 0.2

dec1 = decimal.Decimal(0.1)
dec2 = decimal.Decimal(0.2)

print(float1 + float2)
print(dec1 + dec2)

# Write a program to check if the sum of three numbers is equal to 100.
# Use boolean comparisons to print the result as True or False.
numbers = input("Enter 3 numbers: ").split(" ")
intNumbers = list(map(int, numbers))

isEqual = sum(intNumbers) == 100

print(isEqual)

# Accept two fractions from the user (in the form of a/b where both a and b are integers) and multiply them.
# Use the fractions. Fraction class to handle fractions and print the resulting fraction in its simplified form.
import fractions
import math
num1, den1 = input("Enter first fraction: ").split("/")
num2, den2 = input("Enter second fraction: ").split("/")

frac1 = fractions.Fraction(int(num1), int(den1))
frac2 = fractions.Fraction(int(num2), int(den2))

print(frac1 * frac2)

# Accept two fractions from the user and find their GCD using the math.gcd()
# function along with the numerator and denominator attributes of each fraction.
gcdNumerator = math.gcd(frac1.numerator, frac2.numerator)
gcdDenominator = math.gcd(frac1.denominator, frac2.denominator)

print(gcdDenominator, gcdNumerator)

# Write a program to check if a number is even or odd.
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Compare the values of a float and an int and print whether they are equal or not.
# Input from user
intValue = int(input("Enter an integer: "))
floatValue = float(input("Enter a float: "))

if intValue == floatValue:
    print("Equal")
else:
    print("Not equal")

# Calculate the square of an integer and a float using the exponentiation operator (**).
print(intValue ** 2)
print(floatValue ** 2)

# Write a program to find the maximum of three numbers using nested conditional operators.
a = int(input("Enter a number: "))
b= int(input("Enter a number: "))
c = int(input("Enter a number: "))

maximum = a if (a > b and a > c) else (b if b > c else c)

print(maximum)

# Accept two integer inputs from the user and calculate the absolute difference
# between them using the abs() function.
# Print the result.
print(abs(a - b))

# Accept an integer input from the user and use conditional statements
# to print whether the number is positive, negative, or zero.
if a > 0:
    print("positive")
elif a < 0:
    print("negative")
else:
    print("zero")

# Accept two integer inputs from the user.
# Check if the first number is a multiple of the second and print True if it is, otherwise print False.
isMultiple = a % b == 0

print(isMultiple)