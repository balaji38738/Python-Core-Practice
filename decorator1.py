def decorator_func(original_func):
    def wrapper_func(*args, **kwargs):
        print("Wrapped function executed before", original_func.__name__)
        original_func(*args, **kwargs)
    return wrapper_func

@decorator_func
def display_info(name, age):
    print(name, age)

display_info("abc", 24)