# -*- coding: utf-8 -*-

import sys
sys.path.append("..")

import requests
from bs4 import BeautifulSoup
from constant.request_const import request_methods, raw_url

def get_course(card_no, academic_year):
    url = "{raw_url}?queryStudentId={card_no}&queryAcademicYear={academic_year}".format(raw_url=raw_url, card_no=card_no, academic_year=academic_year)
    return requests.get(url).text()

def post_course(card_no, academic_year):
    post_data = {"queryStudentId":card_no,"queryAcademicYear":academic_year}
    return requests.post(raw_url, data=post_data).text()

def request_course(card_no, academic_year, method):
    """表链接
    card_no - 学号/一卡通号
    academic_year - 学年
    method - 请求方法 - 1 GET 2 POST
    """
    request_method = request_methods[str(method)]
    if request_method == "GET":
        req = get_course(card_no, academic_year)
    elif request_method == "POST":
        req = post_course(card_no, academic_year)
    print(req)
    return req

if __name__ == "__main__":
    request_course("213171001","17-18-2",1)