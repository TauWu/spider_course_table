# 并行运行跑批程序

> ./course.log
ps -ef | grep bs4_spider_course_table | cut -c 10-15 | xargs kill -s 9

cd ./beautiful_soup

(python3 bs4_spider_course_table.py 213140001 213143999) &
(python3 bs4_spider_course_table.py 213150001 213153999) &
(python3 bs4_spider_course_table.py 213160001 213163999) &
(python3 bs4_spider_course_table.py 213170001 213173999) &
