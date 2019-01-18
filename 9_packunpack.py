# Python 3.7.2/win10 64bit/IDE:Pycharm 2018.3.3
# practice packing and unpacking by using enumerate(list_name), dict_name.item()...
from random import randint
import os

def list_packunpack(list1p):
    # in case of list, enumerate function return index and value by using pack unpack
    print("\nList Example\n1. Access the values by using index and value variable")
    for index, value in enumerate(list1p):
        print("index={}, value={}".format(index, value))

    print("\n2. Access the values by using starting point of list")
    for info_list1p in enumerate(list1p):
        print("index={}, value={}".format(info_list1p[0], info_list1p[1]))

    print("\n3. Access the values by using unpacking")
    for unp_list1p in enumerate(list1p):
        print("index={}, value={}".format(*unp_list1p))

def dict_packunpack(dict1p):
    #in case of dict, items function return key and value
    print("\nDict Example\n1. Access the values by using key, value variable")
    for key, value in dict1p.items():
        print("key={}, value={}".format(key, value))

    print("\n2. Access the values by using starting point of list")
    for access_dict in dict1p.items():
        print("key={}, value={}".format(access_dict[0], access_dict[1]))

    print("\n3. Access the values by using unpacking")
    for unp_access_dict in dict1p.items():
        print("key={}, value={}".format(*unp_access_dict))

def example_unpack():
    cur_path="D:\\workspaces\\python_study\\zipfolder"
    print("\nos.walk() Exmaple\nwalk function in the os package is example of unpacking")
    print("iteration from current folder to sub folder and files")
    for unpack_v in os.walk(cur_path):
        print("1. Path: {}, \n2. Subfolder: {}, \n3. Files:{} \n".format(*unpack_v))

if __name__=="__main__":
    list1 = [randint(100, 999) for _ in range(10)]
    print(list1)
    list_packunpack(list1)

    dict1 = {"new mexico":[505, 507], "tennessee":[423, 615, 731, 865, 901, 931],
             "new hamphire":603, "hawaii":808, "connecticut":[203, 475, 860, 959],
             "massachusetts":[339, 351, 413, 508, 617, 774, 781, 857, 978]}
    print("\n", dict1)
    dict_packunpack(dict1)

    example_unpack()

