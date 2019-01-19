# Python 3.7.2/win10 64bit/IDE:Pycharm 2018.3.3
# cow and bull- cow: the same digit with same place, bull - same number but not same place

from random import randint as produce_num

def generate_num():
    gene_num=str(produce_num(1000, 9999))
    return start_game(gene_num)

def welcome_game():
    nickname=input("Please input your nick name: ")
    print("Hello, {}.\nWelcome this game".format(nickname))
    return nickname

def start_game(com_input):
    try_count=0
    nickname=welcome_game()
    data_file="8_cow_and_bull.txt"
    while True:
        cow = bull = 0
        try_count=try_count+1
        print("\nYour try count is {}".format(try_count))
        user_input=str(int(input("Please input num from 1000 to 9999\n =>")))
        for index in range(len(user_input)):
            if user_input[index] ==com_input[index]:
                cow=cow+1
            else: #user_input[index] != com_input[index]
                if user_input[index] in com_input:
                    bull=bull+1
        print("cow:{}, bull:{}, user_input:{}".format(cow, bull, user_input))
        if cow==4:
            break
    print("correct!! user_input:{}, {}:com_input, try_count:{}".format(user_input, com_input, try_count))
    return save_rank(data_file, try_count, nickname)

# displaying score and nickname by opening text file - show data by reading line one by one
def display_rank():
    with open("8_cow_and_bull.txt", "r") as rank_file:
        for line in rank_file:
            print(line.replace("\n", ""))

# After reading file, sort with new score and nickname and return dictionary
def load_data(data_file, new_try_count, new_nick_name):
    skip_times=5
    rank_data=dict()
    sorted_rank_data=dict()
    with open(data_file, "r") as rank_file:
        #line skip for header
        for times in range(skip_times):
            skip_line=rank_file.readline()

        #read one line and save each data
        for line in rank_file:
            temp_line=line.split(',\t')
            nickname=temp_line[1]
            try_count=int(temp_line[2].replace("\n", ""))
            rank_data[nickname]=try_count
        rank_data[new_nick_name]=new_try_count

        sorted_rank_data=dict(sorted(rank_data.items(), key=lambda x :x[1]))
        return sorted_rank_data

# writing text file with new ranking data
def save_rank(data_file, new_try_count, new_nick_name):
    line_counter=0
    rank_data=load_data(data_file, new_try_count, new_nick_name)
    with open(data_file, "w") as rank_file:
        rank_file.write("================================\nWELCOME TO COW N BULL GAME\n================================\n"
                        "rank#\tnickname\ttry_count\n================================\n")
        for nickname, trycount in rank_data.items():
            line_counter=line_counter+1
            rank_file.write("{},\t{},\t{}\n".format(line_counter, nickname, trycount))

if __name__=="__main__":
    display_rank()
    generate_num()
    display_rank()
