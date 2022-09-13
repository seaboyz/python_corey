from tkinter import image_names
from PIL import Image, ImageFilter
import os

# Change the current working directory to the picture directory
os.chdir("/Users/qianggao/Desktop/pics")

# Make a new folder to store the modified images
os.makedirs("modified", exist_ok=True)

# Make a new folder to store the rotated images
os.makedirs("rotated", exist_ok=True)

# Make a new folder to store the blurred images
os.makedirs("blurred", exist_ok=True)

size_300 = (300, 300)

""" image1 = Image.open("67877030618__B75DE0F7-41E7-41FD-8D99-0EA0C45E60F8.jpeg")
# image1.show()
image1.save("pic1.png") """

# Loop through all the images in the directory
for image_name in os.listdir('.'):
    """ if image_name.endswith(".jpeg") or image_name.endswith(".jpg") or image_name.endswith(".JPG"):
        i = Image.open(image_name)
        # Get the file name without the extension
        file_name, extension = os.path.splitext(image_name)
        pre_fix, file_number, *args = file_name.split("_")
        if(pre_fix == 'IMG'):
            print(image_name)
            i.save(f'{file_number}.jpg', 'jpeg')
            os.remove(image_name) """

    """ if image_name.endswith('.png') or image_name.endswith('.PNG'):
        i = Image.open(image_name)
        file_name, extension = os.path.splitext(image_name)
        pre_fix, file_number = file_name.split("_")
        if(pre_fix == 'IMG'):
            print(image_name)
            i.save(f'{file_number}.png', 'png')
            os.remove(image_name)
 """
    """ if image_name.endswith('.jpeg') or image_name.endswith('.jpg') or image_name.endswith('.JPG'):
        i = Image.open(image_name)
        file_name, extension = os.path.splitext(image_name)
        if len(file_name) > 4:
            i.save(f'{file_name[-4:]}.jpg', 'jpeg')
            os.remove(image_name) """

    """ if image_name.endswith('.jpg'):
        i = Image.open(image_name)
        file_name, extension = os.path.splitext(image_name)
        i.thumbnail(size_300)
        i.save(os.path.join('modified', file_name + '_thumbnail.jpg')) """

    """ if image_name.endswith('.jpg'):
        i = Image.open(image_name)
        file_name, extension = os.path.splitext(image_name)
        i.rotate(90).save(os.path.join('rotated', file_name + '_rotated.jpg')) """

    if image_name.endswith('.jpg'):
        i = Image.open(image_name)
        file_name, extension = os.path.splitext(image_name)
        i.filter(ImageFilter.GaussianBlur(15)).save(os.path.join('blurred', file_name + '_blurred.jpg'))
