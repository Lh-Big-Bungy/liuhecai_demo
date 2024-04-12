def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} is called")
        result = func(*args, **kwargs)
        print(result)
        print(f"Function {func.__name__} is finished")
        return result
    return wrapper

@log_decorator
def add(a, b):
    return a + b

result = add(3, 5)
print("Result:", result)
