"""
API
re.findall(pattern, string, flags=0)
作用：扫描string字符串，返回所有与pattern匹配的列表
参数：
    pattern:正则表达式
    string:从此字符串查找
    flags:匹配模式
"""

import re

# 返回匹配结果列表
rs = re.findall('\d+', 'chuan13zhi24')  # ['13', '24']

print(rs)
# flag的作用
rs1 = re.findall('a.bc', 'a\nbc', re.DOTALL) # 加上re.DOTALL之前无法匹配，加上之后可以匹配（flag匹配模式设置为DOTALL）
rs2 = re.findall('a.bc', 'a\nbc', re.S) # re.S可以匹配所有字符
print(rs1, rs2)

#  分组
rs = re.findall('a.+bc', 'a\nbc', re.DOTALL)
rs3 = re.findall('a(.+)bc', 'a\nbc', re.DOTALL)
print(rs, rs3)  # ['a\nbc'] ['\n']

"""
正则表达式中没有（）则返回与整个正则匹配的列表
如果正则表达式中又（），则返回与（）中匹配的内容列表，小括号两边的东西都是负责确定提取数据所在位置
"""



