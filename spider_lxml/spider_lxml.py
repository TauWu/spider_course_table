# -*- coding: utf-8 -*-

import sys
sys.path.append("..")

# 内置模块
from util.request_jwc import request_course
from util.data_struct import get_course_dict
from util.db_controller import insert_func

# 错误模块
from requests.exceptions import ConnectionError

from lxml import etree


# 创建元素
req = request_course(213151001, "17-18-1", 1)

print(req)