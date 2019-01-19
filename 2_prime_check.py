# Python 3.7.2/win10 64bit/IDE:Pycharm 2018.3.3
# 10 numbers generate random number from 3 to user max
# and check whether it is prime num or not and push the prime number at the array

from random import randint

def is_prime(num):
    for idx in range(2,num-1):
        print(idx)
        if(num%idx==0):
            return False

    return True



user_max=int(input("Please input the max: "))
num_arr=[randint(3,user_max) for _ in range(10)]
prime_arr=[]
print(num_arr)
for idx in range(len(num_arr)-1):
    if is_prime(num_arr[idx]):
        prime_arr.append(num_arr[idx])

print(prime_arr)