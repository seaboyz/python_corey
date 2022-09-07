# def hello_func():
#     return 'Hello Function.'


# for i in range(4):
#     print(hello_func())

# print(len(hello_func()))

# def hello_func(greeting):
#     return f"{greeting} function."

# print(hello_func("hello"))

# def hello_function(greeting,name):
#     return "{greeting}, {name}"

# print(hello_function('hello','john'))

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

# student_info('Math','cs',name='john',age='22')


# course = ['Math', 'Art']
# info = {'name': 'john', 'age': 39}
# student_info(*course, **info)

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """Return True for leap years, False for non-leap years."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]


print( days_in_month(2022, 2))
