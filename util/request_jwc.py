# -*- coding: utf-8 -*-

import requests
from constant.request_const import request_methods, raw_url

# 不同的请求方式获取课表网页数据

def get_course(card_no, academic_year):
    """获取课表(GET)
    """
    url = "{raw_url}?queryStudentId={card_no}&queryAcademicYear={academic_year}".format(raw_url=raw_url, card_no=card_no, academic_year=academic_year)
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
        return get_course(card_no, academic_year)
    elif request_method == "POST":
        return post_course(card_no, academic_year)