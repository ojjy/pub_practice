# Python 3.7.2/win10 64bit/IDE:Pycharm 2018.3.3
# extracting file(unzip) and write zip file
from zipfile import ZipFile, ZIP_DEFLATED
from os import path, walk, system
import platform

#   open read mode and display and extract all files in zipfile
def unzip(src_zipfile_name, dest_zipfolder_path):
    with ZipFile(src_zipfile_name, 'r') as read_zf:
        read_zf.printdir()
        print("Extracting all files in zipfile")
        # read_zf.extract() #extracting specific file
        read_zf.extractall(dest_zipfolder_path)
    print("DONE!!\n")

# write zipfile from src path to dest file
def zip(src_zipfolder_path, dest_zipfile_name):
    with ZipFile(dest_zipfile_name,'w') as write_zf:
        #iteration for getting file full path by using walk and join function
        for paths, folders, files in walk(src_zipfolder_path):
            for file in files:
                file_path=path.join(paths, file)
                print("compress:: ", file_path)
                write_zf.write(file_path, compress_type=ZIP_DEFLATED,
                               compresslevel=ZIP_DEFLATED)
    print("DONE!!\n")

if __name__=="__main__":
    src_zf_name="D:\\workspaces\\python_study\\zipfolder\\src_test.zip"
    dest_zf_path="D:\\workspaces\\python_study\\zipfolder\\dest_zf_path"
    unzip(src_zipfile_name=src_zf_name, dest_zipfolder_path=dest_zf_path)

    src_zf_path="D:\\workspaces\\python_study\\zipfolder\\src_zf_path"
    dest_zf_name="D:\\workspaces\\python_study\zipfolder\\dest_test.zip"
    zip(src_zipfolder_path=src_zf_path, dest_zipfile_name=dest_zf_name)
    print(system("python --version"))
    print(platform.platform())
    print(platform.machine())




# reference
# https://www.geeksforgeeks.org/working-zip-files-python/
# http://www.hanbit.co.kr/channel/category/category_view.html?cms_code=CMS8947142043
# https://wikidocs.net/8934
# http://psychoria.tistory.com/330?category=581816
# https://docs.python.org/3/library/zipfile.html
# https://github.com/easybuilders/easybuild/wiki/OS_flavor_name_version

