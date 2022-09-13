""" num = 3

if num < 2:
    print("num is less than 2")
else:
    print("num is greater than or equal to 2") """

my_list = [1, 2, 3, 4, 5]

""" for num in my_list:
    print(num)
else:
    print("hit the for/else statement") """

""" for num in my_list:
    print(num)
    if num == 3:
        break
else:
    print("hit the for/else statement") """

""" for num in my_list:
    print(num)
    if num == 6:
        break
else:  # no break
    print("hit the for/else statement") """


def find_index(to_search, target):
    for i, value in enumerate(to_search):
        if value == target:
            break
    else:
        return -1
    return i


my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
index = find_index(my_list, 'i')

print('Found:', index)
