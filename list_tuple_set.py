# courses = ['History', 'Math', 'Physics', 'CS']

# print(len(courses))
# print(courses[0])
# print(courses[-1])
# print(courses[:2])

# courses.append('Art')
# print(courses)

# courses.insert(0, 'Music')
# print(courses)

# courses_2 = ['Art', 'Music']

# courses.extend(courses_2)

# print(courses)

# courses.remove('Art')
# print(courses)

# courses.remove('Music')
# print(courses)

# courses.sort()
# print(courses)

# courses.sort(reverse=True)
# print(courses)

# s_courses = sorted(courses)
# print(s_courses)
# print(courses)

# print(min(courses))

# print(courses.index("Art"))
# print('Art' in courses)

# for course in courses:
#     print(course)

# for course in enumerate(courses):
#     print(course)

# for index, course in enumerate(courses):
#     print(index, course)

# course_str = ', '.join(courses)
# print(course_str)

# new_list = course_str.split(', ')
# print(new_list)

list_1 = ['History', 'Math', 'Physics', 'CS']
list_2 = list_1

list_1.remove('History')

print(list_1)
print(list_2)

tup_1 = ('History', 'Math', 'Physics', 'CS')
tup_2 = tup_1

print(tup_1)
print(tup_2)

set_1 = {'History', 'Math', 'Physics', 'CS'}
set_1.add('History')
print(set_1)

print('Math' in set_1)

cs_courses = {'History', 'Math', 'Physics', 'CS'}
art_courses = {'History', 'Math', 'Art', 'Design'}
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))

empty_list = []
empty_list = list()

empty_tuple = ()
empty_tuple = tuple()

empty_set = {}  # This is going to create a empty dictionary
empty_set = set()
