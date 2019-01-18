# Python 3.7.2/win10 64bit/IDE:Pycharm 2018.3.3
# twenty questions game : computer generate number randomly and person need to answer the number
# and save the try_count in the text file for getting score after terminating process
from random import randint

# display top 10 by reading 10 times as one line
def display_top10():
    displayed_lines=15 # include two lines both === and titles(rank#, nickname, try_count)
    line_counter=0
    with open("6_twenty_questions.txt", "r") as open_file:
        for line in open_file:
            #print string after removing one time newline because of including newline 2 times both print func and line str
            print(line.replace("\n", ""))
            line_counter=line_counter+1
            if(line_counter>=displayed_lines):
                break

# input the number until it is the same both generate_num and user_input
# and return results generate_num, nickname and try_count
def twenty_questions():
    generate_num=randint(1,99)
    try_count=1

    while True:
        user_input=int(input("Please input num: "))
        if(generate_num>user_input):
            print("FAIL::trying to {} time(s), answer > {} :user_input\n".format(try_count, user_input))
            try_count=try_count+1
            continue
        elif(generate_num<user_input):
            print("FAIL::trying to {} time(s), answer < {} :user_input\n".format(try_count, user_input))
            try_count=try_count+1
            continue
        else:
            print("SUCCESS::tried to {} time(s), answer:{}\n".format(try_count, generate_num))
            break

    nickname=input("Please input your nickname: ")
    return [generate_num, nickname, try_count]



# Read ranking data from text file except 5 lines(skip not gamedata)
# Save ranking data to rank_data and convert dictionary type(total_rank_data)
# Sort ranking data and write to text file
def save_gamedata(new_nickname, new_try_count):
    total_rank_data={}
    skip_times=5
    sorted_rank_data={}
    with open("6_twenty_questions.txt", "r") as fp:
        for skip_line in range(skip_times):
            skip_line=fp.readline()

        for line in fp:
            rank_data=line.split(',\t')
            nickname=rank_data[1]
            try_count=int(rank_data[2])
         #  total_rank_data.append([nickname, try_count])
            total_rank_data[try_count]=nickname
    total_rank_data[new_try_count]=new_nickname
   # total_rank_data.append([new_nickname, new_try_count]

    sorted_rank_data=dict(sorted(total_rank_data.items(), key=lambda x: x[0]))
    idx=0
    with open("6_twenty_questions.txt", "w") as open_file:
        open_file.write("================================\nWELCOME TO 20Q WORLD\n================================\nrank#\tnickname\ttry_count\n================================\n")
        for key, value in sorted_rank_data.items():
            idx=idx+1
            open_file.write("{},\t{},\t{}\n".format(idx, value, key))



if __name__=="__main__":
    display_top10()
    game_data=twenty_questions()
    print(game_data[1], game_data[2])
    save_gamedata(game_data[1], game_data[2])
    # save_gamedata("hello", 20)
