nums = [1, 2, 3]

""" for num in nums:
    print(num) """

# print(dir(nums))

""" iter_nums = nums.__iter__()
print(iter_nums.__next__())
print(iter_nums.__next__()) """

""" iter_nums = iter(nums)
print(next(iter_nums))
print(next(iter_nums))
print(next(iter_nums))
print(next(iter_nums)) """

""" iter_nums = iter(nums)
while True:
    try:
        item = next(iter_nums)
        print(item)
    except StopIteration:
        break """


class MyRange:
    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current


def my_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1


# nums = MyRange(1, 10)

# for num in nums:
#     print(num)

""" print(next(nums))
print(next(nums))
print(next(nums)) """

nums = my_range(1, 10)
print(next(nums))
print(next(nums))

for num in nums:
    print(num)
