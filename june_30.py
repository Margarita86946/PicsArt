# Write a program that takes a sentence and creates a dictionary where each word is a key,
# and the value is the number of times that word appears.
# Use a sample sentence and break it into words to fill the dictionary.
text1 = input("Enter you text: ").split()

dict1 = {}

for i in text1:
    if i not in dict1:
        dict1[i] = text1.count(i)

print(dict1)

# Create a dictionary to store student names as keys and their scores as values.
# Use a few sample names and scores to populate the dictionary.
# Print out each student's name and score on a new line.
studentsScores = {
    "Ani": 85,
    "Gor": 92,
    "Arman": 78,
    "James": 90,
    "Nare": 88
}

for name, score in studentsScores.items():
    print(f"{name}: {score}")

# Create a dictionary that maps numbers from 1 to 5 to their word equivalents (e.g., {1: "one", 2: "two", ...)).
# Use this dictionary to convert a list of numbers into words and print each word on a new line.
dict2 = { 
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five" 
}

list1 = [1, 2, 3, 4, 5]

for i in list1:
    if i in dict2:
        print(dict2[i])

# Create a dictionary to represent a store's inventory with items as keys and quantities as values.
# Print the quantity of a specific item (e.g., "Apples").
# Update the quantity of an item and print the dictionary to show the change.
dict3 = {
    "bread": 30,
    "milk": 20,
    "eggs": 50,
    "apples": 15,
    "sugar": 10 
}

print(dict3["apples"])

dict3["sugar"] = 40

print(dict3)

# Write a program that takes a sentence and uses a set to find all unique words.
# Print each unique word on a new line.
text2 = input("Enter you text: ").split()

uniqueWords1 = set()

for i in text2:
    uniqueWords1.add(i.strip(".,!?;:'\"()[]{}"))

for i in uniqueWords1:
    print(i)

# Given two lists of numbers, use sets to find and print the common elements between them.
list2 = [2, 4, 6, 8, 10, 12]
list3 = [3, 6, 9, 12, 15]

set1 = set(list2)
set2 = set(list3)

common = set1 & set2

print(common)

# Given a list of numbers, use a set to find any duplicates in the list and print them.
# You can add numbers to a set one by one and check if they are already present.
list4 = [1, 2, 2, 3, 4, 4, 5]

set3 = set()
set4 = set()

for i in list4:
    if i in set3:
        set4.add(i)
    else:
        set3.add(i)

print(set4)

# Use a set to create a list of vocabulary words from a paragraph. Break the paragraph into individual words,
# add each word to the set, and print the final set of unique words.
text3 = input("Enter your text: ").split()

uniqueWords2 = set()

for i in text3:
    uniqueWords2.add(i.strip(".,!?;:'\"()[]{}"))

print(uniqueWords2)

# Declare two sets. Print their union, intersection, and symmetric difference.
set5 = {1, 2, 3, 4}
set6 = {3, 4, 5, 6}

print(set5 | set6)
print(set5 & set6)
print(set5 ^ set6)

# Declare two arrays. Both arrays are the same except that one array contains one element more.
# Find that element.
list5 = [1, 2, 3, 4]
list6 = [1, 2, 3]

set7 = set(list5)
set8 = set(list6)

print(set7 ^ set8)

# Write a program that will receive two sets and return True if one is a subset of the other, False otherwise.
set9 = {3, 4}
set10 = {3, 4, 5, 6}

isSubset = set9.issubset(set10) or set10.issubset(set9)

print(isSubset)

# Declare a set consisting of integers.
# Delete all odd numbers in the set, and add a given number of even numbers.
set11 = {1, 2, 3, 4, 5, 6, 7, 8, 9}

oddCount = 0
newSet = set()

for i in set11:
    if i % 2 == 0:
        newSet.add(i)
    else:
        oddCount += 1

start = 2
countToAdd = 0

while countToAdd != oddCount:
    if start not in newSet:
        newSet.add(start)
        countToAdd += 1
    start += 2

print(newSet)

# Implement a program that will accept a sentence from the user and return the same sentence,
# but replace all spaces with commas.
text4 = input("Enter your text: ")
replacedText = ""

for i in text4:
    if i == " ":
        replacedText += ","
    else:
        replacedText += i

print(replacedText)

# Implement a program that will accept a word from the user and print that word in reverse.
text5 = input("Enter your text: ")
reversedText = ""

for i in range(len(text5)-1, -1, -1):
    reversedText += text5[i]

print(reversedText)

# Implement a program that will accept a sentence from the user and count how many words are in that sentence.
text6 = input("Enter your text: ")

count = 0 

for i in range(len(text6) - 1):
    if text6[i] != " " and text6[i + 1] == " ":
        count += 1

if len(text6) > 0 and text6[-1] != " ":
    count += 1

print(count)

# Implement a program that will take a sentence and capitalize the first letter of each word.
text7 = input("Enter your text: ")

result = ""
makeUpper = True

for ch in text7:
    if makeUpper and 'a' <= ch <= 'z':
        result += chr(ord(ch) - 32)
        makeUpper = False
    else:
        result += ch
        if ch == ' ':
            makeUpper = True
        else:
            makeUpper = False

print(result)

# Implement a program that prints the maximum value in a list
list7 = [12, 5, 91, 3, 44]

maximum = list7[0]

for i in list7:
    if i > maximum:
        maximum = i

print(maximum)

# Implement a program that prints the minimum value in a list.
list8 = [8, -2, 5, 0, 3]

minimum = list8[0]

for i in list8:
    if i < minimum:
        minimum = i

print(minimum)

# Implement a program that prints the number of even elements in a list.
list9 = [1, 4, 7, 8, 10, 11]

count = 0 

for i in list9:
    if i % 2 == 0:
        count += 1

print(count)

# Implement a program that will create a new list containing only the positive numbers from the original list.
list10 = [-3, 4, 0, -1, 9]
positiveList = []

for i in list10:
    if i > 0:
        positiveList = positiveList + [i] 

print(positiveList)