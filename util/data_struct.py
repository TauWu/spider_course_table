# -*- coding:utf-8 -*-

# 将通过不同方式获取的课程列表转换为字典

import re

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