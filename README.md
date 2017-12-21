# 项目名称
spider_course_table
<p>
课表爬虫

# 项目目标
提供各种花式爬取学生课表的Python代码
<p>
提取网址: http://xk.urp.seu.edu.cn/jw_service/service/stuCurriculum.action
<p>

## GET请求
```py
import requests

#查询参数
#  queryStudentId:    学生一卡通/学号
#  queryAcademicYear: 查询学期

requests.get("http://xk.urp.seu.edu.cn/jw_service/service/stuCurriculum.action?queryStudentId=213171001&queryAcademicYear=17-18-2")
```
## POST请求
```py
import requests

#查询参数
#  queryStudentId:    学生一卡通/学号
#  queryAcademicYear: 查询学期

data = {
    "queryStudentId": "213171001",
    "queryAcademicYear": "17-18-2"
}
requests.post("http://xk.urp.seu.edu.cn/jw_service/service/stuCurriculum.action",data=data)
```

## Selenium模拟登录
```py
from selenium import webdriver

def start_run(card_no):
    # 打开浏览器/网页
    raw_url = "http://xk.urp.seu.edu.cn/jw_service/service/stuCurriculum.action"
    browser = webdriver.Chrome()
    browser.get(raw_url)
    browser.set_window_size(1200,800)
    
    # 输入学生ID
    student_id_element = browser.find_element_by_css_selector("#queryStudentId")
    student_id_element.send_keys(card_no)

    # 点击确定按钮
    submit_element = browser.find_element_by_css_selector("#stuCurriculum_0")
    submit_element.click()

    # 保持在查询结果页面 等待后续操作...
```
# 作者信息
- Tau Woo
- 2017-12-21 15:13:16

# 环境配置
## Ubuntu
### Python3的安装
```sh
# Python3 安装
sudo apt-get install python3
sudo apt-get intsall python3-pip
```