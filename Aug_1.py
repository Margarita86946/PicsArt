# 1
def simple_sequance(start, end):
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("Invalid type")
    
    if start > end:
        return
    
    for i in range(start, end + 1):
        yield i

gen = simple_sequance(-3, 5)

for num in gen:
    print(num, end = " ")

# 2
def countdown(n):
    if not isinstance(n, int) or n < 1:
        raise TypeError("Invalid type")
    
    for i in range(n, 0, -1):
        print(f"Yielding: {i}")
        yield i

gen = countdown(5)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

# 3
numbers = list(range(1 ,11))

squares_list = [i ** 2 for i in numbers]

squares_gen = (i ** 2 for i in numbers)

print(f"List: {squares_list}")

print(f"Gen object: {squares_gen}")

for sq in squares_gen:
    print(sq)

# 4
def fibonacci_gen(limit = None):
    if (not isinstance(limit, int) and limit != None) or limit < 0:
        raise TypeError("Invalid type")
    
    a, b = 0, 1

    while limit is None or a <= limit:
        yield a
        a, b = b, a + b


for num in fibonacci_gen(5):
    print(num)   

# 5
import typing

def even_numbers(nums):
    if not isinstance(nums, typing.Iterable):
        raise TypeError("Invalid type")
    
    for i in nums:
        if isinstance(i, int) and i % 2 == 0:
            yield i

numbers = [1, 2, 3, 4, 5, 10, 11, 14]

for i in even_numbers(numbers):
    print(i, end = " ")

# 6
import typing

def cumulative_sum(nums):
    if not isinstance(nums, typing.Iterable):
        raise TypeError("Invalid type")
    
    total = 0
    for num in nums:
        total += num
        yield total

for partial_sum in cumulative_sum([1, 3, 5, 2]):
    print(partial_sum)