import re

# 在不适用r原串时，遇到转移符
# rs = re.findall('a\nbc', 'a\nbc')
# print(rs)
# rs = re.findall('a\nbc', 'a\\nbc')
# ra = re.findall('a\\\\nbc', 'a\\nbc')
# print(rs, ra)

# r原串在正则中可以消除转移符带来的影响
rs = re.findall(r'a\\nbc', 'a\\nbc')
print(rs)

















