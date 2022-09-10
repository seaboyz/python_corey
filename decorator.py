# def outer_function():
#     message = 'Hi'

#     def inner_function():
#         print(message)
#     return inner_function


# my_func = outer_function()
# my_func()
# my_func()
# my_func()

# def outer_function(msg):

#     def inner_function():
#         print(msg)

#     return inner_function

# hi_func = outer_function('Hi')
# bye_func = outer_function('Bye')

# hi_func()
# bye_func()

# def decorator_function(message):
#     def wrapper_function():
#         print(message)
#     return wrapper_function

# def wrapper_function(*args, **kwargs):
#     print(
#         f"wapper function executed this before {original_function.__name__} function.")
#     return original_function(*args, **kwargs)
# return wrapper_function


# @decorator_function
# def display():
#     print("Display function ran.")


# @decorator_function
# def display_info(name, age):
#     print(f"display_info ran with argumens {name}, {age}.")


# display()
# display_info('John',40)
# def decorator_function(original_function):
#     def wrapper_function(*args, **kwargs):
#         print(
#             f"wapper function executed this before {original_function.__name__} function.")
#         return original_function(*args, **kwargs)
#     return wrapper_function

""" 
class decorator_class(object):
    def __init__(self, orginal_function):
        self.original_function = orginal_function

    def __call__(self, *args, **kwargs):
        print(
            f"call() method exiecuted this before {self.original_function.__name__}")
        return self.original_function(*args, **kwargs)


@decorator_class
def display():
    print("Display function ran.")


@decorator_class
def display_info(name, age):
    print(f"display_info ran with argumens {name}, {age}.")


display()
display_info('John', 40)
 """


def my_timer(orig_func):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print(f"{orig_func} ran in: {t2} secs.")
        return result

    return wrapper


class decorator_class(object):
    def __init__(self, orginal_function):
        self.original_function = orginal_function

    def __call__(self, *args, **kwargs):
        print(
            f"call() method exiecuted this before {self.original_function.__name__}")
        return self.original_function(*args, **kwargs)


def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(
        orig_func.__name__), level=logging.INFO)
        
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


@my_timer
@my_logger
def display_info(name, age):
    print(f"display_info ran with arguments ({name}, {age}).")

# @my_logger
# def display_info(name,age):
#     print(f"display_info ran with arguments ({name}, {age}).")


display_info('John', 40)
