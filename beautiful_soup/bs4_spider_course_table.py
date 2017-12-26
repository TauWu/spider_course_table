# -*- coding: utf-8 -*-

import sys
sys.path.append("..")

import requests
from bs4 import BeautifulSoup
from constant.request_const import request_methods, raw_url

def get_course(card_no, academic_year):
    """获取课表(GET)
    """
    url = "{raw_url}?queryStudentId={card_no}&queryAcademicYear={academic_year}".format(raw_url=raw_url, card_no=card_no, academic_year=academic_year)
    print(url)
    return requests.get(url).text

def post_course(card_no, academic_year):
    """获取课表(POST)
    """
    post_data = {"queryStudentId":card_no,"queryAcademicYear":academic_year}
    return requests.post(raw_url, data=post_data).text


def request_course(card_no, academic_year, method):
    """发起课表请求
    + `card_no`学号/一卡通号
    + `academic_year`学年
    + `method`请求方法_详情见constant中的定义_
    """
    request_method = request_methods[str(method)]
    if request_method == "GET":
        req = get_course(card_no, academic_year)
    elif request_method == "POST":
        req = post_course(card_no, academic_year)
    return req

def get_beautiful_soup(card_no, academic_year, method):
    """获取BeautifulSoup对象
    + `card_no`学号/一卡通号
    + `academic_year`学年
    + `method`请求方法_详情见constant中的定义_
    """
    return BeautifulSoup(request_course(card_no, academic_year, method))

if __name__ == "__main__":
    bsObj = get_beautiful_soup("213122983","17-18-2",1)
    # 获取上午下午课程
    for i in bsObj.findAll("td",{"class":"line_topleft","rowspan":"5","align":"center"}):
        print(i,'\n')
    # 获取晚上周末课程
    for i in bsObj.findAll("td",{"class":"line_topleft","rowspan":"2","align":"center"}):
        print(i,'\n')