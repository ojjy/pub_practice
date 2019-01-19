# Python 3.7.2/win10 64bit/IDE:Pycharm 2018.3.3
# deciding whether the string is palindrome or not

from math import ceil

input_str=input("Please input string: ")


#remove space and replace lowercase of all words
def preprocess_palin(str):
    str=str.replace(" ", "")
    print("after removing space: {}".format(str))
    str=str.lower()
    print("after changing lowercase: {}".format(str))
    return str



#check whether the word is palindrome or not
def is_palindrome(str):
    for idx in range(int(ceil(str_length/2))):
        if(str[idx]!=str[str_length-idx]):
            print(idx, str[idx], str[str_length-idx])
            return False

    return True

input_str=preprocess_palin(input_str)
print(input_str)
str_length=len(input_str)-1
print(is_palindrome(input_str))


#Testcase: "HELLO  OLLEH", "A santa at NASA" Debugging by using print function