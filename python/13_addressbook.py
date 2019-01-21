# Python 3.7.2/win10 64bit/IDE:Pycharm 2018.3.3
import sqlite3 as dbms
from datetime import date

class address_book():

    # Create DB => connect DBMS => create table
    def __init__(self):
        try:
            self.con=dbms.connect('address_book.db')
            self.cur=self.con.cursor()
            self.table_name='addr_book'
#            self.cur.execute('DROP TABLE IF EXISTS {}'.format(self.table_name))
        except Exception as ex:
            print("ERROR:: CAN NOT CONNECT THE DB : {}".format(ex))

        self.cur.execute('''CREATE TABLE IF NOT EXISTS {}(name TEXT, phone_num TEXT, email TEXT, birthday DATE, group_num SMALLINT, note TEXT, idx INTEGER PRIMARY KEY AUTOINCREMENT)'''.format(self.table_name))

    # read file one by one and split '/' and save each variable then insert
    def add_info_text(self):
        try:
            with open('13_addressbook.txt', 'r') as open_text:
                for line in open_text:
                    self.name, self.phone_num, self.email, self.birthday, self.group_num, self.note=line.split('/')
                    #print(self.name, self.phone_num, self.email, self.birthday, self.group_num, self.note)
                    self.group_num=int(self.group_num)
                    year, month, day=self.birthday.split('-')
                    self.birthday=date(int(year), int(month), int(day))
                    self.note=self.note.replace("\n", "")
                    self.cur.execute('''INSERT INTO addr_book(name, phone_num, email, birthday, group_num, note) values (?,?,?,?,?,?)''',(self.name, self.phone_num, self.email, self.birthday, self.group_num, self.note))
                    self.con.commit()
        except FileNotFoundError:
            print("ERROR::CANNOT OPEN FILE::FileNotFoundError")

    # insert query SET func
    def add_info(self):
        try_count=0
        while try_count<=3:
            self.name, self.phone_num, self.email, self.birthday, self.group_num, self.note=input("Please input name, phone num, email, birthday, group_num, note: (split by using / char)").split("/")
            # print("name={}, phone_num={}, email={}, self.birthday={}, self.group_num={}, self.note={}".format(self.name, self.phone_num, self.email, self.birthday, int(self.group_num), self.note))
            try_count=try_count+1
            self.group_num=int(self.group_num)
            year, month, day=self.birthday.split('-' or ' ')
            self.birthday=date(int(year), int(month), int(day))

            if isinstance(self.name, str) and isinstance(self.phone_num, str) and isinstance(self.email, str) and isinstance(self.birthday, date) and isinstance(self.group_num, int) and isinstance(self.note, str):
                print("correct")
                self.cur.execute("INSERT INTO addr_book (name, phone_num, email, birthday, group_num, note) values (?,?,?,?,?,?)",(self.name, self.phone_num, self.email, self.birthday, self.group_num, self.note))
                self.con.commit()
                break
            else:
                print("{}번 입력하셨습니다 최대 횟수:3".format(try_count))
                continue


    # select all GET func
    def display_all_info(self):
        note='abq_church'
        # self.cur.execute('SELECT COUNT(*) FROM addr_book')
        print("name,\tphone_num,\temail,\tbirthday,\tgroup_num,\tnote,\tindex")
        for name, phone_num, email, birthday, group_num, note, index in self.cur.execute('SELECT * FROM addr_book'):
            print("{},\t{},\t{},\t{},\t{},\t{},\t{}".format(name, phone_num, email, birthday, group_num, note, index))

    # select specific queries
    def search_info(self, item ,keyword):
        for row in self.cur.execute('SELECT * FROM addr_book WHERE "{}"="{}"'.format(item, keyword)):
            print(row)

    # update specific queries
    def update_info(self):
        pass

    # delete specific queries
    def delete_info(self):
        pass

    def remove_all(self):
        pass
    # input and execute db command
    def input_db_cmd(self):
        cmd_msg=input("Please input db command: ")
        try:
            self.cur.execute(cmd_msg)
            self.con.commit()
            print("SUCCESS TRANSACTION: {}".format(cmd_msg))
            if cmd_msg.split(' ')[0] == 'select':
                print("select execution")
                for fetch in self.cur.fetchall():
                    print(fetch)

        except Exception as ex:
            print("cannot execution this cmd:{}, error msg {}".format(cmd_msg, ex))

def usage():
    pass

def main():
    adr1=address_book()
    usage()
    while True:
        dbop=input("Please input operation (insert/display/cmd/update/delete/search/stop): ")
        if dbop=='insert':
            adr1.add_info_text()
            continue
        elif dbop=='display':
            adr1.display_all_info()
            continue
        elif dbop=='cmd':
            adr1.input_db_cmd()
            continue
        elif dbop=='update':
            adr1.update_info()
            continue
        elif dbop=='delete':
            adr1.delete_info()
            continue
        elif dbop=='search':
            adr1.search_info("name", "kelly")
            continue
        elif dbop=='stop':
            break
        else:
            print("input error")
            continue
if __name__=="__main__":
    main()
