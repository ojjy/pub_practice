# Python 3.7.2/win10 64bit/IDE:Pycharm 2018.3.3

#   solution1. By using array
fibo_arr_length=3#int(input("How many generate the series of fibonacci? \n => "))

fibo_arr=[0,1]
for idx in range(1,fibo_arr_length):
    fibo_arr.append(fibo_arr[idx-1]+fibo_arr[idx])
print(fibo_arr)



#   solution2. By using recursive function

def fibo(num):
    if(num==1):
        return 0
    elif(num==2):
        return 1
    else:
        return fibo(num-1)+fibo(num-2)

fibo_arr2=[]
for index in range(2):
    print("index={}".format(index))
    fibo_arr2.append(fibo(index))
print(fibo_arr2)

# RecursionError: maximum recursion depth exceeded in comparison