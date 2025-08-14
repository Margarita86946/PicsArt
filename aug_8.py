# Write a program to identify all prime numbers between 1 and 100 using list comprehensions.
def is_prime(n):
    if n <= 0 or not isinstance(n, int):
        return
    
    if n < 2:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

print([i for i in range(1, 100) if is_prime(i)])

# Using a list comprehension, create a new list from [1, 2, 3, -4, -5, 6] that contains only the positive numbers.
ls = [1, 2, 3, -4, -5, 6]
newLs = [i for i in ls if i > 0]
print(newLs)

# Write a program that categorizes numbers in a list as "Even", "Odd", or "Prime" using if-elif inside a loop.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    if is_prime(num):
        print(f"{num} is Prime")
    elif num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")

# Create a nested list comprehension to generate a multiplication table (1-10).
table = [[i * j for i in range(1, 11)] for j in range(1, 11)]
print(table)

# Write a program to filter and print words from a list of strings that start with vowels using list comprehension.
def is_vowel(string):
    vowels = ("a", "e", "i", "o", "u")

    for char in string:
        if char not in vowels:
            return False

    return True

words = ["banana", "apple", "union", "enter", "good"]
newWords = [i for i in words if is_vowel(i[0])]
print(newWords)

# Implement custom_enumerate using yield, similar to the Python built-in enumerate.
import typing

def custom_enumerate_gen(iterable, start=0):
    if not isinstance(iterable, typing.Iterable) or not isinstance(start, int):
        raise TypeError("Invalid type") 
           
    for x in iterable: yield start, x; start += 1

print(list(custom_enumerate_gen([1,2,3], -1)))

# Create a function custom_map_with_yield that applies a transformation
# to elements of an iterable and yields each result.
import typing

def custom_map_gen(func, *iterables):
    if not isinstance(func, typing.Callable):
        raise TypeError("Invalid type")
    
    for i in iterables:
        if not isinstance(i, typing.Iterable):
            raise TypeError("Invalid type")
    
    min_len = len(min(iterables, key = len))
        
    yield from (func(*[it[i] for it in iterables]) for i in range(min_len))

    
print(list(custom_map_gen(lambda x, y: x + y, [1, 2, 3, 4], [1, 2, 3])))

# Implement custom_filter_with_yield that yields items from an iterable that satisfy a given condition.
import typing

def custom_filter(function, iterable):
    if (not isinstance(function, typing.Callable) and function is not None) or not isinstance(iterable, typing.Iterable):
        raise TypeError("Invalid type")

    if function is None:
        function = lambda x: x
    
    yield from (i for i in iterable if function(i))

print(list(custom_filter(None, [1, 2, 0, 4, 5, 6])))

# Write a zip_generator that takes multiple iterables and yields tuples, similar to Python's zip.
import typing

def custom_zip_gen(*iterables, strict=False):
    for i in iterables:
        if not isinstance(i, typing.Iterable):
            raise TypeError("Invalid type")
    
    if not isinstance(strict, bool):
        raise TypeError("Invalid type")
    
    if strict:
        lenght = len(iterables[0])
        for i in iterables:
            if len(i) != lenght:
                raise ValueError("Lenghts of iterables should be the same")
    else:
        min_len = len(min(iterables, key = len))

    yield from (tuple(it[i] for it in iterables) for i in range(min_len))

print(list(custom_zip_gen('abcdefg', "hgghg", "hsdh")))

# Write a generator function range_generator that mimics the behavior of range(start, stop, step) using yield.
def range_gen(start, stop, step = 1):
    if not isinstance(start, int) or not isinstance(stop, int) or not isinstance(step, int):
        raise TypeError("Invalid type")
    
    while start != stop:
        yield start
        start += step

print(list(range_gen(1, 10, 3)))