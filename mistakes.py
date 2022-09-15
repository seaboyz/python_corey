import time
from datetime import datetime


# def display_time(time=None):
#     if(time == None):
#         time = datetime.now()
#     print(time.strftime('%B %d, %Y %H:%M:%S'))

def display_time(time=datetime.now()):
    print(time.strftime('%B %d, %Y %H:%M:%S'))


print("default time:", display_time.__defaults__)
display_time()
time.sleep(1)
print("default time:", display_time.__defaults__)
display_time()
time.sleep(1)
print("default time:", display_time.__defaults__)
display_time()


""" names = ['John', 'Paul', 'George', 'Ringo']
heroes = ['Batman', 'Superman', 'Spiderman', 'Ironman']

# zip is iterator, it can be exhausted, so we need to convert it to list to be able to use it again
identities = zip(names, heroes)
iden_list = list(identities)

for names, heroes in identities:
    print(f'{names} is actually {heroes}')
     
print(list(identities))

for name, hero in iden_list:
    print(f'{name} is actually {hero}')

print(iden_list) """

""" import html
import glob

print(html.escape)
print(glob.escape) """

""" def add_employee(name, employee_list=[]):
    employee_list.append(name)
    return employee_list

employees = ['Jane', 'Jack']

print("default argument",add_employee.__defaults__)

print(add_employee('George', employees))
print("default argument",add_employee.__defaults__)

print(add_employee('John'))
print("default argument",add_employee.__defaults__)

print(add_employee('Paul'))
print("default argument",add_employee.__defaults__) """

""" def add_employee(name, employee_list=None):
    if employee_list is None:
        employee_list = []
    employee_list.append(name)
    return employee_list

print(add_employee('John'))
print("Default argument", add_employee.__defaults__)
print(add_employee('Paul'))
print("Default argument", add_employee.__defaults__) """
