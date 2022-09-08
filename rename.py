from fileinput import filename
import os

# change current directory
# os.chdir('/Users/qianggao/Desktop/python_corey')

# make a now directory
# os.mkdir('change_name_practice')

# cd the new folder
os.chdir('/Users/qianggao/Desktop/python_corey/change_name_practice')

# print(os.getcwd())

# create bunch of sample files
# for i in range(1,11):
#     open(f"test_{i}.txt",'w')

# change files names in batch
for f in os.listdir():
    file_name, file_extention = os.path.splitext(f)

    file_title, file_number = file_name.split('_')

    # pad number with 0s
    file_number = file_number.zfill(2)

    new_name = f"{file_number}_{file_title}{file_extention}"

    os.rename(f,new_name)
