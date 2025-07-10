import decimal
import fractions

#xndir 1
x = int(input("Enter x: "))
y = int(input("Enter y: "))
sum = x + y
print(f"sum of x and y is: {sum}")

#xndir 2
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

comp1 = 2j
comp2 = 5 + 3j
print(comp1 + comp2)
print(comp1 - comp2)
print(comp1 * comp2)
print(comp1 / comp2)

#xndir 3, 5
dec1 = decimal.Decimal(5.3252)
frac1 = fractions.Fraction(10, -8)
frac2 = fractions.Fraction(3, 14)

print(int1 > float1)
print(int1 < float1)
print(int1 == float1)
print(int1 != float1)
print(int1 >= float1)
print(int1 <= float1)

print(dec1 > float1)
print(dec1 < float1)
print(dec1 == float1)
print(dec1 != float1)
print(dec1 >= float1)
print(dec1 <= float1)

print(frac1 > frac2)
print(frac1 < frac2)
print(frac1 == frac2)
print(dec1 != float1)
print(dec1 >= float1)
print(dec1 <= float1)

#xndir 4
print(abs(comp1), abs(comp2))

print(frac1 + frac2)
print(frac1 - frac2)
print(frac1 * frac2)
print(frac1 / frac2)

dec2 = decimal.Decimal(0.0000000009754)
print(dec1 - dec2)
print(dec1 + dec2)

#xndir 6
str1 = "Hello"
str2 = "world"
print(str1 + " " + str2)

#xndir 7
print(f"First char: {str1[0]}\nLast char: {str1[len(str1)-1]}")

#xndir 8
print(str1[:3], str1[-1:-3:-1])

#xndir 9
word1 = input("Enter your word: ")
word2 = input("Enter your word: ")
print(word1 + " " + word2)

#xndir 10
print(str1.upper(), str1.lower())

#xndir 11
print(str1[0] == "A", str1[len(str1)-1] == "Z")

#xndir 12
mirg = "banana"
print(mirg.count('a'))

#xndir 13
sentance = input("Enter your sentance: ")
splited = sentance.split(" ")
joined = "-".join(splited)
print(joined)

#xndir 14
name = input("Enter your name: ")
print(f"Hello, {name}!")