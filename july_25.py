# Write a recursive binary search algorithm to find the index of a target value in a sorted array.
def binary_search(ls, target, start=0, end=None):
    if end is None:
        end = len(ls) - 1

    if start > end  or not isinstance(ls, list):
        return -1

    ls.sort()
    mid = (start + end) // 2

    if target == ls[mid]:
        return mid
    elif target > ls[mid]:
        return binary_search(ls, target, mid + 1, end)
    else:
        return binary_search(ls, target, start, mid - 1)

print(binary_search([3, 2, 1], 3))

# Write a recursive function to flatten a list containing nested lists.
def flatten_a_list(ls):
    if not isinstance(ls, list):
        return -1
    
    res = []
    for i in ls:
        if isinstance(i, list):
            res.extend(flatten_a_list(i))
        else:
            res.append(i)
    
    return res

print(flatten_a_list([1, 2, [3, 4, [5, 6]]]))

# Write a recursive function to find the maximum element in a list.
def find_max(ls):
    if not len(ls) or not isinstance(ls, list):
        return -1
    
    if len(ls) == 1:
        return ls[0]
    else:
        return max(ls[0], find_max(ls[1:]))
    
print(find_max([1, 2, 3]))

# Write a recursive function to calculate the n-th Fibonacci number.
def fibonacci(n):
    if n < 0 or not isinstance(n, int):
        return -1
    
    if n == 0 or n == 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)
    
print(fibonacci(10))