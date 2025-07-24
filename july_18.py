# Write a function sum_numbers that accepts an arbitrary number of positional arguments and returns their sum.
def sum_numbers(*args):
    for i in args:
        if not isinstance(i, int):
            return -1
        
    return(sum(args))

print(sum_numbers("h"))

# Write a function display_student_info that accepts any number of keyword arguments and prints them in the format: key: value.
def display_student_info(**kwargs):
    if not kwargs:
        print("Empty kwargs.")
    
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_student_info(name = "Alice", age = 20, major = "CS")

# Write a function order_item that accepts:
# o A required item argument.
# o A quantity argument with a default value of 1.
# o Arbitrary positional arguments (*args) to specify additional options.
# o Arbitrary keyword arguments (**kwargs) for customization details.
def order_item(item, quantity = 1, *options, **customizations):
    print(f"Item: {item}")
    print(f"Quantity: {quantity}")
    print(f"Options: {options}")
    print(f"Customizations: {customizations}")

order_item("pizza", 2, "extra chees", "thin crust", size = "large", spicy = True)

# Write a function register_user that accepts:
# o A required positional argument: username.
# o A required keyword-only argument: email.
# o Hint: Use * to enforce keyword-only arguments
def register_user(username, *, email):
    print(f"Email: {email}")
    print(f"Username: {username}")

register_user( "James", email = "akshsds@gmail.com")

# Analyze the following code, explain why it raises an error, and fix the function call:

# The code doesnt rais an error but the call is wrong extras are positional arguments but in the call they were treated as keyword arguments so details took them.
# Here is the corrected version of the code.
def book_ticket(destination, price, discount=0, *extras, **details):
    print(f"Booking to {destination} for ${price - discount}")
    if extras:
        print(f"Extras: {', '.join(extras)}")
    if details:
        print(f"Details: {details}")
book_ticket("Paris", 100, 10, "window seat", "meal")

# Implement a function process_data that accepts a mix of positional arguments, 
# default arguments, arbitrary positional arguments (*args), and arbitrary keyword arguments (**kwargs).(....shat erkar pahanj e)
def process_data(operation = None, data = [], threshold = None, *numbers, **options):
    data += list(numbers)

    if options.get("reverse", False):
        return data.reverse()
    
    if options.get("uniqur", False):
        return list(set(data))

    if operation is None:
        return data

    operation = operation.lower()
    result = None
    
    if  operation == "sum":
        result = sum(data)
    elif operation == "multiply":
        result = 1
        for i in data:
            result *= i
    elif operation == "filter":
        if  threshold != None:
            result = [i for i in data if i < threshold]
        else:
            return "Threshold required for 'filter' operation"
    else:
        return "Invalid operation"
    
    return result

print(process_data("sum", data = [1, 2, 3], 5, 4, 5, 6, reverse = True, unique = True))

# Write a closure that creates a counter. Each call to the inner function should increment the counter by 1 and return the current count.
def call_counter_wrapper():
    def call_counter():
        call_counter_wrapper.count += 1
        return call_counter_wrapper.count
    return call_counter

call_counter_wrapper.count = 0

print(call_counter_wrapper()())
print(call_counter_wrapper()())

def call_counter():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count   
    return inner

counter = call_counter()

print(counter())
print(counter())

# Create a closure that takes a multiplier as an argument and returns a function that multiplies any given number by that multiplier.
def multiply_wrapper(multiplier):   
    def multiply(number):
        nonlocal multiplier
        if not isinstance(multiplier, int) or not isinstance(number, int):
            return
        
        return(multiplier * number)
    
    return multiply

print(multiply_wrapper(3)(2))

# Write a closure that tracks the number of times a specific function is called.
def greet():
    print("hello maga")

def counter(f):
    def inner():
        inner.counter += 1
        f()
    inner.counter = 0
    return inner

greet = counter(greet)

greet()
greet()
greet()

print(greet.counter)

# Create a closure to calculate running totals. Each call to the inner 
# function should add a number to the total and return the updated total.
def calculate_total():
    total = 0
    def inner(number):
        nonlocal total
        total += number
        return total
    return inner

calculate = calculate_total()

print(calculate(5))
print(calculate(8))

# Implement a closure that takes a string as input and allows appending to or resetting the string when the inner function is called.
def string_manipulator(string):
    def inner(key_word):
        nonlocal string
        if not isinstance(string, str) or not isinstance(key_word, str):
            return
        
        if key_word.lower() == "reset":
            string = ""
        else:
            string += key_word
        return string
    return inner

print(string_manipulator("barev")("reset"))
