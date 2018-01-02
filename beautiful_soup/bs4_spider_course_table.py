# -*- coding: utf-8 -*-

import sys
sys.path.append("..")

from bs4 import BeautifulSoup
import re, json

# 内置模块
from util.request_jwc import request_course
from util.data_struct import get_course_dict
from util.db_controller import insert_func

# 错误模块
from requests.exceptions import ConnectionError

# 使用BeautifulSoup解析获取到的网页数据
def get_beautiful_soup(card_no, academic_year, method):
    """获取BeautifulSoup对象
    + `card_no`学号/一卡通号
    + `academic_year`学年
    + `method`请求方法_详情见constant中的定义_
    """
    return BeautifulSoup(request_course(card_no, academic_year, method))

def get_course_struct(bsList):
    """传入经过网页分析的bsList,进一步分析变成可用的结构体
    """
    m = re.findall("<td.+rowspan=\".\">(.+)</td>",str(bsList))
    s = m[0].split("<br/>")
    if s.count("\xa0") == 0:
        return
    return s

def get_course_list(card_no, academic_year, method):
    """通过card_no, academic_year, method生成BeautifulSoup对象解析出课程列表
    """
    bsObj = get_beautiful_soup(card_no, academic_year, method)
    course_list = list()
    # 获取上午下午课程
    for i in bsObj.findAll("td",{"class":"line_topleft","rowspan":"5","align":"center"}):
        s = get_course_struct(i)
        if s: course_list.append(s[:-1])
    # 获取晚上周末课程
    for i in bsObj.findAll("td",{"class":"line_topleft","rowspan":"2","align":"center"}):
        s = get_course_struct(i)
        if s: course_list.append(s[:-1])
    return course_list

def bs4_main(academic_year, start_cardno, end_cardno, logger):
    for i in range(start_cardno, end_cardno):
        try:
            course_info = get_course_dict(get_course_list(i, academic_year, 1))
            insert_func(i, academic_year, course_info, logger)
        except IndexError:
            logger.err("数据解析错误\t%d"%i)
        except ConnectionError:
            logger.err("网络连接错误\t%d"%i)
        else:
            pass