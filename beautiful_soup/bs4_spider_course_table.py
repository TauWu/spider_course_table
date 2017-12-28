# -*- coding: utf-8 -*-

import sys
sys.path.append("..")

import requests
from bs4 import BeautifulSoup
from constant.request_const import request_methods, raw_url
from database import db_conn
from pymysql.err import IntegrityError

import re, json

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

def get_course_struct(bsList):
    """传入经过网页分析的bsList,进一步分析变成可用的结构体
    """
    m = re.findall("<td.+rowspan=\".\">(.+)</td>",str(bsList))
    s = m[0].split("<br/>")
    if s.count("\xa0") == 0:
        return
    return s

def get_course_list(bsObj):
    """通过BeautifulSoup对象解析出课程列表
    """
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

def get_course_dict(course_list):
    """通过课程列表解析出课程字典
    最终生成的结构体结构如下:
    {
        "1":[
            {
                "name":"xxx",
                "start_week":1,
                "end_week":16,
                "start_time":1,
                "start_time":;3
                "location":"J1-203"
            }
        ]
    }
    """
    count = 1
    # 存放所有课程信息数据
    course_dict = dict()
    for course in course_list:
        # 存放时间区段课程数据
        course_part_list = list()
        if len(course) == 0:
            course_part_list = []
        else:
            for i in range(0,len(course),3):
                # 存放单节课程数据
                course_single = dict()
                course_single["name"] = course[i]
                result = re.findall("\[(.+)\-(.+)周\](.+)\-(.+)节", course[i+1])
                course_single["start_week"] = result[0][0]
                course_single["end_week"] = result[0][1]
                course_single["start_time"] = result[0][2]
                course_single["end_time"] = result[0][3]
                course_single["location"] = course[i+2]
                course_part_list.append(course_single)
        course_dict[str(count)] = course_part_list
        count = count + 1
    return course_dict

def insert_db(conn, cur, card_no, academic_year, course_info):
    insert_sql = """
    insert into
        s_course_table(card_no, academic_year, course_info)
    values
        ({card_no}, "{academic_year}", "{course_info}")
    """
    cur.execute(insert_sql.format(card_no=card_no,academic_year=academic_year,course_info=course_info))
    conn.commit()

def update_db(conn, cur, card_no, academic_year, course_info):
    update_sql = """
    update
        s_course_table
    set
        course_info = "{course_info}"
    where
        card_no = {card_no} and academic_year = (academic_year)
    """
    cur.execute(update_sql.format(card_no=card_no,academic_year=academic_year,course_info=course_info))
    conn.commit()

def insert_func(card_no):
    bsObj = get_beautiful_soup(str(i),"17-18-2",1)
    course_info = get_course_dict(get_course_list(bsObj))
    conn, cur = db_conn()
    try:
        insert_db(conn, cur, str(i), "17-18-2", str(course_info))
        insert_log("插入新的数据", i)
    except IntegrityError:
        insert_log("更新重复插入", i)
        update_db(conn, cur, str(i), "17-18-2", str(course_info))

def insert_log(msg, card_no):
    f = open("../course.log","a")
    f.write("%s\t%d \n"%(msg,card_no))
    f.close()


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("请输入参数 213150001 213153999")
    else:
        for i in range(int(sys.argv[1]), int(sys.argv[2])):
            try:
                insert_func(i)
            except IndexError:
                insert_log("数据解析错误", i)
            else:
                pass