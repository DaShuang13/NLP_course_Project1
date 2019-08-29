#! /usr/bin/python
# -*- coding: utf-8 -*-
import bz2
import codecs
import struct
from urllib import parse
import base64


def base64_encode(string, encode_type):
    return str(base64.b64encode(string.encode(encode_type)), encode_type)


def base64_decode(string, decode_type):
    return str(base64.b64decode(string).decode(decode_type))


if __name__ == '__main__':
    with open("D:/nlp/corpus/stu_db/test.txt", "w") as a:
        print(str(base64.b64encode("中国\n".encode("utf-8")), "utf-8"))
        a.write(str(base64.b64encode("中国123".encode("utf-8")), "utf-8"))
    with open("D:/nlp/corpus/stu_db/test.txt", "r") as b:
        for line in b.readlines():
            print(base64.b64decode(line).decode("utf-8"))
