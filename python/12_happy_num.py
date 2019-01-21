

# 해피 넘버 인지 판별하고 해피 넘버 이면 그 넘버 리턴
# 언해피 넘버이면 0을 리턴
# 몫, 나머지, 제곱수의 합
def happy_num(num):
    numop=num
    digit_list=list()
    #print("num={}".format(num))
    for times in range(1, 100000):
        q,r=divmod(numop,10)
        digit_list.append(r)
        numop=int(numop*0.1)
     #   print("q={}, r={}, r={}".format(q, r, numop))
        if q==0:
            break

        else:
            continue

    #print(digit_list)

    value=0
    for index in range(len(digit_list)):
     #   print("value={}, digit[{}]={}".format(value, index, digit_list[index]))
        value=value+digit_list[index]*digit_list[index]
    #print("value={}".format(value))
    if value==1: return num
    else: return happy_num(value)

if __name__=="__main__":
    happy_num_list=list()
    try:
        for i in range(1000):
            happy_num(i)
        happy_num_list.append(i)
    except RecursionError:


        print(i)