# Implemen enumerate
import typing

def custom_enumerate(iterable, start=0):
    if not isinstance(iterable, typing.Iterable) or not isinstance(start, int):
        raise TypeError("Invalid type")
    
    res = []
    for i in iterable:
        res.append((start, i))
        start += 1
    return res

print(custom_enumerate([1,2,3], -1))

# Implement reduce
import typing

def custom_reduce(function, iterable, initial = None):
    if not isinstance(iterable, typing.Iterable) or not isinstance(function, typing.Callable):
        raise TypeError("Invalid type")
    
    if initial is None:
        if not iterable:
            raise TypeError("Iterable can not be empty")
        res = iterable[0]
        start = 1
    else:
        res = initial
        start = 0

    for i in range(start, len(iterable)):
        res = function(res, iterable[i])

    return res

print(custom_reduce(lambda x, y: x + y, [], 100))

# Implement map
import typing

def custom_map(func, *iterables):
    if not isinstance(func, typing.Callable):
        raise TypeError("Invalid type")
    
    for i in iterables:
        if not isinstance(i, typing.Iterable):
            raise TypeError("Invalid type")
    
    min_len = len(min(iterables, key = len))
        
    res = []
    for i in range(min_len):
        args = [it[i] for it in iterables] 
        res.append(func(*args)) 
        
    return res
    
print(custom_map(lambda x, y: x + y, [1, 2, 3, 4], [1, 2, 3]))

# implement zip
import typing

def custom_zip(*iterables, strict=False):
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

    res = []
    for i in range(min_len):
        el = tuple(it[i] for it in iterables)
        res.append(el)
    return res

print(custom_zip('abcdefg', "hgghg", "hsdh"))

# Implement filter
import typing

def custom_filter(function, iterable):
    if (not isinstance(function, typing.Callable) and function is not None) or not isinstance(iterable, typing.Iterable):
        raise TypeError("Invalid type")

    if function is None:
        function = lambda x: x
    
    res = []
    for i in iterable:
        if function(i):
            res.append(i)
    
    return res

print(custom_filter(None, [1, 2, 0, 4, 5, 6]))