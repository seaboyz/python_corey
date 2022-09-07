student = {'name': 'john', 'age': 25, 'course': ['Math', 'CompSci']}

print(student['name'])

print(student.get(1))
print(student.get('name'))
print(student.get('phone', 'Not Found'))

student['phone'] = "555-555-5555"
print(student)

student.update({'name':'jane'})
print(student)

del student['age']
print(student)

phone = student.pop('phone')
print(student)
print(phone)

print(student.keys())
print(student.values())
print(student.items())

for key in student:
    print(key)

for key,value in student.items():
    print(key, value)