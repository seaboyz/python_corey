# try:
#     f = open('testcp.txt')
# except Exception:
#     print(f"Sorry, this file does not exist.")

""" try:
    f = open('test_cp.txt')
except FileNotFoundError as e:
    print(e)
    print(f"Sorry, this file does not exist.")
except Exception :
    print("Sorry, something went wrong.")
else:
    print(f.read())
    f.close()
finally:
    print("Executing Finally...") """

try:
    f = open('test_cp.txt')
    if f.name == 'test_cp.txt':
        raise Exception
except FileNotFoundError as e:
    print(e)
    print(f"Sorry, this file does not exist.")
except Exception :
    print("Sorry, something went wrong.")
else:
    print(f.read())
    f.close()
finally:
    print("Executing Finally...")
