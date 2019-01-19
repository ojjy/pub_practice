# Python 3.7.2/win10 64bit/IDE:Pycharm 2018.3.3
# get the max val by generating array as the user length

from random import randint

#solution1. find the max num by iterating array
def cal_max_val(numlist):
    max_val=numlist[0]

    for idx in range(len(numlist)):
        if(max_val<numlist[idx]):
            max_val=numlist[idx]

    return max_val
user_length=int(input("Please input the length of arr: "))
generate_arr=[randint(100, 999) for _ in range(user_length)]
print(generate_arr)
print("max_val: {}".format(cal_max_val(generate_arr)))


#soultion2. find the max num by sorting array
def cal_max_val_sort(numlist):
    numlist.sort()
    return numlist[len(numlist)-1]

user_length=int(input("Please input the length of arr: "))
generate_arr=[randint(100, 999) for _ in range(user_length)]
print(generate_arr)
print("max_val: {}".format(cal_max_val_sort(generate_arr)))