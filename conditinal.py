if True:
    print('conditional was True')

language = 'Python'

if(language == 'Python'):
    print('True')

if(language != 'Java'):
    print('True')

language = 'Java'

if language == 'Python':
    print("Language is Python.")
else:
    print("Language is not Python.")

if language == 'Python':
    print("language is Python")
elif language == 'Java':
    print("Language is Java")
elif language == 'JS':
    print("Language is Javascript")
else:
    print("No Match!")

user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)
print(a is b)
print(id(a))
print(id(b))

# condition = False
# condition = None
# condition = 0
# condition = []
# condition = ''
condition = {}


if condition:
    print("Evaluated to True")
else:
    print("Evaluated to False")
