# -*- coding: utf-8 -*-

# 日志文件操作模块

def insert_log(msg, card_no):
    f = open("./course.log","a")
    f.write("%s\t%d \n"%(msg,card_no))
    f.close()