import os
import shutil

path = input('Enter the folder path : ')
names = os.listdir(path)
folder_name = ['image.png', 'image.jpg']
print('The folder contains the following files = ' + str(names))

for x in range(0, 10):
    if not os.path.exists(path+folder_name[x]):
        os.makedirs(path+folder_name[x])

for files in names:
    if ".png" in files and not os.path.exists(path + 'image.png/' + files):
        shutil.move(path + files, path + 'image.png/' + files)
    if ".jpg" in files and not os.path.exists(path + 'image.jpg/' + files):
        shutil.move(path + files, path + 'image.jpg/' + files)
