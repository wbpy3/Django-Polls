import sqlite3
import time


class WriteDataIntoDb:
    current = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    conn = sqlite3.connect('../Django_polls/db.sqlite3')  # 连接数据库
    c = conn.cursor()

    # 通过sql语句写入直接
    def write_questions(self):
        self.c.execute("INSERT INTO polls_question "
                       "(question_text, pub_date) "
                       "VALUES ('what is your name','{0}')".format(str(self.current)))

        self.conn.commit()
        self.conn.close()

    def write_choice(self, answer, question_id, ):
        self.c.execute("INSERT INTO polls_choice "
                       "(choice_text, votes, question_id) "
                       "VALUES ('{0}',0,{1})".format(answer, question_id))

        self.conn.commit()
        self.conn.close()


if __name__ == '__main__':
    write_obj = WriteDataIntoDb()
    write_obj.write_choice("小李子", 2)  # 第二个参数是问题的id
