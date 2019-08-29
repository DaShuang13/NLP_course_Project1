#! /usr/bin/python
# -*- coding: utf-8 -*-
from io import BytesIO

import MySQLdb
import math
import base64
import pandas as pd


def base64_encode(string, encode_type):
    """
    base64位的编码
    :param string: 需要编码的内容
    :param encode_type: 编码类型
    :return: 返回编码后的结果
    """
    return str(base64.b64encode(string.encode(encode_type)), encode_type)


def base64_decode(string, decode_type):
    """
    base64位的解码
    :param string: 需要解码的字符串内容
    :param decode_type: 解码类型
    :return: 返回解码后的结果
    """
    return str(base64.b64decode(string).decode(decode_type))


def connect_mysql(local_path, url, db, username, password):
    """
    连接数据库，并导出到本地路径
    :param local_path: 本地路径
    :param url: mysql url
    :param db: 数据库
    :param username: 用户名
    :param password: 密码
    :return: 无返回值
    """
    with open(local_path, "w", encoding="utf-8") as db_data:
        db = MySQLdb.connect(url, username, password, db, charset="utf8")
        cursor = db.cursor()
        step = 1000
        start = 0
        end = step
        max_record_count = 89611
        max_iter_num = math.ceil(float(max_record_count) / float(step))
        for i in range(max_iter_num):
            # 元信息:
            sql = "select * from stu_db.news_chinese where id > {0} and id <= {1};".format(start, end)  # 89611
            cursor.execute(sql)
            result = cursor.fetchall()
            for item in result:
                db_data.write("{}\n".format("\001".join(
                    [str(item[0]), item[1], item[2], base64_encode(item[3], "utf-8"), base64_encode(item[4], "utf-8"),
                     base64_encode(item[5], "utf-8"), item[6]])))
                # id,author,source,content(encode),feature(encode),title(encode),url
            db_data.flush()
            start += step
            end += step
        db.close()


def load_data(local_path):
    raw_data = []
    with open(local_path, "r", encoding="utf-8") as db_data:
        for line in db_data.readlines():
            raw_data.append(line.strip().split("\001"))
    return pd.DataFrame(raw_data, columns=["id", "author", "source", "content", "feature", "title", "url"])


def main():
    # connect_mysql("D:/nlp/corpus/stu_db/news_chinese.txt", "*","*", "*", "*")
    print(load_data("D:/nlp/corpus/stu_db/news_chinese.txt"))


if __name__ == '__main__':
    main()
