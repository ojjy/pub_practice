###################################################
# Preparing for Python interview v1
# Key features of Python
# 1. interpreted language
# 2. dynamic type
# 3. support for OOP not public, protected, private
# 4.
# 5. devloper fast run slower than compiled language
# 6. glue lang.

from sys import getsizeof as get_size
num1 = 1
print(get_size(num1))
num_list = [nums for nums in range(0,10000)]
print(f"get_size(num_list): {get_size(num_list)}")
#############################################################
###################### lambda function ######################
a = lambda x, y:x+y
print("a = lambda x, y:x+y | a(1,2)=> ", a(1,2))


#########################################################
################### enumerate ################

if __name__ == "__main__":
    arr1 = [10, 20, 30, 40, 50, 60]

    for idx, value in enumerate(arr1):
        print("index: {}, value: {}".format(idx, value))

######################
## args : N개의 매개변수를 넘기겠다는 표시
def args_func(*args, num1):
    print("type(args): ", type(args))
    for argi in args:
        print(argi)
    print(num1)

if __name__ == "__main__":
    args_func("python", "C", "Java", "Matlab", num1=100)
###################################################################
####### kwargs: args와 동일한 파라미터 인데, 각 파라미터 마다 이름이 있다. ######
def kwargs_func(num2, **kwargs,):
    for name, job in kwargs.items():
        print("name: {}, job: {}".format(name, job))
    print(num2)

if(__name__ == "__main__"):
    kwargs_func(Kelly="Programmer", Sung="Mechanical Engineer", Jenny="Physician", num2=1000)

##################################################################################
#################### OOP ####################

class Computer:
    processor = "Xeon"

    def set_processor(self, new_processor):
        self.processor = new_processor
        return self.processor

    def get_processor(self):
        return self.processor

class Desktop(Computer):
    ram = "32GB"
    HDD = "1TB"
    os = "Windows7 Pro 64"

class Laptop(Computer):
    ram="64GB"
    HDD="1TB"
    os = "Mac OS Big Sur"

if __name__ == "__main__":
    mycom = Computer()
    print("Base class:: {}, {}".format(mycom.get_processor(), mycom.processor))

    mylaptop = Laptop()
    print("Laptop Class:: os: {}, processor: {}".format(mylaptop.os, mylaptop.processor))


# #References
# https://www.edureka.co/blog/interview-questions/python-interview-questions/
# https://frhyme.github.io/python/python_check_memory_usage/