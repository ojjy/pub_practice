# try:
#     excution_codes
# except:
#     processing code for try_exception
# code practice for try, except, raise

# 1. when we know the name of exception, write the exception name next to except keyword(optional).
# 1-1. ModuleNotFoundError
try:
    import my_module
except:
    print("not valid module")

# 1-2. ZeroDivisionError
try:
    num1=2/0
except ZeroDivisionError:
    print("not valid for division by zero")

# 1-3. FileNotFoundError or IndexError
try:
    file_name='textfile.txt'
    with open(file_name, 'r') as open_file:
        print(open_file.readline())
    list1 = ["one", "two", "three", "four", "five"]
    print(list1[10])

except FileNotFoundError:
    print("{} is not exists".format(file_name))

except IndexError:
    print("error occur in accessing list")


# 2. when we don't know the name of exception, write "exception" keyword next to except
# 2-1. exception instance
try:
    list1=[1,2,3,4]
    print(list1[5])

except Exception as ex:
    print("\"{}\" exception error occur".format(ex))


# 3. "raise" occur exception intentionally
try:
    raise IndexError
except IndexError:
    print("terminate normally")


numlist=['hundred', 'thousand', 'million', 'billion']
charlist=[100, 1000, 100000, 1000000]
nc_dict={"{}".format(numlist):charlist for numlist, charlist in zip(numlist, charlist)}

print(type(nc_dict))

