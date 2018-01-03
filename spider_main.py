# -*- coding: utf-8 -*-
# - 主程序入口 -

import sys
from spider_bs.bs4_spider_course_table import bs4_main
from spider_re.re_spider_course_table import re_main
from util.logger import log_base

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("输入样式 python3 spider_main.py 1 213150001 213153999 17_18_1")
    else:
        logger = log_base("seuxw")
        method = int(sys.argv[1])
        start_cardno = int(sys.argv[2])
        end_cardno = int(sys.argv[3])
        academic_year = sys.argv[4].replace("_","-")
        if method == 1:
            bs4_main(academic_year, start_cardno, end_cardno, logger)
        elif method == 2:
            re_main(academic_year, start_cardno, end_cardno, logger)
        else:
            logger.err("不存在这种操作!")