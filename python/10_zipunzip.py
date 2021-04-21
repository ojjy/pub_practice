# Python 3.7.2/win10 64bit/IDE:Pycharm 2018.3.3
# extracting file(unzip) and write zip file
# update. support multi language
from zipfile import ZipFile, ZIP_DEFLATED
from os import path, walk, system
import platform

#   open read mode and display and extract all files in zipfile
def unzip(src_zipfile_name, dest_zipfolder_path):
    with ZipFile(src_zipfile_name, 'r') as read_zf:
        filesinzip = read_zf.infolist() #ALL of file objects in zip file
        print(filesinzip)
        for file in filesinzip:
            try:
                print(file.filename.encode('cp437').decode('euc-kr', 'ignore'))
                file.filename = file.filename.encode('cp437').decode('euc-kr', 'ignore')
                read_zf.extract(file, dest_zipfolder_path)
            except Exception as e:
                print(src_zipfile_name,"error", e)
                raise Exception
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
    # src_zf_name = "C:\\Users\\yejinjo\\Desktop\\db12.zip"
    # dest_zf_path = "C:\\Users\\yejinjo\\Desktop\\db12"

    src_zf_name="T:\\pemfile.zip"
    dest_zf_path="T:\\pem"
    unzip(src_zipfile_name=src_zf_name, dest_zipfolder_path=dest_zf_path)
    #
    # src_zf_path="D:\\workspaces\\python_study\\zipfolder\\src_zf_path"
    # dest_zf_name="D:\\workspaces\\python_study\zipfolder\\dest_test.zip"
    # zip(src_zipfolder_path=src_zf_path, dest_zipfile_name=dest_zf_name)
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
