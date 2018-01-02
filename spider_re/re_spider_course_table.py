# -*- coding:utf-8 -*-

import sys
sys.path.append("..")

import re, json

# 内置模块
from util.request_jwc import request_course
from util.data_struct import get_course_dict
from util.db_controller import insert_func
from util.logger import insert_log

# 错误模块
from requests.exceptions import ConnectionError

# 使用Re解析获取到的网页数据
def get_course_list(card_no, academic_year, method):
    course_list = list()
    resp = request_course(card_no, academic_year, method)
    print(resp)
    # 获取上午下午课程
    # re.findall()
    # 获取周末晚上课程

if __name__ == "__main__":
    get_course_list(213151001, "17-18-1", 1)