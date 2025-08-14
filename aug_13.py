# Write a decorator greet_decorator that adds a greeting message before and after the execution of the decorated function.
import functools

def greet_decorator(fn):
    @functools.wraps(fn)
    def inner(*args, **kwargs):
        print("Hello!")
        fn(*args, **kwargs)
        print("Goodbye!")
    return inner

@greet_decorator
def say_name():
    print("My name is Python.")

print(say_name())

# Create a decorator log_execution that logs the name of the function being executed along with its arguments and return value.
import functools
import inspect

def greet_decorator(fn):
    @functools.wraps(fn)
    def inner(*args, **kwargs):
        print(f"Executing {fn.__name__} with arguments {inspect.signature(fn)}")
        res = fn(*args, **kwargs)
        print(f"{fn.__name__} returned {res}")
        return res
    return inner

@greet_decorator
def add(a, b):
    return a + b

print(add(3, 5))

# Write a decorator execution_timer that measures and prints the time taken by the decorated function to execute.
import functools
import time

def execution_timer(fn):
    @functools.wraps(fn)
    def inner(*args, **kwargs):
        start = time.time()
        fn(*args, **kwargs)
        end = time.time()
        print(f"{fn.__name__} took {end - start} to execute.")
    return inner    

@execution_timer
def slow_function():
    time.sleep(2)
    print("Finished execution!")

slow_function()

# Create a decorator require_login that only allows a function to execute if a global variable is_logged_in is True. If not, raise an exception.
import functools

def require_login(fn):
    @functools.wraps(fn)
    def inner(*args, **kwargs):
        if not is_logged_in:
            raise Exception("You are not logged in.")
        fn(*args, **kwargs)
    return inner 

@require_login
def view_profile():
    print("Acccessing user profile...")

is_logged_in = True
view_profile()