from subprocess import call


class Duck:

    def quack(self):
        print('Quack, quack')

    def fly(self):
        print('Flap, flap!')


class Person:

    def quack(self):
        print("I am Quacking like a Duck!")

    def fly(self):
        print("I'm Flapping my arms!")

# def quack_and_fly(thing):
#     # Not Duck-typed(Non-Pythonic)
#     if isinstance(thing,Duck):
#         thing.quack()
#         thing.fly()
#     else:
#         print('This has to be a Duck!')

#     print()

# def quack_and_fly(thing):
#     thing.quack()
#     thing.fly()

#     print()


""" # Non-Pythonic
def quack_and_fly(thing):
    if hasattr(thing,'quack'):
        if callable(thing.quack):
            thing.quack()
    
    if hasattr(thing, 'fly'):
        if callable(thing.fly):
            thing.fly() """

# Pythonic (EAFP) easier to ask forgiveness than permission


# def quack_and_fly(thing):
#     try:
#         thing.quack()
#         thing.fly()
#     except AttributeError as e:
#         print(e)

#     print()


# d = Duck()
# quack_and_fly(d)

# p = Person()
# quack_and_fly(p)
person = {'name':'Jess','age':23}

""" #LBYL Look Before You Leap
if 'name' in person and 'age' in person and 'job' in person:
    print(f"I'm {person['name']}. I'm {person['age']} years old and I am a {person['job']}.")
else:
    print('Missing some keys.')

# EAFP
try:
   print(f"I'm {person['name']}. I'm {person['age']} years old and I am a {person['job']}.")
except KeyError as e:
    print(f"Missing {e} key.")  """

my_list = [1,2,3,4,5,6]

# LBYL
if(len(my_list) >=6):
    print(my_list[5])
else:
    print("That index does not exist.")

# EAFP
try:
    print(my_list[5])
except IndexError:
    print("That index does not exist.")