# Python 3.7.2/win10 64bit/IDE:Pycharm 2018.3.3
# practice for walk function in os package
from random import randint
import os
import platform

seperator='<'
print(seperator.join('1234'))


seperator=str(randint(100, 999))
print(seperator.join('abc'))

# iteration and print folders and files from up to down
for paths, folders, files in os.walk("D:\\workspaces\\python_study\\zipfolder"):
    print(paths, folders, files)

# get file full path concatnation with path and file
for paths, folders, files in os.walk('D:\\workspaces\\python_study\\zipfolder'):
    for file in files:
        file_path=os.path.join(paths, file)
        print(file_path)



    print(os.system("python --version"))
    print(platform.platform())
    print(platform.machine())
