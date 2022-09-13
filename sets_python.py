s1 = set([1, 2, 3, 4, 5])
print(s1)

s2 = set([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])
print(s2)

s1.add(6)
print(s1)

s1.update([7, 8, 9], s2)
print(s1)

s1.remove(9)
print(s1)

s1.discard(10)
print(s1)

""" s1.remove(10)
print(s1) """

s1 = {1,2,3}
s2 = {2,3,4}
s3 = {3,4,5}

print(s1 & s2)
print(s1 | s2)

print(s1 & s2 & s3)

s4 = s2.difference(s1)
print(s4)

s5 = s1.symmetric_difference(s2)
print(s5)

l1 = [1,2,3,1,2,3]

l2 = list(set(l1))
print(l2)

employees = ['John', 'Mary', 'Bob', 'Mosh', 'Mary', 'John']
gym_members = ['John', 'Mosh', 'Bob']
developers = ['Mary', 'John', 'Bob', 'Mosh']

emp_gym_and_dev = set(employees).intersection(gym_members, developers)
print(emp_gym_and_dev)

emp_gym_or_dev = set(employees).union(gym_members, developers)
print(emp_gym_or_dev)