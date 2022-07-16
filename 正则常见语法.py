"""
预定义字符集(可写在字符集[...]中)
.\d   数字               0~9                             a\dc        a1c
\D  非数字            ^\d                              a\Dc       abc
\s   空白字符串     <空格>\t\r\n\f\v       a\sc        a c
\S  非空白字符集 ^\s                               a\Sc       abc
\w  单词字符        a-zA-Z0-9
\W 非单词字符    ^\w

数量词(用在字符或(...)之后)
*     匹配前一个字符0或无限次  abc*       ab abccc
+     匹配前一个字符1或无限次   abc+       abc abccc
?     匹配前一个字符0或1次        abc?       ab abc
{m} 匹配前一个字符m次             ab{2}c    abbc
"""

import re

# 字符匹配
# rs1 = re.findall('abc', 'abc')
# rs2 = re.findall('abc', 'abd')
# rs3 = re.findall('abc', 'dfsuaiodsfiuhaosudfhabcsfahiodfuhao')
# print(rs1, rs2, rs3)

# rs1 = re.findall('abc', 'abc')
# rs2 = re.findall('a.c', 'abc')
# rs3 = re.findall('a.c', 'adddc')
# rs4 = re.findall('a.c', 'abcadcaccacba\nc')
# rs5 = re.findall('a\.c', 'abca.c')
# print(rs1, rs2, rs3, rs4, rs5)   # ['abc'] ['abc'] [] ['abc', 'adc', 'acc'] ['a.c']

# rs1 = re.findall('a[bc]d', 'abdacd')
# rs2 = re.findall('a[bc]d', 'aed')
# rs3 = re.findall('a[bc]d', 'abcd')
# print(rs1, rs2, rs3)

rs1 = re.findall('\d\d', '1234')  # ['12', '34']
rs2 = re.findall('\w', 'Az1234_阿巴$￥')  # ['A', 'z', '1', '2', '3', '4', '_', '阿', '巴']
rs3 = re.findall('\d*', '123a333')  # ['123', '', '333', '']   字母无法匹配，又*允许匹配空串
rs4 = re.findall('a\d*', 'a123a124b123a')    # ['a123', 'a124', 'a'] 前面或后面加上字母后不会匹配到空串了，*可以为0次
rs5 = re.findall('a\d+', 'a1123aa1')  # ['a1123', 'a1'] +不可以为0次
rs6 = re.findall('a\d?', 'a2a11a00000aa9')  # ['a2', 'a1', 'a0', 'a', 'a9']出现了0次或1次，只匹配1个，数字可以有货没有，a必须有
rs7 = re.findall('a\d{2}', 'a1a22a333a7890') # ['a22', 'a33', 'a78'] 只要出现两个以上数字的都可以匹配，但只显示前两位

print(rs1, rs2, rs3, rs4, rs5, '\n', rs6, rs7)  # 查重用的最多       可以尝试做查重软件？




