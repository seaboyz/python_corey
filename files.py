# f = open('test.txt','r')

# print(f.name)
# print(f.mode)

# f.close()

"""
# context manager
with open('test.txt', 'r') as f:
    # f_contents = f.read()
    # f_contents = f.readlines()
    # f_contents = f.readline()
    for line in f:
        print(line)
 """
""" 
# read 100 words
with open('test.txt', 'r') as f:
    f_contents = f.read(100)
    print(f_contents, end='')

    f_contents = f.read(100)
    print(f_contents, end='')
 """
""" 
# read large file
with open('test.txt', 'r') as f:
    size_to_read = 100

    f_contents = f.read(size_to_read)

    while(len(f_contents)>0):
        print(f_contents, end='')
        f_contents = f.read(size_to_read)
 """

""" with open('test.txt', 'r') as f:
    size_to_read = 10

    f_contents = f.read(size_to_read)

    while(len(f_contents)>0):
        print(f_contents, end='*')
        f_contents = f.read(size_to_read) """

""" 
with open('test.txt', 'r') as f:
    size_to_read = 10

    f_contents = f.read(size_to_read)
    print(f_contents,end='')

    f.seek(0)

    f_contents = f.read(size_to_read)
    print(f_contents,end='')
 """
""" 
with open('test.txt', 'r') as f:
    f.write('Test')
 """

""" 
with open('test2.txt', 'w') as f:
    f.write('Test') 
    f.seek(0)
    f.write('B')
 """

""" 
# copy line by line
with open('test.txt','r') as rf:
    with open('test_cp.txt','w') as wf: 
        for line in rf:
            wf.write(line)
"""

""" # write and read binary
with open('python.jpeg','rb') as pic:
    with open('python_copy.jpeg','wb') as pic_cp:
        for line in pic:
            pic_cp.write(line)
 """
with open('python.jpeg', 'rb') as pic:
    with open('python_copy.jpeg', 'wb') as pic_cp:
        chuck_size = 4096
        pic_chuck = pic.read(chuck_size)
        while len(pic_chuck) > 0:
            pic_cp.write(pic_chuck)
            pic_chuck = pic.read(chuck_size)
