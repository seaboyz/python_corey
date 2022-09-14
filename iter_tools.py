from ast import operator
import itertools
from unittest import result

# counter = itertools.count(start=5,step=-2.5)

# data = [100, 200, 300, 400]

""" print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter)) """

# daily_data = list(zip(itertools.count(), data))
# print(daily_data)

# daily_data = list(zip(range(10), data))
# print(daily_data)

# daily_data = list(itertools.zip_longest(range(10), data))
# print(daily_data)

""" counter = itertools.cycle([1, 2, 3])
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter)) """

""" counter = itertools.cycle(('On','Off'))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter)) """

""" counter = itertools.repeat(2, times=3)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter)) """

""" squares = map(pow,range(10),itertools.repeat(2))
print(list(squares)) """

""" squares = itertools.starmap(pow,[(0,2),(1,2),(2,2)])
print(list(squares)) """

letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3, 2, 1, 0]
names = ['Corey', 'Nicole']

# result = itertools.combinations(letters, 2)
# result = itertools.product(numbers,repeat=4)
# result = itertools.permutations(letters,2)
# result = itertools.combinations_with_replacement(numbers,4)
# result = itertools.chain(letters,numbers,names)
# result = itertools.islice(range(10), 1, 5, 2)

""" selectors = [True, True, False, True]
result = itertools.compress(letters,selectors) """

""" def it_2(n):
    if n < 2:
        return True
    return False
result = filter(it_2,numbers)
result = itertools.filterfalse(it_2,numbers)
result = itertools.dropwhile(it_2,numbers)
result = itertools.takewhile(it_2,numbers) """

# result = itertools.accumulate(numbers)

people = [
    {
        "name": "Corey",
        "height": 170,
        "age": 30,
    },
    {
        "name": "Nicole",
        "height": 160,
        "age": 27,
    },
    {
        "name": "David",
        "height": 180,
        "age": 30,
    },
]

""" # sort by age
sorted_people = sorted(people, key=lambda x: x["age"])

def get_age(person):
    return person["age"]


result = itertools.groupby(sorted_people, get_age)
for key, group in result:
    print(key, list(group)) """

result = itertools.tee(letters)

for item in result:
    print(item)

""" with open('sample.txt','r') as f:
    header = itertools.islice(f,3)

    for line in header:
        print(line) """
