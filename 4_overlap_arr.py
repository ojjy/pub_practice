# Python 3.7.2/win10 64bit/IDE:Pycharm 2018.3.3
# generate  numbers in two arrays and push the same value between two arrays

from random import randint

list1_length=100
list2_length=200
list1_max=1000
list2_max=10000
list1=[randint(1, list1_max) for _ in range(list1_length)]
list2=[randint(1, list2_max) for _ in range(list2_length)]

print(list1)
print(list2)

#solution1. By using generally for and if statement
overlap_set1=set()
for list1_index in range(list1_length-1):
    for list2_index in range(list2_length-1):
        if(list1[list1_index] == list2[list2_index]):
            overlap_set1.add(list1[list1_index])

print(overlap_set1)


#solution2. By using list comprehension
overlap_set2={list1[list1_idx] for list1_idx in range(list1_length) for list2_idx in range(list2_length) if(list1[list1_idx]==list2[list2_idx])}
print(overlap_set2)