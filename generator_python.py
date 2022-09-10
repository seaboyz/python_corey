""" def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result


my_nums = [1, 2, 3, 4, 5]

print(my_nums)
print(square_numbers(my_nums)) """


# def square_numbers(nums):
#     for i in nums:
#         yield i*i


# my_nums = [1, 2, 3, 4, 5]

# my_nums_gen = square_numbers(my_nums)

# print(my_nums)

# print(next(my_nums_gen))
# print(next(my_nums_gen))
# print(next(my_nums_gen))
# print(next(my_nums_gen))
# print(next(my_nums_gen))

# my_nums = [1, 2, 3, 4, 5]

# def square_numbers(nums):
#     for i in nums:
#         yield i*i

# my_nums_gen = square_numbers(my_nums)

# for num in my_nums_gen:
#     print(num)


# my_nums = [1, 2, 3, 4, 5]

# my_nums_gen = (x*x for x in my_nums)

# print(my_nums_gen)

# for num in my_nums_gen:
#     print(num)


