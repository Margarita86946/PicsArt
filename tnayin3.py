# Create a program that extracts the first 5 characters from a given string
text = input("Enter your text: ")

print(text[:5])

# Extract the last 3 characters of a string using slicing.
print(text[:-3])

# Write a program to print every second character from a string.
print(text[1::2])

# Reverse a given string using slicing and print the result.
print(text[::-1])

# Replace all occurrences of a specific character with another character in a string.
charToReplace = input("Enter a char you want to replace: ")
replacementChar = input("Enter the new character to replace it with: ")

print(text.replace(charToReplace, replacementChar))

# Write a program to print a formatted message using f-strings.
age = int(input("Enter you age: "))
name = input("Enter your name: ")

print(f"Hello, my name is {name}and I am {age} years old.")

# Create a program to format and print a float with 2 decimal places.
number = float(input("Enter your number: "))

print(f"Formatted number: {number:.2f}")

# Write a program to convert all characters in a string to uppercase and then to lowercase.
print(text.upper())
print(text.lower())

# Create a program to count the number of occurrences of a specific character in a string.
charToCount = input("Enter a char which occurrences you want to count: ")

print(text.count(charToCount))

# Write a program to concatenate two strings with a space in between
string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

newString = " ".join([string1, string2])

print(newString)

# Create a program to find the sum of the first and last digit of a given number.
intNumber = abs(int(input("Enter your number: ")))

firstDigit = int(str(intNumber)[0])
lastDigit = intNumber % 10

print(firstDigit + lastDigit)

# Write a program to calculate the average of 3 float numbers and format the result to 3 decimal places.
float1, float2, float3 = input("Enter 3 float numbers: ").split(" ")

avgOfFloats = float(float1) + float(float2) + float(float3) / 3   // պիտի փակագծի մեջ առնես , էսպես սխալ կաշխատի

print(avgOfFloats)

# Create a program that takes a string input and an integer input and repeats the string that many times.
print(intNumber * text)

# Ask the user to enter a string, and then print the string in reverse order.
print(text[::-1])

# Count how many vowels are in the string and print the count.
vowels = ['a', 'e', 'i', 'o', 'u']
count = 0
for char in vowels:
    if char in text:
        count += 1 
print(count)

# Write a program that takes a string as input and outputs the longest substring without repeating characters.
# For example, the string "abcabcbb" should return "abc".
longest = ""
current = ""

for char in text:
    if char in current:
        current = current[current.index(char) + 1:]
    current += char
    if len(current) > len(longest):
        longest = current

print(longest)

# Write a program using a while loop that repeatedly asks the user to input a number until they input 0,
# then print the sum of all entered numbers
sum = intNumber

while num != 0:
    intNumber = int(input("Enter your number: "))
    sum += intNumber

print(sum)

# Create a list of 10 numbers (hardcoded) and calculate the sum of all numbers in the list.
import random

ls = []

for i in range(11):
    ls.append(random.randint(-100, 100)) 

print(ls)
print(sum(ls))

# Declare a list and print the value of the maximum of the elements in the list.
# The list must contain only int values. Do not use the max function.
max = ls[0]   //ստանդարտի անուն է, չենք փոխում, նույնը sum-ի համար
for num in ls:
    if num > max:
        max = num

print(max)

# Declare a list and print the index of the element with the minimum value.
print(ls.index(min(ls)))

# Declare two lists with integer values ​​and print
# the product of the elements with corresponding indices to the screen.
ls1 = []

for i in range(11):
    ls1.append(random.randint(-100, 100)) 

print(ls1)

# erb listern unen tarber lenght petqa stugel vorna metcy avelord qayler chanelu hamar
lenght = len(ls) if (len(ls) > len(ls1)) else len(ls1)  կարժի երկուարությունը պիտի ընտրվի, դա էլ փոխի

newList = []

for i in range(lenght):
    newList.append(ls[i] * ls1[i])

print(newList)

# Write a program that receives an integer. Declare a list.
# If the given number is in the list, print YES, otherwise print NO.
if intNumber in ls:
    print("YES")
else:
    print("NO")

# Declare a list consisting of strings. Print how many times each occurs in the list.
words = ["apple", "banana", "apple", "orange", "banana", "apple"]

printed = []

for word in words:
    if word not in printed:
        count = words.count(word)
        print(f"{word}: {count}")
        printed.append(word)
