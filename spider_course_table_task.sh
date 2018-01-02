# 并行运行跑批程序

> ./course.log

ps -ef | grep bs4_spider_course_table | cut -c 10-15 | xargs kill -s 9

(python3 spider_main.py 1 213140001 213143999 17_18_1) &
(python3 spider_main.py 1 213150001 213153999 17_18_1) &
(python3 spider_main.py 1 213160001 213163999 17_18_1) &
(python3 spider_main.py 1 213170001 213173999 17_18_1) &
