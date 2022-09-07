from tkinter import N


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# my_list = []
# for n in nums:
#     my_list.append(n)

# my_list = [n for n in nums]

# my_list = [n**2 for n in nums]

# my_list =list(map(lambda n: n*n, nums))

# my_list = [n for n in nums if n % 2 == 0]
# my_list = list(
#     filter(lambda n: n % 2 == 0, nums)
# )

# my_list = []

# for letter in 'abcd':
#     for num in range(4):
#         my_list.append((num, letter))

# my_list = [(num,letter) for num in range(4) for letter in 'abcd']

# names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
# heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

# my_list = [(name, hero) for name in names for hero in heros]

# print(my_list)

# my_dict = {hero:name for hero,name in zip(heros,names) if name!='Peter' }

# print(my_dict)

# Set comprehension
# nums = [1, 1, 2, 1, 3, 4, 3, 2, 5, 5, 6, 7, 8, 9, 9, 10]

# my_set = {num for num in nums}

# print(my_set)


# def gen_func(nums):
#     for n in nums:
#         yield n*n


# my_gen = gen_func(nums)

my_gen = (n*n for n in nums)

for i in my_gen:
    print(i)

