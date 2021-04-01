## args : N개의 매개변수를 넘기겠다는 표시
def args_func(*args, num1):
    print("type(args): ", type(args))
    for argi in args:
        print(argi)
    print(num1)

def kwargs_func(num2, **kwargs,):
    print((type(kwargs)))
    for name, job in kwargs.items():
        print("name: {}, job: {}".format(name, job))
    print(num2)

def kwargs_args_func(*args, **kwargs):
    for argsi in args:
        print(argsi)
    for data in kwargs.items():
        print(data)

if __name__ == "__main__":
    # args_func("python", "C", "Java", "Matlab", num1=100)
    # args_func("gc", "holdings", "dp",  num1=100)
    # kwargs_func(Kelly="Programmer", Sung="Mechanical Engineer", Jenny="Physician", num2=1000)
    # kwargs_args_func("helloworld", "dp",num=1, par1="gc", par2=1000)
    mynum = 1000
    mystr = 'Hello World!'
    print("{mystr} New-style formatting is {mynum}x more fun!".format(**locals()))
