# 1 Know how to twrite code on a whiteboard or paper
# 2 Know the basic python control flow
""" for i in range(1, 11):
    print(i)

i = 1
while i <= 10:
    print(i)
    i += 1

a = 10
b = 20
if a > b:
    print(f"{a} is greater than {b}.")
elif a < b:
    print(f"{a} is less than {b}.")
else:
    print(f"{a} is equal to {b}.")
 """
# 3 Be able to discuss how you've used python in a project
# web scraping
# system testing

""" import os, glob
os.chdir("/Users/qianggao/Desktop/python_corey/")
for file in glob.glob("*.py"):
    print(file) """

# 4 Know how to solve common coding problems
# Hackerrank
""" for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num) """

# 5 Know the data types in python
# int, float, str, bool, list, tuple, dict, set, None
""" my_tuple = (1, 2, 3)
my_list = [1, 2, 3]
my_dict = {"name": "Qiang", "age": 30}
my_set = {1, 2, 3} """

# 6 Know how to use the list comprehension
my_list = [char for char in 'hello']
print(my_list)
my_list = [num*num for num in range(1, 11)]
print(my_list)

# 7 Know how to use generators


def fib(num):
    a, b = 0, 1
    for i in range(0, num):
        yield f"{i+1}:{a}"
        a, b = b, a + b


for item in fib(10):
    print(item)

# 8 Know the basic of oop


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def identity(self):
        print(f"My name is {self.name}, and I am {self.age} years old.")


class SuperHero(Person):
    def __init__(self, name, age, superpower):
        super().__init_(name, age)
        self.superpower = superpower

    def identity(self):
        super(SuperHero, self).identity()
        print(f"My superpower is {self.superpower}.")

# 9 Have python related questions ready to ask you interviewer

# 10 Know the basic of other technologies.