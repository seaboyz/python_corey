from datetime import datetime
import os

# print(dir(os))

os.chdir('/Users/qianggao/Desktop')

# print(os.getcwd())

# print(os.listdir())

# os.mkdir('OS-Demo')

# os.makedirs('OS-Demo2/new folder')

# os.rmdir('OS-Demo')

# os.removedirs('OS-Demo2/new folder')

# os.rename('test.txt','demo.txt')

# print(os.stat('demo.txt').st_size)

# mod_time = os.stat('demo.txt').st_mtime
# print(datetime.fromtimestamp(mod_time))

# for dirpath,dirnames,filenames in os.walk(os.getcwd()):
#     print(dirpath,dirnames,filenames,"\n")

# print(os.environ.get('HOME'))

# file_path = os.path.join(os.environ.get('HOME'),'test.txt')
# print(file_path)

# print(os.path.basename('/tmp/test.txt'))
# print(os.path.dirname('/tmp/test.txt'))
# print(os.path.exists('/tmp/test.txt'))
# print(os.path.split('/tmp/test.txt'))

print(dir(os.path))
