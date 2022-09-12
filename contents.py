""" f = open('sample.txt', 'w')
f.write('lorem ipsum')
f.close() """

""" with open('sample.txt', 'w') as f:
    f.write('lorem ipsum') """


""" class Open_File():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exception_type, exception_value, exception_traceback):
        self.file.close()

with Open_File('sample.txt','w') as f:
    f.write('Testing')

print(f.closed) """


""" from contextlib import contextmanager
@contextmanager
def open_file(file, mode):
    try:
        f = open(file, mode)
        yield f
    finally:
        f.close()


with open_file('sample.txt', 'w') as f:
    f.write('Hello World')

print(f.closed) """

""" 
import os
from contextlib import AbstractContextManager
cwd = os.getcwd()
os.chdir('Sample-Dir-One')
print(os.listdir())
os.chdir(cwd)

cwd = os.getcwd()
os.chdir('Sample-Dir-Two')
print(os.listdir())
os.chdir(cwd)
 """




from contextlib import contextmanager
import os
@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)

with change_dir('Sample-Dir-One'):
    print(os.listdir())
