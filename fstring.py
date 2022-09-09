""" first_name = 'Corey'
last_name = 'Schafer'

sentence = 'My name {} {}.'.format(first_name, last_name)

sentence = f"My name is {first_name} {last_name}."

print(sentence)
 """

""" person = {'name':'Jenn','age':23}

# sentence = "My name is {} and I am {} years old.".format(person['name'],person['age'])

sentence = f"My name is {person['name']} and I am {person['age']} years old."

print(sentence) """

""" calculation = f"4 times 11 is equal to {4 * 11}."

print(calculation) """

""" for n in range(1,11):
    # sentence = f"The value is {str(n).zfill(2)}."
    sentence = f"The value is {n:02}."
    print(sentence) """

""" pi = 3.1415926

sentence = f"Pi is equal to {pi:.4f}"
print(sentence)
 """

from datetime import datetime

birthday = datetime(1981,12,22)

sentence = f"My birthday is on {birthday:%B %d %Y}."

print(sentence)
