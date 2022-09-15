from re import sub
import subprocess

# subprocess.run('ls',shell=True)
# subprocess.run('ls -la',shell=True)

# p1 = subprocess.run(['ls','-la'])
# print(p1.returncode)
# print(p1.stdout)

# p1 = subprocess.run(['ls', '-la'], capture_output=True)

# p1 = subprocess.run(['ls', '-la'], stdout=subprocess.PIPE, text=True)

""" with open('output.txt', 'w') as f:
    p1 = subprocess.run(['ls', '-la'], stdout=f, text=True)
 """

""" p1 = subprocess.run(['ls', '-la', 'dne'], capture_output=True, text=True,check=True)
print(p1.stderr) """

""" p1 = subprocess.run(['ls', '-la'], stderr=subprocess.DEVNULL)
print(p1.stderr) """

p1 = subprocess.run(['cat', 'test.txt'], capture_output=True, text=True)
# print(p1.stdout)

p2 = subprocess.run(['grep', '-n', 'cancer'],
                    capture_output=True,
                    text=True,
                    input=p1.stdout)

print(p2.stdout)
