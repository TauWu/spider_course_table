# -*- coding: utf-8 -*-

# 数据库操作动作
from database import db_conn
from pymysql.err import IntegrityError
from .logger import insert_log

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

def insert_func(card_no, academic_year, course_info):
    conn, cur = db_conn()
    try:
        insert_db(conn, cur, str(card_no), academic_year, str(course_info))
        insert_log("[LOG]插入新的数据", card_no)
    except IntegrityError:
        insert_log("[LOG]更新重复插入", card_no)
        update_db(conn, cur, str(card_no), academic_year, str(course_info))