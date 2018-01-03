# -*- coding:utf-8 -*-

import sys
sys.path.append("..")

import re, json

# 内置模块
from util.request_jwc import request_course
from util.data_struct import get_course_dict
from util.db_controller import insert_func
from pprint import pprint

# 错误模块
from requests.exceptions import ConnectionError


def get_course_struct(re_list):
    """解析获得的区块课程信息
    """
    s = re_list.split("<br>")
    if s.count("&nbsp;") == 0:
        return
    return s

# 使用Re解析获取到的网页数据
def get_course_list(card_no, academic_year, method):
    course_list = list()
    resp = request_course(card_no, academic_year, method)
    course_day = re.findall(r"""<td rowspan="5" class="line_topleft" align="center">(.+)</td>""",resp)
    course_night = re.findall(r"""<td class="line_topleft" rowspan="2"   align="center">(.+)</td>""", resp)
    for i in course_day:
        s = get_course_struct(i)
        if s: course_list.append(s[:-1])
    for i in course_night:
        s = get_course_struct(i)
        if s: course_list.append(s[:-1])
    course_dict = get_course_dict(course_list)
    return course_dict

def re_main(academic_year, start_cardno, end_cardno, logger):
    """使用Re模块匹配课表主程序
    """
    try:
        for i in range(start_cardno, end_cardno):
            course_list = get_course_list(i, academic_year, 1)
            insert_func(i, academic_year, course_list, logger)
    except IndexError:
        logger.err("数据解析错误\t%d"%i)
    except ConnectionError:
        logger.err("网络连接错误\t%d"%i)
    else:
        pass