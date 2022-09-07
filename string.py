from gettext import find


message = "Hello World"

print(message.lower())
print(message.upper())
print(message.count('l'))
print(message.find('World'))
print(message.find('x'))
print(message.replace('World','Universe'))
print(message + " Michael")
print(f"{message} Michael")
print("{} Michael".format(message))

print(dir(message))
print(help(find))