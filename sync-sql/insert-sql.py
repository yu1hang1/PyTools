import datetime
import mysql.connector


class database:
    def __init__(self, ip, port, user, psw, dbname):
        try:
            con = mysql.connector.connect(
                host=ip,
                user=user,
                password=psw,
                port=port,
                database=dbname,
                charset='utf8',
                buffered=True)
            print('数据库连接成功')
            self.con = con  # con在其他类方法中还要多次调用，所以定义为成员变量
        except mysql.connector.Error as e:
            print('连接失败', str(e))

    def insert_tb(self, sql, data_insert):
        try:
            cursor = self.con.cursor()
            cursor.executemany(sql, data_insert)
            self.con.commit()
            print('数据插入成功', data_insert)
        except mysql.connector.Error as e:
            self.con.rollback()
            print('插入失败', str(e))
            cursor.close()


if __name__ == "__main__":
    db = database('127.0.0.1', '3306', 'root', '1qaz!QAZ', 'test')
    for i in range(1, 2):
        str_i = str(i)
        book_name = "我爱祖国" + str_i
        book_id = 1400 + i
        author_id = 1400 + i
        pages = 300 + i
        press = "北京景出版社" + str_i
        cup_type = "银奖"
        cup_time = datetime.datetime.now()
        author_name = "xxx" + str_i
        content = "我会长说唱" + str_i
        sql_insert1 = 'INSERT INTO books(book_id,author_id,book_name,pages,press)VALUES (%s,%s,%s,%s,%s);'
        sql_insert2 = 'INSERT INTO Awards(book_id,cup_type,cup_time,author_id)VALUES (%s,%s,%s,%s);'
        sql_insert3 = 'INSERT INTO author(author_id,author_name,content)VALUES (%s,%s,%s);'
        data_insert = []
        var1 = (book_id, author_id, book_name, pages, press)
        var2 = (book_id, cup_type, cup_time, author_id)
        var3 = (author_id, author_name, content)
        data_insert.append(var3)
        db.insert_tb(sql_insert3, data_insert)
